
import pandas as pd

'''
from pandas.testing import assert_frame_equal
from decimal import *
'''


def soilSample():
    df = pd.read_csv('C:/Users/Home/Desktop/dataset/SoilSample(1)__20180301_max_sturm_q_49.csv')
    print(df.columns, df.columns.size)
    df2 = pd.read_csv('C:/Users/Home/Desktop/dataset/SoilSample(2)__bodemscanq49.csv')
    print(df2.columns, df2.columns.size)

    df.round({"Long": 0, "Lat": 2})
    df2.round({"Long": 0, "Lat": 2})
    print(pd.concat([df, df2]).drop_duplicates(keep=False))
    # getcontext().prec = 5

    Long = df[['Long']].values
    Long0 = df2[['Long']].values


    print(Long == Long0)
    # long = assert_frame_equal(Long, Long0)

    Lat = df[['Lat']].values
    Lat1 = df2[['Lat']].values
    print((Lat == Lat1).all())

    Hoogte = df[['Hoogte']].values
    Hoogte1 = df2[['Hoogte']].values
    print((Hoogte == Hoogte1).all())
    # hoogte = assert_frame_equal(Hoogte, Hoogte1)

    EC_05m = df[['EC_0.5m']].values
    EC_05m1 = df2[['EC_0.5m']].values
    print((EC_05m == EC_05m1).all())

    EC_1m = df[['EC_1m']].values
    EC_1m1 = df2[['EC_1m']].values
    print((EC_1m == EC_1m1).all())

    EC_15m = df[['EC_1.5m']].values
    EC_15m1 = df2[['EC_1.5m']].values
    print((EC_15m == EC_15m1).all())

    EC_3m = df[['EC_3m']].values
    EC_3m1 = df2[['EC_3m']].values
    print((EC_3m == EC_3m1).all())

    Class_3 = df[['Class_3']].values
    Class_31 = df2[['Class_3']].values
    print((Class_3 == Class_31).all())

    Class_5 = df[['Class_5']].values
    Class_51 = df2[['Class_5']].values
    print((Class_5 == Class_51).all())

    Outlier = df[['Outlier']].values
    Outlier1 = df2[['Outlier']].values
    print((Outlier == Outlier1).all())


soilSample()
# def yieldSimilarity():

import pandas as pd
#df = pd.read_csv(q49_file, encoding='ISO-8859-1')
df3 = pd.read_csv('C:/Users/Home/Desktop/dataset/Yield(1).csv', encoding='ISO-8859-1')
print(df3.columns, df3.columns.size)
df4 = pd.read_csv('C:/Users/Home/Desktop/dataset/Yield(2)__opb_uien_q49.csv')
print(df4.columns, df4.columns.size)

# check how many different rows
different_rows = pd.concat([df3, df4]).drop_duplicates(keep=False, inplace=False) # 5 decimals - 1417 different rows - either remove those rows or go to 4 decimals
len(different_rows) # if pleased, assign index to both dataframes

# assign index to each row in both dataframes
df3 = df3.reset_index()
df4 = df4.reset_index()

# create array of indexes to drop (the different rows)
index_to_drop = different_rows.index.values

# remove each row which differs from both dataframes
new_df3 = df3.drop(index_to_drop)

#KeyError: '[35880 35881 35882 35883] not found in axis'
new_df4 = df4.drop(index_to_drop)

# drop index column from both dataframes
new_df3 = new_df3.drop(['index'], axis=1)
new_df4 = new_df4.drop(['index'], axis=1)

# check how many different rows
pd.concat([new_df3, new_df4]).drop_duplicates(keep=False) # Empty DataFrame which means they are the same
'''
def merging():
    df = pd.read_csv('C:/Users/Home/Desktop/dataset/SoilSample(1)__20180301_max_sturm_q_49.csv')
    print(df.columns, df.columns.size)
    df2 = pd.read_csv('C:/Users/Home/Desktop/dataset/SoilSample(2)__bodemscanq49.csv')
    print(df2.columns, df2.columns.size)
    
    if df.columns == df2.columns:
        result = pd.semidas_old_files(df, df2, on=['Lat', 'Long'])
        print(result.columns)

        result2 = df2.equals(df)
        print(result2)
        result2.to_csv("Soil - Sample")
'''


# two files locations
file1 = 'C:/Users/Home/Desktop/dataset/SoilSample(1)__20180301_max_sturm_q_49.csv'
file2 = 'C:/Users/Home/Desktop/dataset/SoilSample(2)__bodemscanq49.csv'

# read the files
df = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# check how many different rows
pd.concat([df, df2]).drop_duplicates(keep=False, inplace=False) # 6 decimals - all rows are different

# round to 5 decimals
df['Long'] = round(df['Long'], 5)
df['Lat'] = round(df['Lat'], 5)
df2['Long'] = round(df2['Long'], 5)
df2['Lat'] = round(df2['Lat'], 5)

# check how many different rows
different_rows = pd.concat([df, df2]).drop_duplicates(keep=False, inplace=False) # 5 decimals - 1417 different rows - either remove those rows or go to 4 decimals
len(different_rows) # if pleased, assign index to both dataframes

# assign index to each row in both dataframes
df = df.reset_index()
df2 = df2.reset_index()

# create array of indexes to drop (the different rows)
index_to_drop = different_rows.index.values

# remove each row which differs from both dataframes
new_df = df.drop(index_to_drop)
new_df2 = df2.drop(index_to_drop)

# drop index column from both dataframes
new_df = new_df.drop(['index'], axis=1)
new_df2 = new_df2.drop(['index'], axis=1)

# check how many different rows
pd.concat([new_df, new_df2]).drop_duplicates(keep=False) # Empty DataFrame which means they are the same