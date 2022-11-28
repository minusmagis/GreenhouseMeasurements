import serial
import time
import datetime
import os
import sys
import glob
import pandas as pd
import numpy as np
import math
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# from PySide6 import shiboken
from ui_form import Ui_MainWindow
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator
matplotlib.use('QT5Agg')


# Class that holds the serial information for each load and handles coms channel opening and closing
class classHardware_():
    def __init__(self, port):
        self.port = port
        self.status = "close"
        self.door = self.assign_port()

    # Try to open serial coms with the given port and raise an exception if not possible. If possible
    # return the serial object
    def assign_port(self):
        try:
            door = serial.Serial(self.port, 115200, timeout=5)
            door.close()
            return door
        except serial.serialutil.SerialException:
            Warning("No COM port defined for load" + str(self.port))
            return None

    # Open serial communication with the serial object and change status flag accordingly
    def open_door(self):
        if self.status == "close":
            self.door.open()
            self.status = "open"

    # Close serial communication with the serial object and change status flag accordingly
    def close_door(self):
        if self.status == "open":
            self.door.close()
            self.status = "close"


# Load Class that takes care of the command sending and data receiving from the KORAD Load,
# which inherits the classHardware properties.
class Load(classHardware_):
    def __init__(self, port):
        super().__init__(port)
        self.list_resistance = None
        self.mpp_resistance = 10

    # Read the current and the voltage from the load and return it as a list
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

    # Set the resistance on the load and wait a prudential time so that it is correctly set.
    def send_resistance_to_load(self, res):
        self.open_door()
        set_res_str = f':RES {res}OHM\n'
        self.door.write(set_res_str.encode('utf-8'))
        set_input_str = f':INPut ON\n'
        self.door.write(set_input_str.encode('utf-8'))
        time.sleep(0.5)
        self.close_door()

    # Create a resistance list that has a higher concentration of points in the center than on the edges
    def custom_resistance_list(self, min, max, point_number):

        resistance_list_top = list()
        resistance_list_bot = list()
        half_point_number = int(point_number / 2)

        scale_factor_top = (max - self.mpp_resistance) ** (2 / point_number)
        scale_factor_bot = (self.mpp_resistance - min) ** (2 / point_number)

        for i in range(half_point_number):
            resistance_list_top.append(self.mpp_resistance - 1 + scale_factor_top ** i)

        resistance_list_top.append(max)
        resistance_list_top.pop(0)

        for i in range(half_point_number):
            resistance_list_bot.append(self.mpp_resistance + 1 - scale_factor_bot ** i)

        resistance_list_bot.append(min)
        resistance_list_bot.reverse()

        # print(resistance_list_top)
        # print(resistance_list_bot)

        resistance_list = resistance_list_bot + resistance_list_top

        # print(resistance_list)

        return resistance_list


    # Create a logarithmic numspace within two limit resistance values. Measure voltage and current for each of
    # the resistance values and return it as two lists, in the shape of an IV Curve.
    def sweep_measurement(self, res_min, res_max, resistance_nb_step):
        voltage_list = []
        current_list = []
        self.list_resistance = self.custom_resistance_list(res_min, res_max, resistance_nb_step)
        #self.list_resistance = np.logspace(math.log10(res_max), math.log10(res_min), num=resistance_nb_step, base=10)
        for res in self.list_resistance:
            self.send_resistance_to_load(res)
            result = self.receive_result()
            current_list.append(result[0])
            voltage_list.append(result[1])
        return voltage_list, current_list


