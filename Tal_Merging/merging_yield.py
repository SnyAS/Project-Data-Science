import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# files locations for yield datasets
q49_file = "Epsilon file"
q49_file2 = 'Beta file'

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

# describe the longitude
df3['lon(degr)'].describe()
# remove noise
df3 = df3[df3['lon(degr)'] < 6]
# describe the longitude
df4['lon(degr)'].describe()
# remove noise
df4 = df4[df4['lon(degr)'] < 6]

# round to longitude and latitude to 5 decimals so there will be only 291 different rows
df3['lon(degr)'] = round(df3['lon(degr)'], 5)
df3['lat(degr)'] = round(df3['lat(degr)'], 5)
df4['lon(degr)'] = round(df4['lon(degr)'], 5)
df4['lat(degr)'] = round(df4['lat(degr)'], 5)

pd.concat([df3[['lon(degr)', 'lat(degr)']],df4[['lon(degr)', 'lat(degr)']]]).drop_duplicates(keep=False, inplace=False)

df3.count() # 35883
df4.count() # 35880

# Inner join of two dataframes on longitude and latitude - including duplicates
inner_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='inner').reset_index(drop=True))
# unique rows based on the combination of longitude and latitude
unique_inner_df = (pd.merge(df3, df4, on=['lon(degr)', 'lat(degr)'], how='inner').drop_duplicates(['lon(degr)', 'lat(degr)']).reset_index(drop=True))
# Amount of unique rows
unique_inner_df.count() # 29108 unique rows
# Amount of original data-points lost
print(len(df3) - len(unique_inner_df)) # lost 6775 data points
# Amount of repeated combinations of longitude and latitude
print(len(inner_df) - len(unique_inner_df)) # 20235 redundant rows

# unique inner-join visualization - kde plot
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(unique_inner_df['lon(degr)'], unique_inner_df['lat(degr)'], ax=ax)
sns.rugplot(unique_inner_df['lon(degr)'], color="g", ax=ax)
sns.rugplot(unique_inner_df['lat(degr)'], vertical=True, ax=ax)

# unique inner-join visualization - scatter plot
g = sns.jointplot(x='lon(degr)', y='lat(degr)', data=unique_inner_df, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=.5, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$X$", "$Y$")

# df3 visualization - kde plot
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df3['lon(degr)'], df3['lat(degr)'], ax=ax)
sns.rugplot(df3['lon(degr)'], color="g", ax=ax)
sns.rugplot(df3['lat(degr)'], vertical=True, ax=ax)

# df3 visualization - scatter plot
g = sns.jointplot(x='lon(degr)', y='lat(degr)', data=df3, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=.5, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$X$", "$Y$")

# df4 visualization - kde plot
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df4['lon(degr)'], df4['lat(degr)'], ax=ax)
sns.rugplot(df4['lon(degr)'], color="g", ax=ax)
sns.rugplot(df4['lat(degr)'], vertical=True, ax=ax)

# df4 visualization - scatter plot
g = sns.jointplot(x='lon(degr)', y='lat(degr)', data=df4, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=.5, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$X$", "$Y$")

inner_df.isnull().any()

'''
Semida TODO:
compare each two corresponding columns and take the mean value of those column and assign it to a newly created column
drop all _x and _y columns after taking the mean of them and assign them to a new column, if column has no corresponding 
column just keep it as it is
'''

# Write all unique dataframes to csv
unique_inner_df.to_csv('C:/Users/Inholland/Desktop/dataset/yield_unique_inner_join.csv')

print(len(unique_inner_df.columns))
'''
the rest of features which can't be compared
'year', 'month', 'day', 'hr', 'min', 'sec', 'lon(degr)', 'lat(degr)', 'alt(m)',sats', 'x(m)', 'y(m)', '', 'usertare(%)', 'Hoogte', 'loadkg', '',
'''
#returning ture ->can be merged
print((unique_inner_df['workwidth(m)'].values == unique_inner_df['workwidth'].values).all()) #true
print((unique_inner_df['qual_y'].values == unique_inner_df['qual_x'].values).all()) #true
print((unique_inner_df['tare(kg)'].values == unique_inner_df['tarekg'].values).all()) #true
print((unique_inner_df['tarecorrectedtotalyield(ton)_y'].values == unique_inner_df['totalyield(ton)_y'].values).all())#duplicate?
print((unique_inner_df['totalyield(ton)_x'].values == unique_inner_df['tarecorrectedtotalyield(ton)_x'].values).all()) #true
print((unique_inner_df['workwidth'].values == unique_inner_df['workwidth(m)'].values).all()) #true

#returning false
print((unique_inner_df['tarecorrectedtotalyield(ton)_x'].values == unique_inner_df['tarecorrectedtotalyield(ton)_y'].values).all())
print((unique_inner_df['tarecorrectedyield(ton/ha)_y'].values == unique_inner_df['tarecorrectedyield(ton/ha)_x'].values).all())
print((unique_inner_df['loadweight(ton)_y'].values == unique_inner_df['loadweight(ton)_x'].values).all())
print((unique_inner_df['loadnr_y'].values == unique_inner_df['loadnr_x'].values).all())
print((unique_inner_df['point weight (kg)_y'].values == unique_inner_df['point weight (kg)_x'].values).all())
print((unique_inner_df['conv.factor_y'].values == unique_inner_df['conv.factor_x'].values).all())
print((unique_inner_df['totalyield(ton)_y'].values == unique_inner_df['totalyield(ton)_x'].values).all())
print((unique_inner_df['worktime(s)'].values == unique_inner_df['worktimes'].values).all())
print((unique_inner_df['beltspdm'].values == unique_inner_df['beltspd(m/s)'].values).all())
print((unique_inner_df['loadkg'].values == unique_inner_df['load(kg)'].values).all())
print((unique_inner_df['speed(km/h)'].values == unique_inner_df['speedkmh'].values).all())
print((unique_inner_df['beltspdm'].values == unique_inner_df['beltspd(m/s)'].values).all())
print((unique_inner_df['totalarea'].values == unique_inner_df['totalarea(ha)'].values).all())
print((unique_inner_df['yieldton'].values == unique_inner_df['yield(ton/ha)'].values).all())
print((unique_inner_df['loadbeltm'].values == unique_inner_df['loadbelt(m)'].values).all())
