#coding=utf8
from metro_data import station_list
import pandas as pd
import numpy as np
import json, io


df_hourin = pd.read_pickle("hour_in.pickle")
df_hourout = pd.read_pickle("hour_out.pickle")


df = pd.DataFrame(columns=df_hourin.columns)
for i in range(0,48):
    df.loc[len(df)] = [0] * len(station_list)
df.index = list(range(0,48))


for index, row in df_hourin.iterrows():
    cur_weekday = index.isoweekday()
    cur_hour = index.hour
    if cur_weekday < 6:
        df.loc[cur_hour] = df.loc[cur_hour] + row
    else:
        df.loc[cur_hour+24] = df.loc[cur_hour+24] + row

for index, row in df_hourout.iterrows():
    cur_weekday = index.isoweekday()
    cur_hour = index.hour
    if cur_weekday < 6:
        df.loc[cur_hour] = df.loc[cur_hour] + row
    else:
        df.loc[cur_hour+24] = df.loc[cur_hour+24] + row

d = {}
for column in df:
    d[column] = list(df[column])
s = json.dumps(d, ensure_ascii=False)

s = s.replace('"','')
print(s)

f = io.open("web/metrohourflow.js", mode="w", encoding='utf8')
f.write("var metrohourflow = " + s + ";")
