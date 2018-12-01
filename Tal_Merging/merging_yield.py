import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# files locations
q49_file = 'C:/Users/Tal/Downloads/Yield(1)__000029-20180305-033343-Q49_Uien_2018.csv'
q49_file2 = 'C:/Users/Tal/Downloads/Yield(2)__opb_uien_q49.csv'

# read files as dataframes
df3 = pd.read_csv(q49_file, encoding='ISO-8859-1')
df4 = pd.read_csv(q49_file2)

# rename suffix of columns in df4 to the same as in df3
df4 = df4.rename(columns={'speed(km/h': 'speed(km/h)', 'conv.facto': 'conv.factor',
                          'X': 'lon(degr)', 'Y': 'lat(degr)',
                          'beltspd(m/': 'beltspd(m/s)', 'workwidth(': 'workwidth(m)',
                          'yield(ton/': 'yield(ton/ha)', 'totalyield': 'totalyield(ton)',
                          'point_weig': 'point weight (kg)', 'totalarea(': 'totalarea(ha)',
                          'worktime(s': 'worktime(s)', 'loadweight': 'loadweight(ton)',
                          'loadbelt(m': 'loadbelt(m)', 'usertare(%': 'usertare(%)',
                          'tarecorrec': 'tarecorrectedyield(ton/ha)', 'tarecorre2': 'tarecorrectedtotalyield(ton)'})

# remove irrelevant/redundent columns
df3 = df3.drop(['year', 'month', 'day', 'sec', 'qual', 'tare(kg)', 'conv.factor', 'usertare(%)', 'sats', 'alt(m)'], axis=1)
df4 = df4.drop(['year', 'month', 'day', 'sec', 'qual', 'Hoogte', 'tare(kg)', 'conv.factor', 'usertare(%)'], axis=1)

# round to longitude and latitude to 5 decimals so there will be only 291 different rows
df3['lon(degr)'] = round(df3['lon(degr)'], 5)
df3['lat(degr)'] = round(df3['lat(degr)'], 5)
df4['lon(degr)'] = round(df4['lon(degr)'], 5)
df4['lat(degr)'] = round(df4['lat(degr)'], 5)

pd.concat([df3[['lon(degr)', 'lat(degr)']],df4[['lon(degr)', 'lat(degr)']]]).drop_duplicates(keep=False, inplace=False)
# 291 different rows when it comes to latitude and longitude
df3.count() # 35883
df4.count() # 35880

# Inner join of two dataframes on longitude and latitude - including duplicates
inner_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='inner').fillna(0).reset_index(drop=True))
# unique rows based on the combination of longitude and latitude
unique_inner_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='inner').drop_duplicates(['lon(degr)', 'lat(degr)']).reset_index(drop=True))
# Amount of unique rows
unique_inner_df.count() # 29109 unique rows
# Amount of original data-points lost
print(len(df3) - len(unique_inner_df)) # lost 6775 data points
# Amount of repeated combinations of longitude and latitude
print(len(inner_df) - len(unique_inner_df)) # 20235 redundant rows
# plot doesn't work with the current datasets
sns.scatterplot(x='lon(degr)', y='lat(degr)', data=unique_inner_df, legend='brief')

# Outer join of two dataframes on longitude and latitude - including duplicates
outer_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='outer').fillna(0).reset_index(drop=True))
# unique rows based on the combination of longitude and latitude
unique_outer_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='outer').drop_duplicates(['lon(degr)', 'lat(degr)']).reset_index(drop=True))
# Amount of unique rows
unique_outer_df.count() # 29249 unique rows
# Amount of original data-points lost
print(len(df3) - len(unique_outer_df)) # lost 6484 data points
# Amount of repeated combinations of longitude and latitude
print(len(outer_df) - len(unique_outer_df)) # 20235 redundant rows

# Left join of two dataframes on longitude and latitude - including duplicates
left_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='left').fillna(0).reset_index(drop=True))
# unique rows based on the combination of longitude and latitude
unique_left_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='left').drop_duplicates(['lon(degr)', 'lat(degr)']).reset_index(drop=True))
# Amount of unique rows
unique_left_df.count() # 29109 unique rows
# Amount of original data-points lost
print(len(df3) - len(unique_left_df)) # lost 6624 data points
# Amount of repeated combinations of longitude and latitude
print(len(left_df) - len(unique_left_df)) # 20235 redundant rows

# Right join of two dataframes on longitude and latitude - including duplicates
right_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='right').fillna(0).reset_index(drop=True))
# unique rows based on the combination of longitude and latitude
unique_right_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='right').drop_duplicates(['lon(degr)', 'lat(degr)']).reset_index(drop=True))
# Amount of unique rows
unique_right_df.count() # 29249 unique rows
# Amount of original data-points lost
print(len(df3) - len(unique_right_df)) # lost 6635 data points
# Amount of repeated combinations of longitude and latitude
print(len(right_df) - len(unique_right_df)) # 20235 redundant rows

# Write all unique dataframes to csv
unique_inner_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_unique_inner_join.csv')
unique_outer_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_unique_outer_join.csv')
unique_left_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_unique_left_join.csv')
unique_right_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_unique_right_join.csv')

# Write all full dataframes to csv
inner_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_inner_join.csv.csv')
outer_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_outer_join.csv')
left_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_left_join.csv')
right_df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/yield_right_join.csv')