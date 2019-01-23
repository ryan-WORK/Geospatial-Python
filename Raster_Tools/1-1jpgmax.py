import sys
import time
from osgeo import gdal
from osgeo import gdalconst


def jpgInfo():
    gdal.UseExceptions()
    try:
        driver = gdal.GetDriverByName('JPEG')
        driver.Register()
        file_path = ('./mydata/SDSU_3Color.jpg')
        dataset = gdal.Open(file_path, gdalconst.GA_ReadOnly)
        print('Data*****************************************')
    except RuntimeError:
        print("No Data & Exit Program")
        sys.exit(1)

    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    bands = dataset.RasterCount



    print ('Driver: ', dataset.GetDriver().ShortName,'/', \
            dataset.GetDriver().LongName)
    print ('Size is ',dataset.RasterXSize,'x',dataset.RasterYSize, \
          'x',dataset.RasterCount)
    print ('Projection is ',dataset.GetProjection())

    geotransform = dataset.GetGeoTransform()
    if not geotransform is None:
            print ('Origin = (',geotransform[0], ',',geotransform[3],')')
            print ('Pixel Size = (',geotransform[1], ',',geotransform[5],')')

    for band in range(bands):
        band +=1
        print("[GETTING BAND ]:", band)
        sb = dataset.GetRasterBand(band)
        if band is None:
            continue

        stats = sb.GetStatistics(True, True)
        if stats is None:
            continue

        print("[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % (stats[0], stats[1], stats[2], stats[3] ))
        print('Line *************************************************************')


band = None
dataset = None

print(jpgInfo())
