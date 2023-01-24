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

for i,file in enumerate(cell_file_list):
    cell_df_list.append(pd.read_csv(os.path.join(folder_with_all_files, file), delimiter="\t"))
    cell_df_list[i]['Date_Timestamp'] = pd.to_datetime(cell_df_list[i]['Date_Timestamp'], format='%Y-%m-%d %H:%M:%S')

    max_values_raw = cell_df_list[i].groupby([cell_df_list[i]['Date_Timestamp'].dt.date])['Power'].nlargest(1)
    # print(max_values_raw)
    if i == 0:
        max_values = pd.DataFrame(max_values_raw).reset_index()
        # print(max_values)
        max_values.rename(columns = {'Power':'Power_1'}, inplace = True)
    else:
        max_values_dumb = pd.DataFrame(max_values_raw).reset_index()
        max_values[f'level_{i + 1}'] = max_values_dumb['level_1']
        max_values[f'Power_{i+1}'] = max_values_dumb['Power']


columns = ['Isc','Voc','FF','PCE','Date_Timestamp']
data_list = list()  # the list for each cell
list_cell = list()  # the bigger list

for i,cell in enumerate(cell_df_list):
    data_list = list()
    for label in columns:
        foo_list = list()
        # foo_list.append(label)
        for value in max_values[f'level_{i+1}']:
            foo_list.append(cell[cell.index == value][label].values[0])
        data_list.append(foo_list)
    list_cell.append(data_list)

# print(list_cell,sep='\n')

df_final_list = list()
for i,cell in enumerate(cell_df_list):
    df_final_list.append(pd.DataFrame(list_cell[i]))
    df_final_list[i] = df_final_list[i].transpose()
    df_final_list[i].rename({0:'Isc',1:'Voc',2:'FF',3:'PCE',4:'Date_Timestamp_Exact'},axis=1,inplace=True)
    # print(df_final_list[0])

for i,cell in enumerate(cell_df_list):
    df_final_list[i]['Power'] = max_values[f'Power_{i+1}']
    df_final_list[i]['Datestamp'] = max_values['Date_Timestamp']

cell_irr_list = list()
for i,cell_df in enumerate(df_final_list):
    irr_list = list()
    for i,row in cell_df.iterrows():
        date = row['Date_Timestamp_Exact']
        irr_df['MPP_Time'] = pd.to_datetime(irr_df['MPP_Time'], format= '%d/%m/%Y %H:%M:%S')
        irr_list.append(irr_df.iloc[(irr_df['MPP_Time'] - date).abs().argsort()[:1]]['_index_218-EKO MS-802'].values[0])
    cell_irr_list.append(irr_list)

# print(cell_irr_list)

df_final_irr_list = list()
for i,cell in enumerate(cell_irr_list):
    df_final_irr_list.append(pd.DataFrame(cell_irr_list[i]))
    # df_final_irr_list[i] = df_final_irr_list[i].transpose()
    df_final_irr_list[i].rename({0:'Irradiance_W_m-2'},axis=1,inplace=True)
    df_final_irr_list[i]['Irradiance_W_m-2'] = df_final_irr_list[i]['Irradiance_W_m-2'].astype(float)

# print(df_final_irr_list)

for i,cell in enumerate(df_final_list):
    cell['Irradiance_W_m-2'] = df_final_irr_list[i]['Irradiance_W_m-2']

    cell['Real_PCE'] = 100*cell['Power']/(df_final_irr_list[i]['Irradiance_W_m-2']*14.0064)

columns_ordering = ['Datestamp','Date_Timestamp_Exact','Irradiance_W_m-2','Isc','Voc','FF','PCE','Power','Real_PCE']

for i, cell in enumerate(df_final_list):
    cell = cell[columns_ordering]
    cell = cell.round(2)
    cell.to_csv(os.path.join(folder_with_all_files,f'cell_{i+1}_summary_max_values.txt'),sep='\t',index=False)

    # max_values.to_csv(os.path.join(folder_with_all_files,f'max_Power_values.txt'),sep='\t',index=False)
#
#
# irr_df['MPP_Time'] = pd.to_datetime(irr_df['MPP_Time'], format= '%d/%m/%Y %H:%M:%S')
#
# datedumb = cell_df_list[0].iloc[-5000]['Date_Timestamp']
#
# result = irr_df.iloc[(irr_df['MPP_Time']-datedumb).abs().argsort()[:1]]
#
# print(datedumb)
# print(result['MPP_Time'])