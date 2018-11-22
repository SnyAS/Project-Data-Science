#https://pythonhosted.org/brewery/examples/merge_multiple_files.html

import pandas as pd


df = pd.read_csv('C:/Users/Administrator/Desktop/project/merge/merge/shp/the_shp-vakkenkaart_uien.csv')
print(df.columns)
df2 = pd.read_csv('C:/Users/Administrator/Desktop/project/merge/merge/shp/the shp- opbsleep.csv')
print(df2.columns)

#(df.columns == df2.columns)

result = pd.merge(df, df2, on=['X', 'Y'])
print(result.columns)

result.to_csv("vakkenkaart_uien_opbsleep.csv")

#MERGING NEW DATASETS
df3 = pd.read_csv('C:/Users/Administrator/Desktop/project/merge/merge/shp/the shp- opb uien q49.csv')
print(df.columns)
df4 = pd.read_csv('C:/Users/Administrator/Desktop/project/merge/merge/.csv')
print(df2.columns)

result1 = pd.merge(df3, df4, on=['X', 'Y'])
print(result1.columns)

result.to_csv("opb_uien_q49+original.csv")