# Cell class to transform and store all the relevant figures of merit of each cell--------------------------------------------- What is the use of ref?
class Cell():
    def __init__(self, ref):
        self.ref = ref
        self.isc = None
        self.voc = None
        self.ff = None
        self.pce = None
        self.power = None
        self.voltage_mpp = None
        self.idx_mpp = None
        self.df_iv = pd.DataFrame()

    # Take the load object instance, the max and min resistance values and the resistance step and perform an IV curve
    # and extract the relevant figures of merit from the result.
    def measure_cell(self, oload, res_min, res_max, resistance_nb_step):
        self.get_df_iv(oload, res_min, res_max, resistance_nb_step)
        self.get_cell_parameters()

    # Take the load object instance, with the resistance sweep values and perform a sweep measurement. Convert the
    # resulting lists into a dataframe and store it in df_iv.
    def get_df_iv(self, oload, res_min, res_max, resistance_nb_step):
        voltage_list = []
        current_list = []
        voltage_list, current_list = oload.sweep_measurement(res_min, res_max, resistance_nb_step)
        self.df_iv = pd.DataFrame(list(zip(voltage_list, current_list)), columns=['Voltage (V)', 'Current (A)'])

    # Calculate cell parameters from dataframe
    def get_cell_parameters(self):
        self.get_isc()
        self.get_voc()
        self.get_fill_factor()
        self.get_pce()

    # Get the point of lowest resistance that corresponds to Isc and the first in the current array.
    def get_isc(self):
        self.isc = self.df_iv['Current (A)'][self.df_iv.index[0]]

    # Get the point of highest resistance that corresponds to Voc and the last in the voltage array.
    def get_voc(self):
        self.voc = self.df_iv['Voltage (V)'][self.df_iv.index[-1]]

    # Calculate the fill factor by finding Vmpp and Impp and dividing it by Voc * Isc
    def get_fill_factor(self):
        self.df_iv['Power (W)'] = self.df_iv['Voltage (V)'] * self.df_iv['Current (A)']
        self.idx_mpp = self.df_iv['Power (W)'].idxmax()
        self.voltage_mpp = self.df_iv['Voltage (V)'][self.idx_mpp]
        self.power = self.df_iv['Power (W)'][self.idx_mpp]
        impp = self.df_iv['Current (A)'][self.idx_mpp]
        if self.isc * self.voc != 0:
            self.ff = (impp * self.voltage_mpp) / (self.isc * self.voc)
        else:
            self.ff = 0

    # Calculate PCE in the wrong way by accepting that irradiance is 1 even at night :3
    def get_pce(self):
        self.pce = self.isc * self.voc * self.ff

    # Set the resistance of the load to the mpp equivalent resistance
    def mpp_tracking(self, oload):
        oload.mpp_resistance = oload.list_resistance[self.idx_mpp]
        oload.send_resistance_to_load(oload.mpp_resistance)
        


# Classes should be CamelCased? i propose to change to DataFile :D------------------------------------------------------------------------------- Read this :D
# Data File class to store all the timestamps, the calculated parameters and the IV curves.
class Data_file():
    def __init__(self, path, ref):
        self.path = path
        self.ref = ref
        self.timestamp = None
        self.date = None
        self.df_params = None
        self.df_iv = self.get_last_iv()
        self.df_full_params = self.get_df_full_params()

    # Read the summary dataframe from the project path. If it does not exist create an emtpy dataframe
    def get_df_full_params(self):
        path_summary = f'{self.path}/Summary'
        filename = f'Cell{self.ref}_param.txt'
        if os.path.exists(path_summary) and os.path.exists(path_summary + '/' + filename):
            return pd.read_csv(path_summary + '/' + filename, delimiter = "\t")
        else:
            return pd.DataFrame()

    # Get the last IV curve dataframe from the cell folder, and if it does not exist create an empty dataframe
    def get_last_iv(self):
        path_cell = f'{self.path}/Cell{self.ref}'
        if os.path.exists(path_cell):
            file = [f for f in os.listdir(path_cell) if os.path.isfile(os.path.join(path_cell, f))][-2]
            return pd.read_csv(path_cell + '/' + file, delimiter = "\t")
        else:
            return pd.DataFrame()

    # Get all the relevant parameters and save them to the specified path
    def save_dfs(self, df_iv, isc, voc, ff, pce, mpp, mpp_power):
        self.get_data(df_iv, isc, voc, ff, pce, mpp, mpp_power)
        self.save_dfs_to_files()

    # Round the numbers to 3 decimal places and add a timestamp to the data before formatting it all to fit into the df
    def get_data(self, df_iv, isc, voc, ff, pce, mpp, mpp_power):
        self.df_iv = df_iv.round(3)
        self.get_timestamp()
        self.df_params = pd.DataFrame({'Date_Timestamp':self.date, 'UNIX_Timestamp(s)':self.timestamp, 'Isc':[isc], 'Voc':[voc], 'FF':[ff], 'PCE':[pce], 'MPP voltage': mpp, 'Power': mpp_power}).round(3)

    # Format the timestamp into something that makes sense (most likely I will add kronos to this :3
    def get_timestamp(self):
        self.timestamp = round(time.time())
        self.date = datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Create paths for the cell and the summary with the correct formatting, convert the iv to a csv.
    # If the file already exists, update the parameters and if not create the cell and summary files
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

    # Concatenate the files in case the file already exists to prevent data loss or duplication
    def update_params_file(self, path_summary, path_cell, filename):
        self.df_full_params = pd.concat([self.df_full_params, self.df_params])
        self.df_full_params.to_csv(path_cell + '/' + filename + '_param.txt', index=None, sep='\t')
        self.df_full_params.to_csv(path_summary + '/' + filename + '_param.txt', index=None, sep='\t')

    # Create save directory
    def create_save_directory(self, path):
        try:
            os.makedirs(path)
        except FileExistsError:
            pass


