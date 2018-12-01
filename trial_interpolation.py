import pandas as pd
from numpy.core.multiarray import ndarray
from scipy.interpolate import griddata

q49_file = '/Users/andreydelany/Documents/Inholland/Project_BigData/datasets/Yield(1).csv'
q49_file2 = '/Users/andreydelany/Documents/Inholland/Project_BigData/datasets/Yield(2).csv'

df_1 = pd.read_csv(q49_file, encoding='ISO-8859-1')
df_2 = pd.read_csv(q49_file2)

lat_dest_interpolate = df_1['lat(degr)']
lon_dest_interpolate = df_1['lon(degr)']

lat_lon_origin_interpolate = df_2[['X','Y']]

yield_origin = df_2['yield(ton/']
yield_des_actual = df_1['yield(ton/ha)']

yield_des_nearest = griddata(lat_lon_origin_interpolate, yield_origin, (lon_dest_interpolate, lat_dest_interpolate), method='nearest')
yield_des_linear = griddata(lat_lon_origin_interpolate, yield_origin, (lon_dest_interpolate, lat_dest_interpolate), method='linear')
yield_des_cubic = griddata(lat_lon_origin_interpolate, yield_origin, (lon_dest_interpolate, lat_dest_interpolate), method='cubic')


def validation(actual,predicted):
    actual_array = actual.as_matrix()
    if type(predicted) is not ndarray:
        predicted_array = predicted.as_matrix()
    else:
        predicted_array = predicted
    differences = []
    outliers = []
    for i in range(actual.shape[0]):
        predicted_value = predicted_array[i].item()
        try:
            if type(actual_array[i]) is str:
                actual_value = float(actual_array[i].replace("$","").replace(".", "."))
            else:
                actual_value = actual_array[i]
            difference = abs(actual_value - predicted_value)
            if difference > 1.:
                outliers.append(difference)
            differences.append(difference)

        except Exception as err:
            print(predicted_array[i],type(predicted_array[i]),i, err)
    differences = pd.np.array(differences).astype(float)
    print('average_error:',pd.np.nanmean(differences))
    print('max_error:',pd.np.nanmax(differences))
    print('min_error:',pd.np.nanmin(differences))
    print('amount_of_errors_over_one:',len(outliers))

print("nearest Neighbor")
validation(yield_des_actual, yield_des_nearest)
print("linear")
validation(yield_des_actual,yield_des_linear)
print("cubic")
validation(yield_des_actual,yield_des_cubic)