import os, sys, time, gdal
from gdalconst import *

startTime = time.time()
xValues = [-117.119288]
yValues = [32.733004]

file_path = ("./mydata/n33w118_Img/imgn33w118_13.img")
dataset = gdal.Open(file_path, GA_ReadOnly)
gdal.AllRegister()

if dataset is None:
    print("No data located in the path")
    sys.exit(1)
else:
    print("Data is Located")


rows = dataset.RasterYSize
cols = dataset.RasterXSize
bands = dataset.RasterCount

geotransform = dataset.GetGeoTransform()
xOrigin = geotransform[0]
yOrigin = geotransform[3]
pixelW = geotransform[1]
pixelH = geotransform[5]

for i in range(1):
    x = xValues[i]
    y = yValues[i]

    xOffset = int((x-xOrigin)/ pixelW)
    yOffset = int((y-yOrigin)/ pixelH)

    s = str(x) + '=X  ' + str(y) + '=Y ' + str(xOffset) + '=xOffset ' + str(yOffset) + '=yOffset '

    for j in range(bands):
        band = dataset.GetRasterBand(j+1)
        data = band.ReadAsArray(xOffset, yOffset, 1, 1)
        value = data[0,0]
        s = s + str(value) + '=Value of Elevation '
    print("Answer")
    print(s)
endTime = time.time()
print("the script took" + str(endTime - startTime) + ' seconds')
