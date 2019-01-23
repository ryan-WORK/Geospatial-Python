# Print out the information that would be used in a postgis db
import sys
from osgeo import gdal
from osgeo import ogr
def main():
    R1 = open("./output/shapefileREADER.txt", 'a')
    cnt = ogr.GetDriverCount()
    formatList = []

    for i in range(cnt):
        driver = ogr.GetDriver(i)
        driverName = driver.GetName()
        if not driverName in formatList:
            formatList.append(driverName)

    formatList.sort()
    for i in formatList:
        print(i)

    driver = ogr.GetDriverByName('ESRI Shapefile')
    print('ESRI Shapefile Drver IN USE')
    R1.write('ESRI Shapefile Drver IN USE')
    data_FilePath = ('./mydata/inputs/GAS_STATIONS.shp')
    R1.write('./mydata/inputs/GAS_STATIONS.shp')
    datasource = driver.Open(data_FilePath, 0)
    if datasource is None:
        print('Error: Cant do that dude')
        sys.exit(1)
    else:
        print("File Located")

    layer = datasource.GetLayer()
    numFeatures = layer.GetFeatureCount()
    extent = layer.GetExtent()
    print('Number of features: %s\n' % numFeatures)
    print('Extent:', extent)
    print('Upper Right')
    print(extent[0])
    print(extent[3])
    print('Upper Left')
    print(extent[1])
    print(extent[2])
    feature = layer.GetNextFeature()
    while feature:
        name = feature.GetField('Name')
        geom = feature.GetGeometryRef()
        print(name, geom.GetX(), geom.GetY(), geom.GetGeometryName())
        feature.Destroy()
        feature = layer.GetNextFeature()
    datasource.Destroy()
    print("Process is Done")
    R1.write("E = 0-4")
    R1.write(str(extent))
    R1.write("# Features")
    R1.write(str(numFeatures))
    R1.close()



main()
