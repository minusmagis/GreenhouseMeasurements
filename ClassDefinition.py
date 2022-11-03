import serial
import time
import datetime
import os
import sys
import glob
import pandas as pd
import numpy as np
import math


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
        time.sleep(0.5)
        self.close_door()

    # Create a logarithmic numspace within two limit resistance values. Measure voltage and current for each of
    # the resistance values and return it as two lists, in the shape of an IV Curve.
    def sweep_measurement(self, res_min, res_max, resistance_nb_step):
        voltage_list = []
        current_list = []
        
        self.list_resistance = np.logspace(math.log10(res_min), math.log10(res_max), num=resistance_nb_step, base=10)
        print(self.list_resistance)
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
        oload.send_resistance_to_load(oload.list_resistance[self.idx_mpp])


# Classes should be CamelCased? i propose to change to DataFile :D------------------------------------------------------------------------------- Read this :D
class Data_file():
    def __init__(self):
        self.timestamp = None
        self.date = None
        self.df_iv = None
        self.df_params = None

    # Get all the relevant parameters and save them to the specified path
    def save_dfs(self, df_iv, isc, voc, ff, pce, mpp, path, ref):
        self.get_data(df_iv, isc, voc, ff, pce, mpp)
        self.save_dfs_to_files(path, ref)

    # Round the numbers to 3 decimal places and add a timestamp to the data before formatting it all to fit into the df
    def get_data(self, df_iv, isc, voc, ff, pce, mpp):
        self.df_iv = df_iv.round(3)
        self.get_timestamp()
        self.df_params = pd.DataFrame({'Date_Timestamp':self.date, 'UNIX_Timestamp(s)':self.timestamp, 'Isc':[isc], 'Voc':[voc], 'FF':[ff], 'PCE':[pce], 'MPP voltage': mpp}).round(3)

    # Format the timestamp into something that makes sense (most likely I will add kronos to this :3
    def get_timestamp(self):
        self.timestamp = round(time.time())
        self.date = datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Create paths for the cell and the summary with the correct formatting, convert the iv to a csv.
    # If the file already exists, update the parameters and if not create the cell and summary files
    def save_dfs_to_files(self, path, ref):
        path_cell = f'{path}/Cell{ref}'
        self.create_save_directory(path_cell)
        path_summary = f'{path}/Summary'
        self.create_save_directory(path_summary)
        date = self.date.replace(" ", "_")
        date = date.replace(":", "-")
        filename='Cell' + str(ref)
        self.df_iv.to_csv(path_cell + '/' + filename + '_IV_' + date +'.txt', index=None, sep='\t')
        if os.path.isfile(path_cell + '/' + filename + '_param.txt'):
            self.update_params_file(path_summary, path_cell, filename)
        else:
            self.df_params.to_csv(path_cell + '/' + filename + '_param.txt',index=None, sep='\t')
            self.df_params.to_csv(path_summary + '/' + filename + '_param.txt',index=None, sep='\t')

    # Concatenate the files in case the file already exists to prevent data loss or duplication
    def update_params_file(self, path_summary, path_cell, filename):
        df_open = pd.read_csv(path_cell + '/' + filename + '_param.txt', delimiter = "\t")
        df = pd.concat([df_open, self.df_params])
        df.to_csv(path_cell + '/' + filename + '_param.txt',index=None, sep='\t')
        df.to_csv(path_summary + '/' + filename + '_param.txt',index=None, sep='\t')

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
        self.load_dict = self.get_load_dict()

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
    def get_load_dict(self):
        load_dict = {}
        i = 1
        for port in self.list_port:
            load_dict[port] = {'load':Load(port), 'cell':Cell(i), 'data_file':Data_file()}
            i += 1
        return load_dict

    # Measure the cells and save the processed data. Leave the cells at mppt resistance afterwards.
    def measure_cells(self):
        for port in self.load_dict:
            cell = self.load_dict[port]['cell']
            load = self.load_dict[port]['load']
            data_file = self.load_dict[port]['data_file']
            cell.measure_cell(load, 0.05, 150, 20)
            cell.mpp_tracking(load)
            print(self.load_dict[port]['cell'].df_iv)
            data_file.save_dfs(cell.df_iv, cell.isc, cell.voc, cell.ff, cell.pce, cell.voltage_mpp, self.path, cell.ref)



if __name__ == '__main__':
    f = Main('C:/Users/jules/Documents/test')
    f.measure_cells()

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