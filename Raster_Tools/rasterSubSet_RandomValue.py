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
#   Start Here to create the new Raster file Data base!
    cols = dataset_input.RasterXSize
    rows = dataset_input.RasterYSize
    bands = dataset_input.RasterCount
    # the above are called without the (); they are methods.
    projection = dataset_input.GetProjection()
    metadata = dataset_input.GetMetadata()
    datatype = gdal.GetDataTypeName(dataset_input.GetRasterBand(1).DataType)
    nodataval = dataset_input.GetRasterBand(1).GetNoDataValue()
    geotransform = dataset_input.GetGeoTransform()

    #   Start the output of the new file created!
    file_path_out = './OUTPUT/out_dem_CREATE3.img'
    dataset_output = driver.Create(file_path_out, 1024, 1024, bands, gdal.GDT_Float32)

    for i in range(bands):
        band = dataset_input.GetRasterBand(i+1)
        out_band = dataset_output.GetRasterBand(i+1)

        #COPY all data into new file
        data = band.ReadAsArray(0, 0, 1024, 1024)

#        random_data = randomize_2d_array(data)

        import random
        import numpy as np

        def randomize_2d_array(ary2D, min=0.0, max=1.0):
            res2d = np.empty(ary2D.shape)
            try:
                for i in range(ary2D.shape[0]):
                    rows = ary2D[i]
                    for j in range(rows.size):
                        res2d[i,j] = ary2D[i,j] + random.uniform(min, max)
            except Exception as e:
                    print(e)
            return res2d

        random_data = randomize_2d_array(data)
        out_band.WriteArray(random_data, 0, 0)
        out_band.SetNoDataValue(nodataval)
        band=None
        out_band=None

    dataset_output.SetProjection(projection)
    dataset_output.SetGeoTransform(geotransform)
    dataset_output.SetMetadata(metadata)

    dataset_output = None
    dataset_input = None
    print("Data Set is Flushed")
    print("Process is DONE check the OUTPUT Folder(3)")

print(main())
