from tkinter import filedialog
import os
import pandas as pd
import datetime
import time

# file_with_all_files = filedialog.askopenfilename(initialdir = "/",title = "Select the txt file with the list of files")
folder_with_all_files = filedialog.askdirectory(initialdir = r'P:\Job Documents\Omegalab\Greenhouse\Data\Summary',mustexist = True,title = "Select the directory which you want to check")

# Get folder with all the cells and the summary


cell_file_list = sorted(os.listdir(folder_with_all_files))

for i,file in enumerate(cell_file_list):
    if 'Irr' in file: irr_df = pd.read_csv(os.path.join(folder_with_all_files,file), delimiter="\t")
    if 'Cell' not in file:
        cell_file_list.pop(i)

cell_df_list = list()

for i,file in enumerate(cell_file_list):
    cell_df_list.append(pd.read_csv(os.path.join(folder_with_all_files,file), delimiter="\t"))
    cell_df_list[i]['Date_Timestamp'] = pd.to_datetime(cell_df_list[i]['Date_Timestamp'])

irr_df['MPP_Time'] = pd.to_datetime(irr_df['MPP_Time'])

# irr_df['MPP_Time'] = (irr_df['MPP_Time'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

# print(irr_df['MPP_Time'])

datedumb = cell_df_list[0].iloc[-5000]['Date_Timestamp']

result = irr_df.iloc[(irr_df['MPP_Time']-datedumb).abs().argsort()]

print(datedumb)
print(result['MPP_Time'])

# print(datetime.datetime.fromtimestamp(datedumb))
# print(datetime.datetime.fromtimestamp(result['MPP_Time']))

# Get the summary files for all the cells and produce the sum/average file
# Generate also a max point or max average point for each day and export a decimated average summary file for each cell and for the total

# Export the all the processed files for origin plotting