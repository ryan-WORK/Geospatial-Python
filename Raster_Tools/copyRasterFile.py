from osgeo import gdal
from osgeo import gdalconst
import sys

def main():
    driver = gdal.GetDriverByName('HFA')
#    driver = gdal.AllRegister()
#    gdal.AllRegister()

    file_path_input = './mydata/n33w118_Img/imgn33w118_13.img'
#    file_path_input = str(fIN)
    dataset_input = gdal.Open(file_path_input, gdalconst.GA_ReadOnly)

    if dataset_input is None:
        print("Error: Cant Loate the File %s" % file_path_input)
        sys.exit()
    else:
        print("Located File & ready to copy a NEW raster FROM: [ %s ] " % file_path_input)

    file_path_out = './OUTPUT/out_dem_copy.img'
    dataset_output = driver.CreateCopy(file_path_out, dataset_input, 0)

    dataset_output = None
    dataset_input = None
    print("Data Set is Flushed")
    print("Process is DONE check the OUTPUT Folder(copy)")




print(main())
