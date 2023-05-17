from tkinter import filedialog
import os
import pandas as pd
import datetime
import time

folder_with_all_files = filedialog.askdirectory(initialdir = r'P:\Job Documents\Omegalab\Greenhouse\Data\Summary',mustexist = True,title = "Select the directory which you want to check")

cell_file_list = sorted(os.listdir(folder_with_all_files))
cell_file_list.pop(-1)

for i, file in enumerate(cell_file_list):
    if 'Cell' in file:
        pass

    elif 'Irr' in file:
        irr_df = pd.read_csv(os.path.join(folder_with_all_files,file), delimiter="\t")
        cell_file_list.pop(i)

    else:
        cell_file_list.pop(i)

cell_df_list = list()

def make_summary_file(label):
    for i,file in enumerate(cell_file_list):
        cell_df_list.append(pd.read_csv(os.path.join(folder_with_all_files, file), delimiter="\t"))
        cell_df_list[i]['Date_Timestamp'] = pd.to_datetime(cell_df_list[i]['Date_Timestamp'], format='%Y-%m-%d %H:%M:%S')

        max_values_raw = cell_df_list[i].groupby([cell_df_list[i]['Date_Timestamp'].dt.date])[label].max()

        if i == 0:
            max_values = pd.DataFrame(max_values_raw).reset_index()
            max_values.rename(columns = {label:f'{label}_1'}, inplace = True)


        else:
            max_values_dumb = pd.DataFrame(max_values_raw).reset_index()
            max_values[f'{label}_{i+1}'] = max_values_dumb[label]

    # print(max_values)
    max_values.to_csv(os.path.join(folder_with_all_files,f'max_{label}_values.txt'),sep='\t',index=False)

columns = ['Isc','Voc','FF','Power']

for label in columns:
    make_summary_file(label)

irr_df['MPP_Time'] = pd.to_datetime(irr_df['MPP_Time'], format= '%d/%m/%Y %H:%M:%S')

datedumb = cell_df_list[0].iloc[-5000]['Date_Timestamp']

result = irr_df.iloc[(irr_df['MPP_Time']-datedumb).abs().argsort()[:1]]

print(datedumb)
print(result['MPP_Time'])

# Get the summary files for all the cells and produce the sum/average file
# Generate also a max point or max average point for each day and export a decimated average summary file for each cell and for the total

# Export the all the processed files for origin plotting