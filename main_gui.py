import ElectricalMeasurements as em
import pandas as pd
import time
import math
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_form import Ui_MainWindow
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator
matplotlib.use('QT5Agg')


# Class that defines the main GUI window and all its methods to interact with the user
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main = em.Main('C:/Users/jules/Documents/test')
        self.worker = []
        self.worker_sensor = None
        self.threadpool = QThreadPool()
        self.gui_cell = {}
        self.init_triggers()
        self.update_gui()

    # Define all the triggers and link them to an action in the back end
    def init_triggers(self):
        self.ui.DashboardButton.clicked.connect(self.switch_menu)
        self.ui.JVCurvesButton.clicked.connect(self.switch_menu)
        self.ui.HistoricalDataButton.clicked.connect(self.switch_menu)
        self.ui.SettingsButton.clicked.connect(self.switch_menu)
        self.ui.StartMeasurementsButton.clicked.connect(self.trigger_measure_all_cells)
        self.ui.PauseMeasurementsButton.clicked.connect(self.stop_worker)
        self.ui.comboBox_cell_list.currentTextChanged.connect(self.switch_cell)

    # Function that evaluates the sender object to decide which button was clicked and sets the stack widget
    # for the main menu accordingly
    def switch_menu(self):
        if self.sender().objectName() == 'DashboardButton':
            self.ui.stackedWidget.setCurrentIndex(3)
        if self.sender().objectName() == 'JVCurvesButton':
            self.ui.stackedWidget.setCurrentIndex(0)
        if self.sender().objectName() == 'HistoricalDataButton':
            self.ui.stackedWidget.setCurrentIndex(1)
        if self.sender().objectName() == 'SettingsButton':
            self.ui.stackedWidget.setCurrentIndex(2)

    # Switch cell GUI subroutine that plots the selected cell data
    def switch_cell(self):
        combo = self.ui.comboBox_cell_list
        cell_nb = combo.currentText()
        if not cell_nb in ['']:
            self.ui.stackedWidget_cells_plot.setCurrentWidget(self.gui_cell[cell_nb].widget_plot)


    def update_gui(self, cell = None):
        comboBox = self.ui.comboBox_cell_list
        if comboBox.currentText() == '':
            comboBox.clear()
            for w in range(0, self.ui.stackedWidget_cells_plot.count(), -1):
                wid = self.ui.stackedWidget_cells_plot.widget(w)
                self.ui.stackedWidget_materials_plot.removeWidget(wid)
                wid.deleteLater()
            self.build_fig_ivs()
            i = 1
            for k in self.main.cells_package.keys():
                if i < 5:
                    fig_iv = self.ui.fig_iv_1
                else:
                    fig_iv = self.ui.fig_iv_2
                self.gui_cell[k] = GUI_Cell(self.main.cells_package[k], self.ui.stackedWidget_cells_plot, fig_iv)
                self.gui_cell[k].build_all()
                comboBox.addItem(k)
            self.build_figs_power()
            self.switch_cell()
        else:
            self.gui_cell[cell].update_all()
            self.update_cell_parameters(cell)
            self.update_dashboard()
            self.update_fig_power()
            self.update_fig_energy()
            self.switch_cell()

    def build_fig_ivs(self):
        self.ui.fig_iv_1 = MplCanvas(self.ui.JVCurvesStack)
        self.ui.fig_iv_2 = MplCanvas(self.ui.JVCurvesStack)
        self.ui.HLayout_iv_plot.addWidget(self.ui.fig_iv_1)
        self.ui.HLayout_iv_plot.addWidget(self.ui.fig_iv_2)
        for fig in [self.ui.fig_iv_1, self.ui.fig_iv_2]:
            fig.axes.cla()
            fig.axes.set_ylabel('Current (A)', fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.set_xlabel('Voltage (V)', fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.xaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.yaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.tick_params(which='both', top=True, right=True, width=2)
            fig.axes.tick_params(which='both', direction="in")
            fig.axes.tick_params(which='major', length=7, labelsize=16)
            fig.axes.tick_params(which='minor', length=5, color='white')


            ticks = fig.axes.get_yticklabels()
            fig.axes.set_yticklabels(ticks, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.set_xticklabels(ticks, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.tick_params(axis='x', colors='white')  # setting up X-axis tick color to red
            fig.axes.tick_params(axis='y', colors='white')  # setting up Y-axis tick color to black
            fig.axes.spines['left'].set_color('white')  # setting up Y-axis tick color to red
            fig.axes.spines['top'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['bottom'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['right'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['bottom'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['right'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['top'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['left'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.set_facecolor('#4b5148')

            fig.draw_idle()

    def build_figs_power(self):
        self.ui.fig_power = MplCanvas(self.ui.tab_power_over_time)
        self.ui.fig_energy = MplCanvas(self.ui.tab_energy_per_day)
        self.ui.toolbar_fig_power = NavigationToolbar(self.ui.fig_power, self.ui.tab_power_over_time)
        self.ui.toolbar_fig_energy = NavigationToolbar(self.ui.fig_energy, self.ui.tab_energy_per_day)
        self.ui.VLayout_power_plot.addWidget(self.ui.toolbar_fig_power)
        self.ui.VLayout_power_plot.addWidget(self.ui.fig_power)
        self.ui.VLayout_energy_per_day.addWidget(self.ui.toolbar_fig_energy)
        self.ui.VLayout_energy_per_day.addWidget(self.ui.fig_energy)
        for fig in [self.ui.fig_power, self.ui.fig_energy]:
            fig.axes.cla()
            if fig == self.ui.fig_power:
                y_axis = 'Power (W)'
            else:
                y_axis = 'Energy (kWh)'
            fig.axes.set_ylabel(y_axis, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.set_xlabel('Time', fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.xaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.yaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.tick_params(which='both', top=True, right=True, width=2)
            fig.axes.tick_params(which='both', direction="in")
            fig.axes.tick_params(which='major', length=5, labelsize=16)
            fig.axes.tick_params(which='minor', length=3, color='white')

            ticks = fig.axes.get_yticklabels()
            fig.axes.set_yticklabels(ticks, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.set_xticklabels(ticks, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.tick_params(axis='x', colors='white')  # setting up X-axis tick color to red
            fig.axes.tick_params(axis='y', colors='white')  # setting up Y-axis tick color to black
            fig.axes.spines['left'].set_color('white')  # setting up Y-axis tick color to red
            fig.axes.spines['top'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['bottom'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['right'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['bottom'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['right'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['top'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['left'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.set_facecolor('#4b5148')

            fig.draw_idle()
        self.ui.line_power, = self.ui.fig_power.axes.plot(pd.to_datetime(1), 1, linewidth=2)
        self.ui.line_energy, = self.ui.fig_energy.axes.plot(pd.to_datetime(1), 1, linewidth=2)
        self.update_fig_power()
        self.update_fig_energy()

    def update_fig_power(self):
        df_power = pd.DataFrame()
        for k in self.main.cells_package.keys():
            if not self.main.cells_package[k]['data_file'].df_full_params.empty:
                if df_power.empty:
                    df_power['UNIX_Timestamp(s)'] = self.main.cells_package[k]['data_file'].df_full_params['UNIX_Timestamp(s)']
                    df_power['Date_Timestamp'] = self.main.cells_package[k]['data_file'].df_full_params['Date_Timestamp']
                    df_power['Power'] = self.main.cells_package[k]['data_file'].df_full_params['Power']
                else:
                    df_instance = pd.merge(df_power, self.main.cells_package[k]['data_file'].df_full_params[['UNIX_Timestamp(s)', 'Date_Timestamp', 'Power']], on='UNIX_Timestamp(s)', how='inner')
                    df_power['UNIX_Timestamp(s)'] = df_instance['UNIX_Timestamp(s)']
                    df_power['Date_Timestamp'] = df_instance['Date_Timestamp_x']
                    df_power['Power'] = df_instance['Power_x'] + df_instance['Power_y']
        self.ui.line_power.set_ydata(df_power['Power'])
        self.ui.line_power.set_xdata(pd.to_datetime(df_power['Date_Timestamp']))
        self.ui.fig_power.axes.relim()
        self.ui.fig_power.axes.autoscale()
        self.ui.fig_power.fig.canvas.draw()
        self.ui.fig_power.fig.canvas.flush_events()

    def update_fig_energy(self):
        df_energy = self.main.get_daily_power_df()
        if not df_energy.empty:
            self.ui.line_energy.set_ydata(df_energy['Energy (kWh)'])
            self.ui.line_energy.set_xdata(pd.to_datetime(df_energy['Date_Timestamp']))
            self.ui.fig_energy.axes.relim()
            self.ui.fig_energy.axes.autoscale()
            self.ui.fig_energy.fig.canvas.draw()
            self.ui.fig_energy.fig.canvas.flush_events()

    def measurement(self, cell):
        self.main.measure_cell(cell)
        self.update_gui(cell)

    def update_cell_parameters(self, cell):
        if cell != None:
            index = list(self.gui_cell).index(cell)
            getattr(self.ui, f'JscStr{index+1}').setText(f'{round(self.main.cells_package[cell]["cell"].isc, 3)}')
            getattr(self.ui, f'VocStr{index+1}').setText(f'{round(self.main.cells_package[cell]["cell"].voc, 3)}')
            getattr(self.ui, f'FFStr{index+1}').setText(f'{round(self.main.cells_package[cell]["cell"].ff*100, 1)}')
            getattr(self.ui, f'PCEStr{index+1}').setText(f'{round(self.main.cells_package[cell]["cell"].pce*100, 1)}')

    def update_dashboard(self):
        power = self.main.get_current_power()
        self.ui.CurrentPowerLabel.setText(f'{power} W')
        self.ui.SunPowerLabel.setText(f'{(self.main.arduino_sensor.light_intensity_east + self.main.arduino_sensor.light_intensity_west) / 2}')
        self.ui.TodayEnergyLabel.setText(f'{self.main.get_daily_power_df()["Energy (kWh)"].iloc[-1]} kWh')
        self.ui.SunPowerLabel.setStyleSheet(u"color: rgb(254, 249, 193);\n background: transparent;")

    def trigger_measure_all_cells(self):
        check = True
        for work in self.worker:
            if work.running:
                check = False
                break
        if check:
            self.ui.stackedWidget_MeasurementTriggers.setCurrentIndex(1)
            self.worker = []
            for cell in self.gui_cell:
                self.trigger_worker(cell)
            self.trigger_worker_sensor()

    def trigger_measure_one_cell(self):
        check = True
        for work in self.worker:
            if work.running:
                check = False
                break
        if check:
            self.worker = []
            cell = self.ui.comboBox_cell_list.currentText()
            self.trigger_worker(cell)

    def cycle_measurement(self, worker_ref, cell, remaining_time = None):
        loop_bool=True
        cycle = 1
        delay=int(self.ui.TimeBetweenJV.value()*60)
        if delay == None:
            delay = 0
        i = 0
        while (i<cycle or loop_bool) and not self.worker[0].checkstop:
            time_s=time.time()
            if remaining_time != None:
                remaining_time.emit('measuring')
            self.measurement(cell)
            time_f=time.time()
            i=i+1
            if i<cycle or loop_bool:
                if remaining_time != None:
                    if len(self.worker) == 1:
                        self.main.update_today_power()
                    self.update_remaining_time(int(time_f-time_s), delay, remaining_time)
                else:
                    if worker_ref == len(self.worker)-1:
                        self.main.update_today_power()
                    time.sleep(1)
                    while (self.ui.NextMeasurementTimeIntervalLabel.text() != 'Measuring...') and not self.worker[0].checkstop:
                        time.sleep(0.1)
        if remaining_time != None:
            remaining_time.emit('not measuring')
        self.worker[worker_ref].running = False

    def cycle_measurement_sensor(self):
        while not self.worker[0].checkstop:
            self.main.arduino_sensor.get_readings()
            while self.ui.NextMeasurementTimeIntervalLabel.text() == 'Measuring...' and not self.worker[0].checkstop:
                time.sleep(0.1)
            while self.ui.NextMeasurementTimeIntervalLabel.text() != 'Measuring...' and not self.worker[0].checkstop:
                time.sleep(0.1)
        self.worker_sensor.running = False

    def trigger_worker(self, cell):
        i = len(self.worker)
        self.worker.append(Worker(self.cycle_measurement, i, cell))
        if i == 0:
            self.worker[i].kwargs['remaining_time'] = self.worker[i].signals.remaining_time
            self.worker[i].signals.remaining_time.connect(self.show_remaining_time)
        self.threadpool.start(self.worker[i])

    def trigger_worker_sensor(self):
        self.worker_sensor = Worker(self.cycle_measurement_sensor)
        self.threadpool.start(self.worker_sensor)

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
            self.ui.NextMeasurementTimeIntervalLabel.setText(f'Measuring...')
        elif time_remaining_str == 'not measuring':
            self.ui.NextMeasurementTimeIntervalLabel.setText(f'Not Measuring')
            self.ui.stackedWidget_MeasurementTriggers.setCurrentIndex(0)
        else:
            self.ui.NextMeasurementTimeIntervalLabel.setText(f'{time_remaining_str}')

    def stop_worker(self):
        if self.worker != None:
            for work in self.worker:
                work.checkstop = True


class GUI_Cell():
    def __init__(self, cell_package, stackedWidget_cells_plot, fig_iv):
        self.cell_package = cell_package
        self.stackedWidget_cells_plot = stackedWidget_cells_plot
        self.fig_iv = fig_iv
        self.tabs = {}
        self.init_widget_plot_creation()

    def init_widget_plot_creation(self):
        self.widget_plot = QWidget()
        self.Vlayout_plot_stability = QVBoxLayout(self.widget_plot)

        self.stackedWidget_cells_plot.addWidget(self.widget_plot)

    def build_all(self):
        self.build_tab_stability()
        self.build_tab_iv()

    def update_all(self):
        self.update_tab_stability()
        self.update_tab_iv()

    def build_tab_stability(self):
        self.gridLayout_plot_stability = QGridLayout()

        self.Vlayout_stability_isc = QVBoxLayout()
        self.Vlayout_stability_voc = QVBoxLayout()
        self.Vlayout_stability_ff = QVBoxLayout()
        self.Vlayout_stability_pce = QVBoxLayout()
        self.fig_stability_isc = MplCanvas(self.widget_plot)
        self.fig_stability_voc = MplCanvas(self.widget_plot)
        self.fig_stability_ff = MplCanvas(self.widget_plot)
        self.fig_stability_pce = MplCanvas(self.widget_plot)
        self.toolbar_fig_stability_isc = NavigationToolbar(self.fig_stability_isc, self.widget_plot)
        self.toolbar_fig_stability_voc = NavigationToolbar(self.fig_stability_voc, self.widget_plot)
        self.toolbar_fig_stability_ff = NavigationToolbar(self.fig_stability_ff, self.widget_plot)
        self.toolbar_fig_stability_pce = NavigationToolbar(self.fig_stability_pce, self.widget_plot)

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
            fig.axes.set_ylabel(ylabel, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.set_xlabel('Time', fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.xaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.yaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.tick_params(which='both', top=True, right=True, width=2)
            fig.axes.tick_params(which='both', direction="in")
            fig.axes.tick_params(which='major', length=5, labelsize=16)
            fig.axes.tick_params(which='minor', length=3,  color='white')

            ticks = fig.axes.get_yticklabels()
            fig.axes.set_yticklabels(ticks, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.set_xticklabels(ticks, fontsize=20, fontname="Bahnschrift", color='white')
            fig.axes.tick_params(axis='x', colors='white')  # setting up X-axis tick color to red
            fig.axes.tick_params(axis='y', colors='white')  # setting up Y-axis tick color to black
            fig.axes.spines['left'].set_color('white')  # setting up Y-axis tick color to red
            fig.axes.spines['top'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['bottom'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['right'].set_color('white')  # setting up above X-axis tick color to red
            fig.axes.spines['bottom'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['right'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['top'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.spines['left'].set_linewidth(3)  # setting up above X-axis tick color to red
            fig.axes.set_facecolor('#4b5148')

            fig.draw_idle()
            if not self.cell_package['data_file'].df_full_params.empty:
                fig.axes.plot_date(pd.to_datetime(self.cell_package['data_file'].df_full_params['Date_Timestamp']), self.cell_package['data_file'].df_full_params[df_full_params_column], xdate = True, linestyle ='-', linewidth=2)

    def build_tab_iv(self):
        if not self.cell_package['data_file'].df_iv.empty:
            x = self.cell_package['data_file'].df_iv['Voltage (V)']
            y = self.cell_package['data_file'].df_iv['Current (A)']
        else:
            x = 1
            y = 1
        self.line, = self.fig_iv.axes.plot(x, y, linewidth=2)
        self.update_tab_iv()

    def update_tab_iv(self):
        if not self.cell_package['data_file'].df_iv.empty:
            self.line.set_ydata(self.cell_package['data_file'].df_iv['Current (A)'])
            self.line.set_xdata(self.cell_package['data_file'].df_iv['Voltage (V)'])
            self.fig_iv.axes.relim()
            self.fig_iv.axes.autoscale()
            self.fig_iv.fig.canvas.draw()
            self.fig_iv.fig.canvas.flush_events()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.fig = Figure(facecolor='#4b5148', tight_layout=True)
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

    def run(self):
        self.fn(*self.args, **self.kwargs)

class WorkerSignals(QObject):
    remaining_time = Signal(str)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    w=QStackedWidget()
    gui=GUI()
    w.addWidget(gui)
    w.resize(2000,1200)
    w.setWindowTitle('Stability')
    w.show()
    try:
        sys.exit(app.exec())
    except:
        gui.stop_worker()
        print('Stopped')