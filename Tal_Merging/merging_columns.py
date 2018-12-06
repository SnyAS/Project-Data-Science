import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# file location for merged yield dataset
q49_file = 'C:/Users/Tal/Downloads/EPSILON_20181202_version3_merged.csv'

# read file as dataframes
df3 = pd.read_csv(q49_file)

# rename columns in dataframe
df3 = df3.rename(columns={'Hoogte_BETA_20181202_version2': 'alt(m)_', 'qual_BETA_20181202_version2': 'qual_',
                          'speedkmh_BETA_20181202_version2': 'speed(km/h)_', 'loadkg_BETA_20181202_version2':
                          'load(kg)_', 'tarekg_BETA_20181202_version2': 'tare(kg)_', 'conv.facto_BETA_20181202_version2':
                          'conv.factor_', 'beltspdm_BETA_20181202_version2': 'beltspd(m/s)_',
                          'workwidth_BETA_20181202_version2': 'workwidth(m)_', 'yieldton_BETA_20181202_version2':
                          'yield(ton/ha)_', 'totalyield_BETA_20181202_version2': 'totalyield(ton)_',
                          'point_weig_BETA_20181202_version2': 'point weight (kg)_', 'totalarea_BETA_20181202_version2':
                          'totalarea(ha)_', 'worktimes_BETA_20181202_version2': 'worktime(s)_',
                          'loadnr_BETA_20181202_version2': 'loadnr_', 'loadweight_BETA_20181202_version2':
                          'loadweight(ton)_', 'tarecorrectedtotalyield(ton)': 'tarecorrectedtotalyield(_ton)',
                          'loadbeltm_BETA_20181202_version2': 'loadbelt(m)_', 'tarecorrec_BETA_20181202_version2':
                          'tarecorrectedyield(tonha)_', 'tarecorre2_BETA_20181202_version2':
                          'tarecorrectedtotalyield(_ton)_', 'tarecorrectedyield(ton/ha)': 'tarecorrectedyield(tonha)'})

# list of regex word for merging columns
column_list = ['alt(m)', 'qual', 'speed(km/h)', 'load(kg)', 'tare(kg)', 'conv.factor', 'beltspd(m/s)', 'workwidth(m)',
               'yield(ton/ha)', 'totalyield(ton)', 'point weight', 'totalarea(ha)', 'worktime(s)', 'loadnr', 'loadweight(ton)',
               'loadbelt(m)', 'tarecorrectedyield(tonha)', 'tarecorrectedtotalyield(_ton)']

# merging columns by taking the mean of each corresponding columns values
def merge_columns(dataframe, column_regex_list):
    for column_name in column_regex_list:
        column_list = [col for col in dataframe.columns if column_name in col]
        dataframe['mean_' + '%s' % column_name] = dataframe[column_list].mean(axis=1)
        dataframe = dataframe.drop(column_list, axis=1)
        print(column_list)
    return dataframe

# visualize the correlation using heatmap
def heatmap(num_of_columns, dataframe):
    k = num_of_columns #number of variables for heatmap
    corrmat = dataframe.corr()
    cols = corrmat.nlargest(k, 'mean_yield(ton/ha)')['mean_yield(ton/ha)'].index
    cm = np.corrcoef(dataframe[cols].values.T)
    sns.set(font_scale=1)
    hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 8}, yticklabels=cols.values, xticklabels=cols.values)
    plt.show()
    return

# amount of columns with duplicates
len(df3.columns)

# merging the columns
merged_df = merge_columns(df3, column_list)

# amount of columns after merging
len(merged_df.columns)

# drop useless/redundent columns
df = merged_df.drop(['Unnamed: 0', 'year', 'month', 'day', 'hr', 'min', 'sec', 'mean_alt(m)', 'mean_tare(kg)',
                     'mean_conv.factor', 'usertare(%)'], axis=1)

# amount of columns after drop
len(df.columns)

# visualize the correlations
heatmap(len(df.columns), df)

# drop identical columns
df = df.drop(['mean_worktime(s)', 'mean_tarecorrectedtotalyield(_ton)', 'x(m)', 'y(m)'], axis=1)

# amount of columns in dataftame
len(df.columns)

# visualize correlation
heatmap(16, df)

# save to CSV
df.to_csv('C:/Users/Tal/Desktop/Tal/Year 4/big data/merged_data.csv')