# Main class that takes care of connecting to the load, making the measurement and data processing
# and saving the data in the specified path
class Main():
    def __init__(self, path):
        self.path = path
        self.list_port = self.serial_ports()
        print('go')
        self.cells_package = self.get_cells_package()

    # Serial port lister that returns a list of ports or an error when in an unsupported platform
    def serial_ports(self):

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

    # Create a dictionary that links the oload with the oCell and the oData_file
    def get_cells_package(self):
        cells_package = {}
        i = 1
        for port in self.list_port:
            cells_package[port] = {'load':Load(port), 'cell':Cell(i), 'data_file':Data_file(self.path, i)}
            i += 1
        return cells_package

    # Measure the cells and save the processed data. Leave the cells at mppt resistance afterwards.
    def measure_all_cells(self):
        for port in self.cells_package:
            cell = self.cells_package[port]['cell']
            load = self.cells_package[port]['load']
            data_file = self.cells_package[port]['data_file']
            cell.measure_cell(load, 0.05, 500, 40)
            cell.mpp_tracking(load)
            data_file.save_dfs(cell.df_iv, cell.isc, cell.voc, cell.ff, cell.pce, cell.voltage_mpp, cell.power)


    # Same as measure_all_cells but for a single cell
    def measure_cell(self, port):
        cell = self.cells_package[port]['cell']
        load = self.cells_package[port]['load']
        data_file = self.cells_package[port]['data_file']
        cell.measure_cell(load, 0.05, 500, 40)
        cell.mpp_tracking(load)
        data_file.save_dfs(cell.df_iv, cell.isc, cell.voc, cell.ff, cell.pce, cell.voltage_mpp, cell.power)

    # Measure the total power for all the strings
    def get_power(self):
        power = 0
        for port in self.cells_package:
            power += round(self.cells_package[port]['cell'].power, 1)
        return power


# Class that defines the main GUI window and all its methods to interact with the user
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main = Main('C:/Users/jules/Documents/test')
        self.worker = []
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
            self.build_fig_power()
            self.switch_cell()
        else:
            self.gui_cell[cell].update_all()
            self.update_cell_parameters(cell)
            self.update_dashboard()
            self.update_fig_power()
            self.switch_cell()

    def build_fig_ivs(self):
        self.ui.fig_iv_1 = MplCanvas(self.ui.JVCurvesStack)
        self.ui.fig_iv_2 = MplCanvas(self.ui.JVCurvesStack)
        self.ui.HLayout_iv_plot.addWidget(self.ui.fig_iv_1)
        self.ui.HLayout_iv_plot.addWidget(self.ui.fig_iv_2)
        for fig in [self.ui.fig_iv_1, self.ui.fig_iv_2]:
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

    def build_fig_power(self):
        self.ui.fig_power = MplCanvas(self.ui.tab_power_over_time)
        self.ui.toolbar_fig_power = NavigationToolbar(self.ui.fig_power, self.ui.tab_power_over_time)
        self.ui.VLayout_power_plot.addWidget(self.ui.toolbar_fig_power)
        self.ui.VLayout_power_plot.addWidget(self.ui.fig_power)
        for fig in [self.ui.fig_power]:
            fig.axes.cla()
            fig.axes.set_ylabel('Power (W)', fontsize=20)
            fig.axes.set_xlabel('Time', fontsize=20)
            fig.axes.xaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.yaxis.set_minor_locator(AutoMinorLocator())
            fig.axes.tick_params(which='both', top=True, right=True, width=2)
            fig.axes.tick_params(which='both', direction="in")
            fig.axes.tick_params(which='major', length=5, labelsize=16)
            fig.axes.tick_params(which='minor', length=3)
            fig.draw_idle()
        self.ui.line_power, = self.ui.fig_power.axes.plot(1, 1, linewidth=2)
        self.update_fig_power()

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
        print(pd.to_datetime(df_power['Date_Timestamp']))
        self.ui.fig_power.axes.relim()
        self.ui.fig_power.axes.autoscale()
        self.ui.fig_power.fig.canvas.draw()
        self.ui.fig_power.fig.canvas.flush_events()
        

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
        power = self.main.get_power()
        self.ui.CurrentPowerLabel.setText(f'{power} W')


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
                    self.update_remaining_time(int(time_f-time_s), delay, remaining_time)
                else:
                    time.sleep(1)
                    while (self.ui.NextMeasurementTimeIntervalLabel.text() != 'Measuring...') and not self.worker[0].checkstop:
                        time.sleep(0.1)
        if remaining_time != None:
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