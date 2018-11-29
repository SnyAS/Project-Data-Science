import pandas as pd

# two files locations
file1 = 'C:/Users/Tal/Downloads/SoilSample(1)__20180301_max_sturm_q_49.csv'
file2 = 'C:/Users/Tal/Downloads/SoilSample(2)__bodemscanq49.csv'

# read the files
df = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# check how many different rows
pd.concat([df,df2]).drop_duplicates(keep=False, inplace=False) # 6 decimals - all rows are different

# round to 5 decimals
df['Long'] = round(df['Long'], 5)
df['Lat'] = round(df['Lat'], 5)
df2['Long'] = round(df2['Long'], 5)
df2['Lat'] = round(df2['Lat'], 5)

# check how many different rows
different_rows = pd.concat([df,df2]).drop_duplicates(keep=False, inplace=False) # 5 decimals - 1417 different rows - either remove those rows or go to 4 decimals
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
pd.concat([new_df,new_df2]).drop_duplicates(keep=False) # Empty DataFrame which means they are the same