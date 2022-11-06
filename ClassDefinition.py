import serial
import time
import datetime
import os
import sys
import glob
import pandas as pd
import numpy as np
import math
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import sip
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator
matplotlib.use('QT5Agg')


class classHardware_():
    def __init__(self, port):
        self.port = port
        self.status = "close"
        self.door = self.assign_port()

    def assign_port(self):
        try:
            door = serial.Serial(self.port, 115200, timeout=5)
            door.close()
            return door
        except serial.serialutil.SerialException:
            Warning("No COM port defined for load" + str(self.port))
            return None

    def open_door(self):
        if self.status == "close":
            self.door.open()
            self.status = "open"

    def close_door(self):
        if self.status == "open":
            self.door.close()
            self.status = "close"

class Load(classHardware_):
    def __init__(self, port):
        super().__init__(port)
        self.list_resistance = None

    def receive_result(self):
        load_output = []
        self.open_door()
        self.door.write(b':MEASure:CURRent?\n')
        time.sleep(0.05)
        load_output.append(float(self.door.readline().decode('utf-8').rstrip('A\n')))
        self.door.write(b':MEASure:VOLTage?\n')
        time.sleep(0.05)
        load_output.append(float(self.door.readline().decode('utf-8').rstrip('V\n')))
        self.close_door()
        return load_output

    def send_resistance_to_load(self, res):
        self.open_door()
        set_res_str = f':RES {res}OHM\n'
        self.door.write(set_res_str.encode('utf-8'))
        set_input_str = f':INPut ON\n'
        self.door.write(set_input_str.encode('utf-8'))
        time.sleep(0.5)
        self.close_door()

    def sweep_measurement(self, res_min, res_max, resistance_nb_step):
        voltage_list = []
        current_list = []
        self.list_resistance = np.logspace(math.log10(res_max), math.log10(res_min), num=resistance_nb_step, base=10)
        for res in self.list_resistance:
            self.send_resistance_to_load(res)
            result = self.receive_result()
            current_list.append(result[0])
            voltage_list.append(result[1])
        return voltage_list, current_list

class Cell():
    def __init__(self, ref):
        self.ref = ref
        self.isc = None
        self.voc = None
        self.ff = None
        self.pce = None
        self.voltage_mpp = None
        self.idx_mpp = None
        self.df_iv = pd.DataFrame()

    def measure_cell(self, oload, res_min, res_max, resistance_nb_step):
        self.get_df_iv(oload, res_min, res_max, resistance_nb_step)
        self.get_cell_parameters()

    def get_df_iv(self, oload, res_min, res_max, resistance_nb_step):
        voltage_list = []
        current_list = []
        voltage_list, current_list = oload.sweep_measurement(res_min, res_max, resistance_nb_step)
        self.df_iv = pd.DataFrame(list(zip(voltage_list, current_list)), columns=['Voltage (V)', 'Current (A)'])

    def get_cell_parameters(self):
        self.get_isc()
        self.get_voc()
        self.get_fill_factor()
        self.get_pce()

    def get_isc(self):
        self.isc = self.df_iv['Current (A)'][self.df_iv.index[-1]]

    def get_voc(self):
        self.voc = self.df_iv['Voltage (V)'][self.df_iv.index[0]]

    def get_fill_factor(self):
        self.df_iv['Power (W)'] = self.df_iv['Voltage (V)'] * self.df_iv['Current (A)']
        self.idx_mpp = self.df_iv['Power (W)'].idxmax()
        self.voltage_mpp = self.df_iv['Voltage (V)'][self.idx_mpp]
        impp = self.df_iv['Current (A)'][self.idx_mpp]
        if self.isc * self.voc != 0:
            self.ff = (impp * self.voltage_mpp) / (self.isc * self.voc)
        else:
            self.ff = 0

    def get_pce(self):
        self.pce = self.isc * self.voc * self.ff

    def mpp_tracking(self, oload):
        oload.send_resistance_to_load(oload.list_resistance[self.idx_mpp])

