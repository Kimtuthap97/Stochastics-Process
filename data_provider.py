import pandas as pd
from pandas import read_csv

dataframe = read_csv('alldongda.csv', usecols=[1, 2], engine='python', skipfooter=3)

data_to_write = []
last_hour = -1
for idx, row in dataframe.iterrows():
    curr_hour = row['hours']
    if curr_hour != last_hour - 1 and curr_hour >= 0:
        if curr_hour == 23 and last_hour == 0:
            continue
        if curr_hour < last_hour:
            data_to_write.extend([0] * (last_hour - curr_hour))
        else:
            data_to_write.extend([0] * (last_hour + 23 - curr_hour))
    data_to_write.append(row['count_id'])
    last_hour = curr_hour

d = {"count": data_to_write}
d = pd.DataFrame(data=d)
d.to_csv("count_dongda.csv")
