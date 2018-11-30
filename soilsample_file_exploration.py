import pandas as pd
import numpy as np

#load and print basic information
folder_path = "/Users/andreydelany/Documents/Inholland/Project_BigData/datasets"
df_1 = pd.read_csv(folder_path + '/SoilSample(1).csv')
print(df_1.columns, df_1.columns.size)
print(df_1.head())
df_2 = pd.read_csv(folder_path + '/SoilSample(2).csv')
print(df_2.columns, df_2.columns.size)
print(df_2.head())

print("differences can be found in followinng columns:")
dict = [{"1":"Lat","2":"Y","isDegree":True},
        {"1":"Lon","2":"X","isDegree":True},
        {"1": "Hoogte", "2": "Hoogte", "isDegree": False},
        {"1": "EC 0.5m", "2": "EC_0.5m", "isDegree": False},
        {"1": "EC 1m", "2": "EC_1m", "isDegree": False},
        {"1": "EC 1.5m", "2": "EC_1.5m", "isDegree": False},
        {"1": "EC 3m", "2": "EC_3m", "isDegree": False},
        {"1": "Class_3", "2": "Class_3", "isDegree": False},
        {"1": "Class_5", "2": "Class_5", "isDegree": False},
        {"1": "Outlier", "2": "Outlier", "isDegree": False},]
for entry in dict:
    first_column = df_1[entry.get("1")]
    second_column = df_2[entry.get("2")]
    result = np.where(first_column == second_column, "same", abs(first_column - second_column).astype(float))
    filtered_result = []
    for row in result:
        if row != "same":
            filtered_result.append(row)
    filtered_result = np.array(filtered_result).astype(float)
    if len(filtered_result) > 0:
        average = np.average(filtered_result)
        print(entry.get("1") + ":")
        if entry.get("isDegree"):
            print("approximate ", round(average * 111000,6), "meter")
            print("max_value", round(filtered_result.max() * 111000,6),"meter")
            print("min_value", round(filtered_result.min() * 111000,6),"meter")
        else :
            print(average)
            print("max_value",filtered_result.max())
            print("min_value", filtered_result.min())