class Data_file():
    def __init__(self, path, ref):
        self.path = path
        self.ref = ref
        self.timestamp = None
        self.date = None
        self.df_params = None
        self.df_iv = self.get_last_iv()
        self.df_full_params = self.get_df_full_params()

    def get_df_full_params(self):
        path_summary = f'{self.path}/Summary'
        if os.path.exists(path_summary):
            filename = f'Cell{self.ref}_param.txt'
            return pd.read_csv(path_summary + '/' + filename, delimiter = "\t")
        else:
            return pd.DataFrame()

    def get_last_iv(self):
        path_cell = f'{self.path}/Cell{self.ref}'
        if os.path.exists(path_cell):
            file = [f for f in os.listdir(path_cell) if os.path.isfile(os.path.join(path_cell, f))][-2]
            return pd.read_csv(path_cell + '/' + file, delimiter = "\t")
        else:
            return pd.DataFrame()

    def save_dfs(self, df_iv, isc, voc, ff, pce, mpp):
        self.get_data(df_iv, isc, voc, ff, pce, mpp)
        self.save_dfs_to_files()

    def get_data(self, df_iv, isc, voc, ff, pce, mpp):
        self.df_iv = df_iv.round(3)
        self.get_timestamp()
        self.df_params = pd.DataFrame({'Date_Timestamp':self.date, 'UNIX_Timestamp(s)':self.timestamp, 'Isc':[isc], 'Voc':[voc], 'FF':[ff], 'PCE':[pce], 'MPP voltage': mpp}).round(3)

    def get_timestamp(self):
        self.timestamp = round(time.time())
        self.date = datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def save_dfs_to_files(self):
        path_cell = f'{self.path}/Cell{self.ref}'
        self.create_save_directory(path_cell)
        path_summary = f'{self.path}/Summary'
        self.create_save_directory(path_summary)
        date = self.date.replace(" ", "_")
        date = date.replace(":", "-")
        filename='Cell' + str(self.ref)
        self.df_iv.to_csv(path_cell + '/' + filename + '_IV_' + date +'.txt', index=None, sep='\t')
        self.update_params_file(path_summary, path_cell, filename)

    def update_params_file(self, path_summary, path_cell, filename):
        self.df_full_params = pd.concat([self.df_full_params, self.df_params])
        self.df_full_params.to_csv(path_cell + '/' + filename + '_param.txt', index=None, sep='\t')
        self.df_full_params.to_csv(path_summary + '/' + filename + '_param.txt', index=None, sep='\t')

    def create_save_directory(self, path):
        try:
            os.makedirs(path)
        except FileExistsError:
            pass

