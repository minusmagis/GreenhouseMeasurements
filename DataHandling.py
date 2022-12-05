import pandas as pd
import os
import time
import datetime
import tkinter as tk
from tkinter import filedialog


# Classes should be CamelCased? i propose to change to DataFile :D------------------------------------------------------------------------------- Read this :D
# Data File class to store all the timestamps, the calculated parameters and the IV curves.
class DataFile():
    def __init__(self, path, ref):
        self.path = path
        self.ref = ref
        self.df_iv = self.get_last_iv()
        self.df_full_params = self.get_df_full_params()
        self.last_day_df = self.get_last_day_data()
        self.day_power = None
        self.timestamp = None
        self.date = None
        self.df_params = None

    def get_last_day_data(self):
        '''
        :param param_summary_file: csv file with a Date_Timestamp timestamp that has the date in 'YYYY-MM-DD HH:MM:SS' format
        :return: pandas dataframe with all the columns that have the same date YYYY-MM-DD as the last row.
        '''

        today, last_meas_time = self.df_full_params['Date_Timestamp'].iloc[-1].split(' ')
        today_data = self.df_full_params[self.df_full_params['Date_Timestamp'].str.contains(today)]

        return today_data

    def day_power_integrate(self):
        '''
        :param today_data: dataframe with the data from just one day
        :return: integrated power (energy) in kWh
        '''

        today_energy = 0
        previous_timestamp = -1
        first_it = True
    #use apply!!
        # Iterate through every row and multiply the power by the time difference to obtain the generated energy
        for index, row in self.last_day_df.iterrows():
            if first_it:
                previous_timestamp = row['UNIX_Timestamp(s)']
                first_it = False
            else:
                time_difference = row['UNIX_Timestamp(s)']-previous_timestamp
                previous_timestamp = row['UNIX_Timestamp(s)']
                today_energy += ( row['Power'] * time_difference / 3600)

        self.day_power = today_energy

    # Read the summary dataframe from the project path. If it does not exist create an emtpy dataframe
    def get_df_full_params(self):
        path_summary = f'{self.path}/Summary'
        filename = f'Cell{self.ref}_param.txt'
        if os.path.exists(path_summary) and os.path.exists(path_summary + '/' + filename):
            return pd.read_csv(path_summary + '/' + filename, delimiter="\t")
        else:
            return pd.DataFrame()

    # Get the last IV curve dataframe from the cell folder, and if it does not exist create an empty dataframe
    def get_last_iv(self):
        path_cell = f'{self.path}/Cell{self.ref}'
        if os.path.exists(path_cell):
            file = [f for f in os.listdir(path_cell) if os.path.isfile(os.path.join(path_cell, f))][-2]
            return pd.read_csv(path_cell + '/' + file, delimiter="\t")
        else:
            return pd.DataFrame()

    # Get all the relevant parameters and save them to the specified path
    def save_dfs(self, df_iv, isc, voc, ff, pce, mpp, mpp_power, temperature, humidity, li_east, li_west):
        self.get_data(df_iv, isc, voc, ff, pce, mpp, mpp_power, temperature, humidity, li_east, li_west)
        self.save_dfs_to_files()

    # Round the numbers to 3 decimal places and add a timestamp to the data before formatting it all to fit into the df
    def get_data(self, df_iv, isc, voc, ff, pce, mpp, mpp_power, temperature, humidity, li_east, li_west):
        self.df_iv = df_iv.round(3)
        self.get_timestamp()
        self.df_params = pd.DataFrame(
            {'Date_Timestamp': self.date, 'UNIX_Timestamp(s)': self.timestamp, 'Isc': [isc], 'Voc': [voc], 'FF': [ff],
             'PCE': [pce], 'MPP voltage': mpp, 'Power': mpp_power, 'Temperature (ºC)': temperature, 'Humidity (%)': humidity, 
             'Light Intensity East (W m-2)': li_east, 'Light Intensity West (W m-2)': li_west}).round(3)

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
        filename = 'Cell' + str(self.ref)
        self.df_iv.to_csv(path_cell + '/' + filename + '_IV_' + date + '.txt', index=None, sep='\t')
        self.update_params_file(path_summary, path_cell, filename)

    # Concatenate the files in case the file already exists to prevent data loss or duplication
    def update_params_file(self, path_summary, path_cell, filename):
        self.df_full_params = pd.concat([self.df_full_params, self.df_params])
        self.df_full_params.to_csv(path_cell + '/' + filename + '_param.txt', index=None, sep='\t')
        self.df_full_params.to_csv(path_summary + '/' + filename + '_param.txt', index=None, sep='\t')
        self.last_day_df = self.get_last_day_data()
        self.day_power_integrate()

    # Create save directory
    def create_save_directory(self, path):
        try:
            os.makedirs(path)
        except FileExistsError:
            pass

def load_SN_to_string_num(serial_number):
    with open("resource/LoadAdresses.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if serial_number in line: return int(line.replace(serial_number, ''))

        Warning('No string number specified for load with SN: '+str(serial_number))
        return None

def string_num_to_load_SN(string_number, serial_number):
    with open("resource/LoadAdresses.txt", 'a', encoding='utf-8') as f:
        new_load = str(serial_number) + '\t' + str(string_number) + '\n'
        f.write(new_load)

        Warning('No string number specified for load with SN: '+str(serial_number))
        return None

if __name__ == '__main__':

    # Create a fileDialog
    root = tk.Tk()
    root.withdraw()
    root_dir = os.getcwd()
    file_path = filedialog.askdirectory(initialdir=root_dir)

    # Create a dummy dataframe
    df = pd.DataFrame([1,2,3],columns=['Column 1'])

    # Create the data file object with reference 1
    data_file = DataFile(file_path,1)

    # Save data in the specified location
    data_file.save_dfs(df, 10, 20, 30,40, 50, 60)