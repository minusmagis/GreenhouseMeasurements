import pandas as pd
import serial
import time

import SmallFunctions as sf
import CommunicationFunctions as CF
import DataHandling as DH


D_ELECTR = True # Flag for debugging this entire script

class Util():
    @staticmethod
    def debugging(message, DFLAG):
        if DFLAG:
            print(message)

class Main():
    def __init__(self, path):
        self.path = path
        self.list_port = CF.serial_ports()
        self.arduino_sensor = Arduino(self.arduino_scan())
        self.cells_package = self.get_cells_package()

    # Scan all serial connections and pop the arduino from the port list to prevent the software to treat it as a load
    def arduino_scan(self):
        for i, port in enumerate(self.list_port):
            sf.debugging('Detecting arduino, Scanning port ' + str(port), D_ELECTR)
            if CF.detect_arduino(port):
                self.list_port.pop(i)
                Util.debugging('Arduino Sensor Detected',D_ELECTR)
                return port

        Util.debugging('Arduino Sensor NOT Detected', D_ELECTR)
        return None

    # Create a dictionary that links the oload with the oCell and the oDataFile
    def get_cells_package(self):
        cells_package = {}
        i = 1
        for port in self.list_port:
            cells_package[port] = {'load':Load(port), 'cell':Cell(i), 'data_file':DH.DataFile(self.path, i)}
            i += 1
        return cells_package

    # Measure the cells and save the processed data. Leave the cells at mppt resistance afterwards.
    def measure_all_cells(self):
        for port in self.cells_package:
            cell = self.cells_package[port]['cell']
            load = self.cells_package[port]['load']
            data_file = self.cells_package[port]['data_file']
            cell.measure_cell(load, 0.05, 500, 200)
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

class classHardware_():
    def __init__(self, port, baudrate = 115200):
        self.port = port
        self.status = "close"
        self.door = self.assign_port(baudrate)

    # Try to open serial coms with the given port and raise an exception if not possible. If possible
    # return the serial object
    def assign_port(self, baudrate):
        try:
            door = serial.Serial(self.port, baudrate, timeout=5)
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

class Arduino(classHardware_):
    def __init__(self, port):
        super().__init__(port, baudrate=9600)
        self.temperature = None
        self.humidity = None
        self.light_intensity_east = None
        self.light_intensity_west = None
        self.sensor_dict = None
        self.delay = 0.2                            # Add a delay for fluid communications

    # Read the desired variables and store them into a list for further processing
    def get_readings(self):

        self.open_door()
        foo = self.door.readline().decode('utf-8').rstrip('A\n')            # Empty the first recognition line
        time.sleep(self.delay)

        time.sleep(self.delay)
        self.door.write(b'T\n')                                            # Write the command to extract temperature
        time.sleep(self.delay)
        print(self.door.readline().decode('utf-8').rstrip().split(':'))
        foo, self.temperature = self.door.readline().decode('utf-8').rstrip().split(':') # Split incoming data to extract value

        time.sleep(self.delay)
        self.door.write(b'H\n')
        time.sleep(self.delay)
        print(self.door.readline().decode('utf-8').rstrip().split(':'))
        foo, self.humidity = self.door.readline().decode('utf-8').rstrip().split(':')

        time.sleep(self.delay)
        self.door.write(b'E\n')
        time.sleep(self.delay)
        foo, self.light_intensity_east = self.door.readline().decode('utf-8').rstrip().split(':')

        time.sleep(self.delay)
        self.door.write(b'W\n')
        time.sleep(self.delay)
        foo, self.light_intensity_west = self.door.readline().decode('utf-8').rstrip().split(':')

        self.close_door()

        # Save all data in a dictionary for further processing and return
        self.sensor_dict = {'Temperature (ºC): ': float(self.temperature), 'Humidity (%):': float(self.humidity),
                       'Light Intensity East (W m-2): ': float(self.light_intensity_east), 'Light Intensity West (W m-2): ': float(self.light_intensity_west)}

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

if __name__ == '__main__':
    measurement1 = Main('test/MartiTest')
    print(measurement1.arduino_sensor.get_readings())
    # # measurement1.measure_all_cells()

    # -------------------Load test---------------------------------



    # -------------------Electrical Test ---------------------------------