class Main():
    def __init__(self, path):
        self.path = path
        self.list_port = self.serial_ports()
        print('go')
        self.cells_package = self.get_cells_package()

    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                if port != 'COM5':
                    result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

    def get_cells_package(self):
        cells_package = {}
        i = 1
        for port in self.list_port:
            cells_package[port] = {'load':Load(port), 'cell':Cell(i), 'data_file':Data_file(self.path, i)}
            i += 1
        return cells_package

    def measure_all_cells(self):
        for port in self.cells_package:
            cell = self.cells_package[port]['cell']
            load = self.cells_package[port]['load']
            data_file = self.cells_package[port]['data_file']
            cell.measure_cell(load, 0.05, 500, 40)
            cell.mpp_tracking(load)
            print(cell.df_iv)
            data_file.save_dfs(cell.df_iv, cell.isc, cell.voc, cell.ff, cell.pce, cell.voltage_mpp)

    def measure_cell(self, port):
        cell = self.cells_package[port]['cell']
        load = self.cells_package[port]['load']
        data_file = self.cells_package[port]['data_file']
        cell.measure_cell(load, 0.05, 500, 40)
        cell.mpp_tracking(load)
        data_file.save_dfs(cell.df_iv, cell.isc, cell.voc, cell.ff, cell.pce, cell.voltage_mpp)

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.main = Main('C:/Users/jules/Documents/test')
        self.worker = []
        self.threadpool = QThreadPool()
        self.gui_cell = {}
        self.init_triggers()
        self.update_gui()

    def init_triggers(self):
        self.comboBox_cell_list.currentTextChanged.connect(self.switch_cell)
        self.pushButton_measure_cell.clicked.connect(self.trigger_measure_one_cell)
        self.pushButton_measure_all.clicked.connect(self.trigger_measure_all_cells)
        self.pushButton_stop.clicked.connect(self.stop_worker)

    def switch_cell(self):
        combo = self.comboBox_cell_list
        cell_nb = combo.currentText()
        if not cell_nb in ['']:
            self.stackedWidget_cells_plot.setCurrentWidget(self.gui_cell[cell_nb].widget_plot)

    def update_gui(self, cell = None):
        comboBox = self.comboBox_cell_list
        if comboBox.currentText() == '':
            comboBox.clear()
            for w in range(0, self.stackedWidget_cells_plot.count(), -1):
                wid = self.stackedWidget_cells_plot.widget(w)
                self.stackedWidget_materials_plot.removeWidget(wid)
                wid.deleteLater()
            for k in self.main.cells_package.keys():
                self.gui_cell[k] = GUI_Cell(self.main.cells_package[k], self.stackedWidget_cells_plot)
                self.gui_cell[k].build_tabs()
                comboBox.addItem(k)
            self.switch_cell()
        else:
            self.gui_cell[cell].tabs.update_all()
            self.switch_cell()

    def measurement(self, cell):
        self.main.measure_cell(cell)
        self.update_gui(cell)

    def trigger_measure_all_cells(self):
        check = True
        for work in self.worker:
            if work.running:
                check = False
                break
        if check:
            self.worker = []
            for cell in self.gui_cell:
                self.trigger_worker(cell)

    def trigger_measure_one_cell(self):
        check = True
        for work in self.worker:
            if work.running:
                check = False
                break
        if check:
            self.worker = []
            cell = self.comboBox_cell_list.currentText()
            self.trigger_worker(cell)

    def cycle_measurement(self, worker_ref, cell, remaining_time):
        loop_bool=self.radioButton_cycle.isChecked()
        cycle = 1
        delay=int(self.lineEdit_delay.text())
        if delay == None:
            delay = 0
        i = 0
        while (i<cycle or loop_bool) and not self.worker[0].checkstop:
            time_s=time.time()
            remaining_time.emit('measuring')
            self.measurement(cell)
            time_f=time.time()
            i=i+1
            if i<cycle or loop_bool:
                self.update_remaining_time(int(time_f-time_s), delay, remaining_time)
        remaining_time.emit('not measuring')
        self.worker[worker_ref].running = False

    def trigger_worker(self, cell):
        i = len(self.worker)
        self.worker.append(Worker(self.cycle_measurement, i, cell))
        if i == 0:
            self.worker[i].kwargs['remaining_time'] = self.worker[i].signals.remaining_time
            self.worker[i].signals.remaining_time.connect(self.show_remaining_time)
        self.threadpool.start(self.worker[i])

    def update_remaining_time(self, time_dif, delay, remaining_time):
        if delay-time_dif<0:
            pass
        else:
            time_remaining=round(delay-time_dif)
            time_f=time.time()-1
            time_d=0
            while time_remaining>0 and not self.worker[0].checkstop:
                hour=math.floor(time_remaining/3600)
                minute=math.floor(((time_remaining/3600)-hour)*60)
                second=round(((((time_remaining/3600)-hour)*60)-minute)*60)
                if hour<10:
                    time_remaining_str='0'+str(hour)
                else:
                    time_remaining_str=str(hour)
                if minute<10:
                    time_remaining_str=time_remaining_str+':0'+str(minute)
                else:
                    time_remaining_str=time_remaining_str+':'+str(minute)
                if second<10:
                    time_remaining_str=time_remaining_str+':0'+str(second)
                else:
                    time_remaining_str=time_remaining_str+':'+str(second)
                remaining_time.emit(time_remaining_str)
                time_s=time_f
                time_f=time.time()
                time_d=time_f-(1-time_d)-time_s
                if time_d>1:
                    time_d=1
                time.sleep(1-time_d)
                time_remaining=time_remaining-1

    def show_remaining_time(self, time_remaining_str):
        if time_remaining_str == 'measuring':
            self.label_remaining_time.setText(f'Measuring...')
        elif time_remaining_str == 'not measuring':
            self.label_remaining_time.setText(f'Not Measuring')
        else:
            self.label_remaining_time.setText(f'Remaining time: {time_remaining_str}')

    def stop_worker(self):
        if self.worker != None:
            for work in self.worker:
                work.checkstop = True
                #work.terminate()

