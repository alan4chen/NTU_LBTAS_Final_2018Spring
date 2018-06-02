from metro_data import station_list

import pandas as pd
from datetime import datetime, timedelta, date
import csv

# Date
data_in_df = pd.DataFrame(columns=station_list + ['date'])
data_out_df = pd.DataFrame(columns=station_list + ['date'])
cur_date = date(year=2018, month=4, day=1)
while cur_date < date(year=2018, month=5, day=1):
    data_in_df.loc[len(data_in_df)] = [0] * len(station_list) + [cur_date]
    data_out_df.loc[len(data_in_df)] = [0] * len(station_list) + [cur_date]
    cur_date += timedelta(days=1)
data_in_df.set_index('date', inplace=True)
data_out_df.set_index('date', inplace=True)
print("==")

# Hour
hour_in_df = pd.DataFrame(columns=station_list + ['hour'])
hour_out_df = pd.DataFrame(columns=station_list + ['hour'])
cur_hour = datetime(year=2018, month=4, day=1, hour=0)
while cur_hour < datetime(year=2018, month=5, day=1):
    print(cur_hour)
    hour_in_df.loc[len(hour_in_df)] = [0] * len(station_list) + [cur_hour]
    hour_out_df.loc[len(hour_in_df)] = [0] * len(station_list) + [cur_hour]
    cur_hour += timedelta(hours=1)
hour_in_df.set_index('hour', inplace=True)
hour_out_df.set_index('hour', inplace=True)
print("==")


with open("data_201804.csv", encoding="utf-8-sig") as f:
    spamreader = csv.reader(f, delimiter=' ', skipinitialspace=True)

    flag = ""
    for row in spamreader:
        if flag != row[0] + '-' + row[1]:
            flag = row[0] + '-' + row[1]
            print(flag)
        # Date
        d = datetime.strptime(row[0], "%Y-%m-%d").date()
        data_in_df.at[d, row[2]] = int(row[4]) + data_in_df.at[d, row[2]]
        data_out_df.at[d, row[3]] = int(row[4]) + data_out_df.at[d, row[3]]

        # Hour
        h = datetime.strptime(row[0] + "-" + row[1], "%Y-%m-%d-%H")
        hour_in_df.at[h, row[2]] = int(row[4]) + hour_in_df.at[h, row[2]]
        hour_out_df.at[h, row[3]] = int(row[4]) + hour_out_df.at[h, row[3]]


print(data_in_df)
data_in_df.to_pickle('date_in.pickle')

print(data_out_df)
data_out_df.to_pickle('date_out.pickle')

print(hour_in_df)
hour_in_df.to_pickle('hour_in.pickle')

print(hour_out_df)
hour_out_df.to_pickle('hour_out.pickle')


