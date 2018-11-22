#https://pythonhosted.org/brewery/examples/merge_multiple_files.html

import brewery
from brewery import ds
import sys
import pandas as pd
import glob
import os
import numpy as np

pathShp = "C:/Users/Administrator/Desktop/project/merge/shp"
pathSatellite = "C:/Users/Administrator/Desktop/project/merge/satelite"
allShpFiles = glob.glob(os.path.join(pathShp,"*.csv"))
allSatelliteFiles = glob.glob(os.path.join(pathSatellite,"*.csv"))
sources = [{"file": "", "fields": []}]

for file in allShpFiles:
    columnNames = pd.read_csv(file, index_col=None, header=0)
    print(columnNames)
    sources.append(allShpFiles., columnNames)


#comb_np_array = np.vstack(np_array_list)
#big_frame = pd.DataFrame(comb_np_array)

#big_frame.columns = ["col1","col2"....]


# Create list of all fields and add filename to store information
# about origin of data records
all_fields = brewery.FieldList(["file"])

# Go through source definitions and collect the fields
for source in sources:
    for field in source["fields"]:
        if field not in all_fields:
            all_fields.append(field)

#Prepare the output stream into merged.csv and specify fields we have found in sources and want to write into output:
out = ds.CSVDataTarget("merged.csv")
out.fields = brewery.FieldList(all_fields)
out.initialize()

#Go through all sources and merge them:
for source in sources:
    path = source["file"]

    # Initialize data source: skip reading of headers - we are preparing them ourselves
    # use XLSDataSource for XLS files
    # We ignore the fields in the header, because we have set-up fields
    # previously. We need to skip the header row.

    src = ds.CSVDataSource(path, read_header=False, skip_rows=1)
    src.fields = ds.FieldList(source["fields"])
    src.initialize()

    for record in src.records():

        # Add file reference into ouput - to know where the row comes from
        record["file"] = path
        out.append(record)

    # Close the source stream
    src.finalize()


#“pretty print” it with:

#$ cat merged.csv | brewery pipe pretty_printer
#And you can see the completeness aspect of data quality with simple audit:

#$ cat merged.csv | brewery pipe audit pretty_printer
