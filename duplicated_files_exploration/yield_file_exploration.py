import pandas as pd
import numpy as np

#load and print basic information
folder_path = "/Users/andreydelany/Documents/Inholland/Project_BigData/datasets"

df_1 = pd.read_csv(folder_path + '/Yield(1).csv', encoding='ISO-8859-1')
print(df_1.columns, df_1.columns.size)
print(df_1.head())
print(df_1.shape)

df_2 = pd.read_csv(folder_path + '/Yield(2).csv')
print(df_2.columns, df_2.columns.size)
print(df_2.head())
print(df_2.shape)

#mapping different column names of the two datasets onto each other
columns = [{"1": "lat(degr)",  "2": "Y",           "isDegree":True},
           {"1":'lon(degr)',   "2":"X",            "isDegree":True},
           {"1": "year",     "2": "year",      "isDegree": False},
           {"1": "month",    "2": "month",     "isDegree": False},
           {"1": "day",      "2": "day",       "isDegree": False},
           {"1": "hr",    "2": "hr",     "isDegree": False},
           {"1": "min",      "2": "min",       "isDegree": False},
           {"1": "sec",    "2": "sec",     "isDegree": False},
           {"1": "qual",    "2": "qual",     "isDegree": False},
           {"1": "speed(km/h)",    "2": "speed(km/h",     "isDegree": False},
           {"1": "load(kg)", "2": "load(kg)", "isDegree": False},
           {"1": "tare(kg)", "2": "tare(kg)", "isDegree": False},
           {"1": "conv.factor", "2": "conv.facto", "isDegree": False},
           {"1": "beltspd(m/s)", "2": "beltspd(m/", "isDegree": False},
           {"1": "workwidth(m)", "2": "workwidth(", "isDegree": False},
           {"1": "yield(ton/ha)", "2": "yield(ton/", "isDegree": False},
           {"1": "totalyield(ton)",    "2": "totalyield",     "isDegree": False},
           {"1": "point weight (kg)",    "2": "point_weight",     "isDegree": False},
           {"1": "totalarea(ha)",    "2": "totalarea(",     "isDegree": False},
           {"1": "'worktime(s)",    "2": "'worktime(s",     "isDegree": False},
           {"1": "loadnr",    "2": "loadnr",     "isDegree": False},
           {"1": "loadweight(ton)",    "2": "loadweight",     "isDegree": False},
           {"1": "loadbelt(m)",    "2": "loadbelt(m",     "isDegree": False},
           {"1": "usertare(%)",    "2": "usertare(%",     "isDegree": False},
           {"1": "tarecorrectedyield(ton/ha)",    "2": "tarecorrec",     "isDegree": False},
           {"1": "tarecorrectedtotalyield(ton)",    "2": "tarecorre2",     "isDegree": False},           ]

df_1 = df_1.rename(columns={"lat(degr)":"lat","lon(degr)":"lon","speed(km/h)":"speed","beltspd(m/s)":"beltspd",
                     "workwidth(m)":"workwidth","yield(ton/ha)":"yield(ton/ha)","totalarea(ha)":"totalarea","worktime(s)":"worktime",
                     "loadweight(ton)":"loadweight","loadbelt(m)":"loadbelt","usertare(%)":"usertare","tarecorrectedyield(ton/ha)":"tarecorrectedyield",
                     "tarecorrectedtotalyield(ton)":"tarecorrectedtotalyield"})

df_2 = df_2.rename(columns={"Y":"lat","X":"lon","speed(km/h":"speed","conv.facto":"conv.factor","beltspd(m/":"beltspd",
                     "workwidth(":"workwidth","yield(ton/":"yield","totalarea(":"totalarea","worktime(s":"worktime",
                     "loadbelt(m":"loadbelt","usertare(%":"usertare","tarecorrec":"tarecorrectedyield",
                     "tarecorre2":"tarecorrectedtotalyield"})

#similar columns
columns_1 = set(df_1.columns)
columns_2 = set(df_2.columns)
intersection = list(set(columns_1).intersection(columns_2))
print(len(intersection),intersection)

df_1['lon'] = round(df_1['lon'], 6)
df_1['lat'] = round(df_1['lat'], 6)
df_2['lon'] = round(df_2['lon'], 6)
df_2['lat'] = round(df_2['lat'], 6)

df_12 = df_1[intersection]
print(df_12.shape)
df_22 = df_2[intersection]
print(df_22.shape)

#drop last four rows of second dataset
for i in range(4):
    df_12 = df_12.drop(df_12.index[-1])

print(df_12.shape)
print(df_22.shape)

df_12 = df_12.sort_values(by=["lat","lon"])
df_22 = df_22.sort_values(by=["lat","lon"])

df_12 = df_12.reset_index(drop=True)
df_22 = df_22.reset_index(drop=True)

#print(df_12[:5])
#print(df_22[:5])

for column in intersection:
    first_column = df_12[column]
    second_column = df_22[column]
    difference = np.where(first_column.astype(float) == second_column.astype(float), "same", abs(first_column - second_column).astype(float))
    filtered_differences = []
    for row in difference:
        if row != "same":
            filtered_differences.append(row)
    filtered_differences = np.array(filtered_differences).astype(float)
    if len(filtered_differences) > 0:
        average_difference = np.average(filtered_differences)
        print(column + ":")
        print(len(filtered_differences))
        print(average_difference)
        print("max_value", filtered_differences.max())
        print("min_value", filtered_differences.min())
        print()
