import osr
from osgeo import gdal
import csv
import argparse

parser = argparse.ArgumentParser(description='GeoTiff to CSV translator')
parser.add_argument('path_to_geo_tiff_file', help='path to geoTiff file')
parser.add_argument('path_to_output_csv_file', help='path to output csv file')
args = parser.parse_args()

#used information from following link for extraction and translation of x,y to lat,long
#https://gis.stackexchange.com/questions/57710/determining-coordinates-of-corners-of-raster-layer-using-pyqgis/57711#57711

#loading tiff
tiff_as_raster = gdal.Open(args.path_to_geo_tiff_file, gdal.GA_ReadOnly)

#extract dim of raster
width = tiff_as_raster.RasterXSize
height = tiff_as_raster.RasterYSize

#extract data for mapping x,y to basic geo_x,geo_y coordinates
geoTransformation_data = tiff_as_raster.GetGeoTransform()

#extract and prepare transformation for geo_x,geo_y to lat,long
projectionRef = tiff_as_raster.GetProjectionRef()
spatialRef = osr.SpatialReference(projectionRef)
geograficCs =spatialRef.CloneGeogCS()
latlong_transformation = osr.CoordinateTransformation(spatialRef, geograficCs)

#extract pixel_values from raster
pixel_values = tiff_as_raster.ReadAsArray()
data_points = []

def calc_geoxy(x, y):
    geo_x = geoTransformation_data[0] + geoTransformation_data[1] * float(x) + geoTransformation_data[2] * float(y)
    geo_y = geoTransformation_data[3] + geoTransformation_data[4] * float(x) + geoTransformation_data[5] * float(y)
    return geo_x,geo_y

def calc_latlong(x,y):
    geo_pt = latlong_transformation.TransformPoint(x, y)[:2]
    return geo_pt[1],geo_pt[0]

def get_pixel_val(x,y):
    return pixel_values[int(y), int(x)]

for x in range(width):
    for y in range(height):
        geo_x, geo_y = calc_geoxy(x, y)
        lat,long = calc_latlong(geo_x, geo_y)
        pixel_val = get_pixel_val(x,y)
        data_points.append({"x":geo_x, "y":geo_y, "lat":lat, "long":long, "value":pixel_val})

#used information from following link for writing data to csv file
#https://realpython.com/python-csv/

with open(args.path_to_output_csv_file, mode='w') as csv_file:
    fieldnames = ['lat', 'long', 'value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data_point in data_points:
        writer.writerow({'lat': data_point.get("lat"), 'long': data_point.get("long"), 'value': data_point.get("value")})

print("Tiff Dimensions: {} x {}\nHighest value: {} and Lowest value: {}".format(width,height,pixel_values.max(),pixel_values.min()))
print("Successfully exported {} data points to CSV file".format(len(data_points)))