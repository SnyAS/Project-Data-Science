import argparse
import pandas as pd
from scipy.interpolate import griddata

parser = argparse.ArgumentParser(description='Resampling Columns from one dataset to another depending on geo coordinates')
parser.add_argument('filepath_target', help='path to target file')
parser.add_argument('target_x')
parser.add_argument('target_y')
parser.add_argument('filepath_to_be_merged', help='path to file that going to be merged')
parser.add_argument('tobemerged_x')
parser.add_argument('tobemerged_y')
parser.add_argument('interpolation_method',choices=['nearest','linear','cubic'])
args = parser.parse_args()

def test():
    d = {'x': [-1,-1,1,1], 'y': [-1,1,-1,1],'value':[2,1,4,3]}
    target = pd.DataFrame(data=d)


    d = {'x': [-0.5,-0.5,0.5,0.5], 'y': [-0.5,0.5,-0.5,0.5],'value_interpolated':[2,1,4,3]}
    tobe_merged = pd.DataFrame(data=d)

    target_values = griddata(tobe_merged[["x","y"]], tobe_merged["value_interpolated"], target[["x","y"]], method="nearest")

    #target = target.reset_index(drop=True)
    target_values = target_values.reset_index(drop=True)

    final = pd.concat([target,target_values],axis=1)
    print(final.head())

def load_dataframe(path_to_file):
    return pd.read_csv(path_to_file, encoding='ISO-8859-1')

def get_file_name(path_to_file):
    parts_of_path = path_to_file.split("/")
    return parts_of_path[-1].replace(".csv","")

filepath_to_be_merged = args.filepath_to_be_merged
filename_to_be_merged = get_file_name(filepath_to_be_merged)

target_filepath = args.filepath_target
target_file = load_dataframe(target_filepath)
file_to_be_merged = load_dataframe(filepath_to_be_merged)

target_file_coordinate_identifier = [args.target_x,args.target_y]
file_to_be_merged_coordinate_identifier = [args.tobemerged_x,args.tobemerged_y]

all_columns_of_to_be_merged_file= list(file_to_be_merged)
columns_to_be_merged = [x for x in all_columns_of_to_be_merged_file if x not in file_to_be_merged_coordinate_identifier]

coordinates_to_be_interpolated = file_to_be_merged[file_to_be_merged_coordinate_identifier]
target_coordinates = target_file[target_file_coordinate_identifier]

for column in columns_to_be_merged:
    values_to_be_interpolated = file_to_be_merged[column]
    target_values = griddata(coordinates_to_be_interpolated, values_to_be_interpolated, target_coordinates, method=args.interpolation_method)
    if type(target_values) is not pd.np.ndarray:
        target_values = target_values.values

    new_column_name = column + "_" + filename_to_be_merged

    #target_values = target_values.reset_index(drop=True)

    target_file[new_column_name] = target_values
    #target_file = pd.concat([target_file, target_values], axis=1)

target_file.to_csv(target_filepath.replace(".csv","_merged.csv"))
