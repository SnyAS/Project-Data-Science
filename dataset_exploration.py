import sys
import pandas as pd

try:
    folder_path_to_file = sys.argv[1]
    df = pd.read_csv(folder_path_to_file,encoding='ISO-8859-1')
    
    print("There are", df.columns.size, "columns with following names:" )
    print(str(df.columns.values).replace("\n",""))
    print("There are", df.shape[0],"rows")
    print()
    print("Column Exploration:")
    columns = df.columns.values
    print()
    for column in columns:
        print("--",column,"--")
        print(df[column].describe())
        print()
except IndexError:
    print("Please give the path to the file that should be explored")