class GUI_Cell():
    def __init__(self, cell_package, stackedWidget_materials_plot):
        self.cell_package = cell_package
        self.stackedWidget_cells_plot = stackedWidget_materials_plot
        self.tabs = {}
        self.init_widget_plot_creation()

    def init_widget_plot_creation(self):
        self.widget_plot = QWidget()
        self.gridLayout_plot = QGridLayout(self.widget_plot)
        self.tabWidget_plot = QTabWidget(self.widget_plot)

        self.gridLayout_plot.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_plot.setStyleSheet(u"font: 18pt \"MS shell Dlg 2\";")
        self.gridLayout_plot.addWidget(self.tabWidget_plot, 0, 0, 1, 1)

        self.stackedWidget_cells_plot.addWidget(self.widget_plot)

    def build_tabs(self):
        self.tabs = GUI_Cell_tabs(self.cell_package, self.tabWidget_plot)
        self.tabs.build_all()

class GUI_Cell_tabs():
    def __init__(self, cell_package, tabWidget_plot):
        self.init_tabs(tabWidget_plot)
        self.cell_package = cell_package

    def init_tabs(self, tabWidget_plot):
        self.tab_stability = QWidget()
        self.tab_iv = QWidget()
        tabWidget_plot.addTab(self.tab_stability, 'Stability')
        tabWidget_plot.addTab(self.tab_iv, 'IV')

    def get_argument_for_refit(self):
        property = 'workfunction'
        method = 'ups'
        karg = {'smoothing_coef': self.settings.spinbox_param_smoothing_1_1.value()}
        return property, method, karg

    def build_all(self):
        self.build_tab_iv()
        self.build_tab_stability()

    def update_all(self):
        self.update_tab_stability()
        self.update_tab_iv()

    def build_tab_stability(self):
        self.Vlayout_plot_stability = QVBoxLayout(self.tab_stability)
        self.gridLayout_plot_stability = QGridLayout()

        self.Vlayout_stability_isc = QVBoxLayout()
        self.Vlayout_stability_voc = QVBoxLayout()
        self.Vlayout_stability_ff = QVBoxLayout()
        self.Vlayout_stability_pce = QVBoxLayout()
        self.fig_stability_isc = MplCanvas(self.tab_stability)
        self.fig_stability_voc = MplCanvas(self.tab_stability)
        self.fig_stability_ff = MplCanvas(self.tab_stability)
        self.fig_stability_pce = MplCanvas(self.tab_stability)
        self.toolbar_fig_stability_isc = NavigationToolbar(self.fig_stability_isc, self.tab_stability)
        self.toolbar_fig_stability_voc = NavigationToolbar(self.fig_stability_voc, self.tab_stability)
        self.toolbar_fig_stability_ff = NavigationToolbar(self.fig_stability_ff, self.tab_stability)
        self.toolbar_fig_stability_pce = NavigationToolbar(self.fig_stability_pce, self.tab_stability)

        self.update_tab_stability()

        self.Vlayout_stability_isc.addWidget(self.toolbar_fig_stability_isc)
        self.Vlayout_stability_isc.addWidget(self.fig_stability_isc)
        self.Vlayout_stability_voc.addWidget(self.toolbar_fig_stability_voc)
        self.Vlayout_stability_voc.addWidget(self.fig_stability_voc)
        self.Vlayout_stability_ff.addWidget(self.toolbar_fig_stability_ff)
        self.Vlayout_stability_ff.addWidget(self.fig_stability_ff)
        self.Vlayout_stability_pce.addWidget(self.toolbar_fig_stability_pce)
        self.Vlayout_stability_pce.addWidget(self.fig_stability_pce)
        self.gridLayout_plot_stability.addLayout(self.Vlayout_stability_isc, 0, 0)
        self.gridLayout_plot_stability.addLayout(self.Vlayout_stability_voc, 0, 1)
        self.gridLayout_plot_stability.addLayout(self.Vlayout_stability_ff, 1, 0)
        self.gridLayout_plot_stability.addLayout(self.Vlayout_stability_pce, 1, 1)
        self.Vlayout_plot_stability.addLayout(self.gridLayout_plot_stability)

    def update_tab_stability(self):
        for param in ['isc', 'voc', 'ff', 'pce']:
            fig = getattr(self, f'fig_stability_{param}')
            fig.axes.cla()
            if param == 'isc':
                ylabel = 'Isc (A)'
                df_full_params_column = 'Isc'
            if param == 'voc':
                ylabel = 'Voc (V)'
                df_full_params_column = 'Voc'
            if param == 'ff':
                ylabel = 'Fill Factor'
                df_full_params_column = 'FF'
            if param == 'pce':
                ylabel = 'PCE'
                df_full_params_column = 'PCE'
            fig.axes.set_ylabel(ylabel, fontsize=20)
            fig.axes.set_xlabel('Time', fontsize=20)
            fig.axes.xaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.yaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.tick_params(which='both', top=True, right=True, width=2)
            fig.axes.tick_params(which='both', direction="in")
            fig.axes.tick_params(which='major', length=5, labelsize=16)
            fig.axes.tick_params(which='minor', length=3)
            fig.draw_idle()
            if not self.cell_package['data_file'].df_full_params.empty:
                fig.axes.plot_date(pd.to_datetime(self.cell_package['data_file'].df_full_params['Date_Timestamp']), self.cell_package['data_file'].df_full_params[df_full_params_column], xdate = True, linestyle ='-', linewidth=2)

    def build_tab_iv(self):
        self.Vlayout_plot_iv = QVBoxLayout(self.tab_iv)
        self.Vlayout_fig_iv = QVBoxLayout()
        self.fig_iv = MplCanvas(self.tab_iv)

        self.update_tab_iv()

        self.Vlayout_fig_iv.addWidget(self.fig_iv)
        self.Vlayout_plot_iv.addLayout(self.Vlayout_fig_iv)

    def update_tab_iv(self):
        for fig in [self.fig_iv]:
            fig.axes.cla()
            fig.axes.set_ylabel('Current (A)', fontsize=20)
            fig.axes.set_xlabel('Voltage (V)', fontsize=20)
            fig.axes.xaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.yaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.tick_params(which='both', top=True, right=True, width=2)
            fig.axes.tick_params(which='both', direction="in")
            fig.axes.tick_params(which='major', length=5, labelsize=16)
            fig.axes.tick_params(which='minor', length=3)
            fig.draw_idle()
        if not self.cell_package['data_file'].df_iv.empty:
            self.fig_iv.axes.plot(self.cell_package['data_file'].df_iv['Voltage (V)'], self.cell_package['data_file'].df_iv['Current (A)'], linewidth=2)

    def deleteLayout(self, cur_lay):
        if cur_lay is not None:
            while cur_lay.count():
                item = cur_lay.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(cur_lay)

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.checkstop=False
        self.running=True
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)

class WorkerSignals(QObject):
    remaining_time = pyqtSignal(str)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QStackedWidget()
    gui=GUI()
    w.addWidget(gui)
    w.resize(2000,1200)
    w.setWindowTitle('Stability')
    w.show()
    try:
        sys.exit(app.exec_())
    except:
        gui.stop_worker()
        print('Stopped')


# -------------------Load test---------------------------------

    # print('---------------------------Load test------------------------')

    # load1 = Load(1)
    # load1.com = 'COM5'
    # load1.link_com()

    # print(load1.load_number)
    # print(load1.com)

    # load1.open_com()
    # print('is serial com open? ' + str(load1.serial.is_open))

    # load1.close_com()
    # print('is serial com open? ' + str(load1.serial.is_open))

    # print('---------------------------Load test end------------------------')

# -------------------Electrical Test ---------------------------------