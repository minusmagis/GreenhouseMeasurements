import pandas as pd


def get_last_day_data(param_summary_file):
    '''
    :param param_summary_file: csv file with a Date_Timestamp timestamp that has the date in 'YYYY-MM-DD HH:MM:SS' format
    :return: pandas dataframe with all the columns that have the same date YYYY-MM-DD as the last row.
    '''
    param_summary_df = pd.read_csv(param_summary_file, sep='\t')

    remove_index_list = list()
    today, last_meas_time = param_summary_df['Date_Timestamp'].iloc[-1].split(' ')

    for index, row in param_summary_df.iterrows():
        row_date = row['Date_Timestamp'].split(' ')[0]
        if row_date != today: remove_index_list.append(index)

    df = df[df['Date_Timestamp'].isin

    today_data = param_summary_df.drop(remove_index_list)

    # print(today_data.to_string())

    return today_data


def day_power_integrate(today_data):
    '''
    :param today_data: dataframe with the data from just one day
    :return: integrated power (energy) in kWh
    '''

    today_energy = 0
    previous_timestamp = -1
    first_it = True
 #use apply!!
    # Iterate through every row and multiply the power by the time difference to obtain the generated energy
    for index, row in today_data.iterrows():
        if first_it:
            previous_timestamp = row['UNIX_Timestamp(s)']
            first_it = False

        else:
            time_difference = row['UNIX_Timestamp(s)']-previous_timestamp
            previous_timestamp = row['UNIX_Timestamp(s)']
            today_energy += ( row['Power'] * time_difference / 3600)

    return today_energy


def multi_day_power_integrate(param_summary_file):
    '''
    :param param_summary_file: csv file with a Date_Timestamp timestamp that has the date in 'YYYY-MM-DD HH:MM:SS' format
                                and the power at each timestamp
    :return: a dataframe with date timestamps, unixtimestamps for midnight, and power.

    Go through all the rows, and separate all the data into different days
    Integrate the power for each day
    '''

    df = pd.read_csv(param_summary_file, sep='\t')

    day_df_list = list()
    previous_day = None
    first_it = True

    # Go through the full summary for the cells and make a new dataframe everytime the date changes,
    # add the row info to the new dataframe and append this new dataframe to the day_df_list
    for index, row in df.iterrows():
        if first_it:
            # Create a new dataframe with the same columnames as the input df and store the first row
            new_df = pd.DataFrame(columns=list(df.columns))
            new_df.loc[len(new_df)] = row
            day_df_list.append(new_df)

            # Set the previous day for further iterations and the first_it flag to false
            previous_day = row['Date_Timestamp'].split(' ')[0]
            first_it = False

        # if the row_date is different create a new dataframe, otherwise just add the current row to the existing dataframe
        else:
            row_date = row['Date_Timestamp'].split(' ')[0]
            if row_date != previous_day:
                new_df = pd.DataFrame(columns=list(df.columns))
                new_df.loc[len(new_df)] = row
                day_df_list.append(new_df)

                previous_day = row_date

            else:  day_df_list[-1].loc[len(day_df_list[-1])] = row

    # Create a dataframe that will store the energy per day with the time and energy information
    # iterate through all the generated dataframes and integrate the power of the day to add it to the energy_per_day_df
    columns = ['Date_Timestamp', 'UNIX_Timestamp(s)', 'energy(kWh)']
    energy_per_day_df = pd.DataFrame(columns=columns)
    for df in day_df_list:
        energy_per_day_df.loc[len(energy_per_day_df)] = [df['Date_Timestamp'].iloc[0],df['UNIX_Timestamp(s)'].iloc[0],day_power_integrate(df)]

    # print(energy_per_day_df.to_string())

    return energy_per_day_df



if __name__ == '__main__':
    today_data = get_last_day_data('test/Summary/Cell1_param.txt')
    total_energy_data = multi_day_power_integrate('test/Summary/Cell1_param.txt')

    # print(today_data.to_string())
    # print(last_day_power_integrate(today_data))

