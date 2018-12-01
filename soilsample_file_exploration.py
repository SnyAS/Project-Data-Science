import pandas as pd
import numpy as np

#load and print basic information
folder_path = "/Users/andreydelany/Documents/Inholland/Project_BigData/datasets"

df_1 = pd.read_csv(folder_path + '/SoilSample(1).csv')
#print(df_1.columns, df_1.columns.size)
#print(df_1.head())

df_2 = pd.read_csv(folder_path + '/SoilSample(2).csv')
#print(df_2.columns, df_2.columns.size)
#print(df_2.head())

print("differences can be found in followinng columns:")
#mapping different column names of the two datasets onto each other
columns = [{"1": "Lat", "2": "Y", "isDegree":True},
           {"1":"Lon",         "2":"X",            "isDegree":True},
           {"1": "Hoogte",     "2": "Hoogte",      "isDegree": False},
           {"1": "EC 0.5m",    "2": "EC_0.5m",     "isDegree": False},
           {"1": "EC 1m",      "2": "EC_1m",       "isDegree": False},
           {"1": "EC 1.5m",    "2": "EC_1.5m",     "isDegree": False},
           {"1": "EC 3m",      "2": "EC_3m",       "isDegree": False},
           {"1": "Class_3",    "2": "Class_3",     "isDegree": False},
           {"1": "Class_5",    "2": "Class_5",     "isDegree": False},
           {"1": "Outlier",    "2": "Outlier",     "isDegree": False}]

for column in columns:
    first_column = df_1[column.get("1")]
    second_column = df_2[column.get("2")]
    difference = np.where(first_column == second_column, "same", abs(first_column - second_column).astype(float))
    filtered_differences = []
    for row in difference:
        if row != "same":
            filtered_differences.append(row)
    filtered_differences = np.array(filtered_differences).astype(float)
    if len(filtered_differences) > 0:
        average_difference = np.average(filtered_differences)
        print(column.get("1") + ":")
        if column.get("isDegree"):
            print("approximate ", round(average_difference * 111000, 6), "meter")
            print("max_value", round(filtered_differences.max() * 111000, 6), "meter")
            print("min_value", round(filtered_differences.min() * 111000, 6), "meter")
        else :
            print(average_difference)
            print("max_value", filtered_differences.max())
            print("min_value", filtered_differences.min())
