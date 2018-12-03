import sys
import pandas as pd
import matplotlib.pyplot as plt

try:
    folder_path_to_file = sys.argv[1]
    df = pd.read_csv(folder_path_to_file,encoding='ISO-8859-1')

    if len(sys.argv) == 2:
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
    elif len(sys.argv[2]):
        column = sys.argv[2]
        print("--", column, "--")
        print(df[column].describe())
        print()
        #df.boxplot(column=[column])
        df.hist(column=[column],bins=10)
        #df[column].hist(bins=1000)
        plt.show()
except IndexError:
    print("Please give the path to the file that should be explored")