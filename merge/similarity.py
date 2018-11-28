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

#import pandas as pd

df3 = pd.read_csv('C:/Users/Home/Desktop/dataset/Yield(1).csv')
print(df3.columns, df3.columns.size)
df4 = pd.read_csv('C:/Users/Home/Desktop/dataset/Yield(2)__opb_uien_q49.csv')
print(df4.columns, df4.columns.size)
print(pd.concat([df3, df4]).drop_duplicates(keep=False))

'''
def merging():
    df = pd.read_csv('C:/Users/Home/Desktop/dataset/SoilSample(1)__20180301_max_sturm_q_49.csv')
    print(df.columns, df.columns.size)
    df2 = pd.read_csv('C:/Users/Home/Desktop/dataset/SoilSample(2)__bodemscanq49.csv')
    print(df2.columns, df2.columns.size)
    
    if df.columns == df2.columns:
        result = pd.merge(df, df2, on=['Lat', 'Long'])
        print(result.columns)

        result2 = df2.equals(df)
        print(result2)
        result2.to_csv("Soil - Sample")
'''
