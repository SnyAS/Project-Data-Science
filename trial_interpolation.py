import pandas as pd
from scipy.interpolate import griddata

q49_file = '/Users/andreydelany/Documents/Inholland/Project_BigData/datasets/Yield(1).csv'
q49_file2 = '/Users/andreydelany/Documents/Inholland/Project_BigData/datasets/Yield(2).csv'

df_1 = pd.read_csv(q49_file, encoding='ISO-8859-1')
df_2 = pd.read_csv(q49_file2)

lat_dest_interpolate = df_1['lat(degr)']
lon_dest_interpolate = df_1['lon(degr)']

lat_lon_origin_interpolate = df_2[['X','Y']]

yield_origin = df_2['yield(ton/']

yield_des_nearest = griddata(lat_lon_origin_interpolate, yield_origin, (lon_dest_interpolate, lat_dest_interpolate), method='nearest')
yield_des_linear = griddata(lat_lon_origin_interpolate, yield_origin, (lon_dest_interpolate, lat_dest_interpolate), method='linear')
yield_des_cubic = griddata(lat_lon_origin_interpolate, yield_origin, (lon_dest_interpolate, lat_dest_interpolate), method='cubic')