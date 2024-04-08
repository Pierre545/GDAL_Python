#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:50:29 2022

@author: pierreaudisio
"""

from osgeo import gdal
import numpy as np
import osr

path = ""

ds = gdal.Open(path)
array = ds.ReadAsArray() 


def array_to_raster(raster, array):
    
    dst_filename = '/home/pierreaudisio/Bureau/Mangrove/test.tif'
    
    
    # Top left corner coordinate and resolution of the array
    GT0, GT1, GT2, GT3, GT4, GT5 = ds.GetGeoTransform()
    
    nrows,ncols = np.shape(array)
    
    # Transformation from the image coordinate space, to the georeferenced coordinate space 
    geotransform=(GT0, GT1, GT2, GT3, GT4, GT5)   
    
    # Open the file
    driver = gdal.GetDriverByName('GTiff')
    output_raster = driver.Create(dst_filename, ncols, nrows, 1 ,gdal.GDT_Float32)
    
    # Specify its coordinates
    output_raster.SetGeoTransform(geotransform)
    
    # Establish its coordinate encoding
    src = osr.SpatialReference() 
    src.ImportFromEPSG(3163)

    # Exports the coordinate system to the file
    output_raster.SetProjection( src.ExportToWkt() ) 
    
    # Writes my array to the raster
    output_raster.GetRasterBand(1).WriteArray(array)
    
    # Write to disk.
    output_raster.FlushCache()  
    
    return output_raster.GetRasterBand(1) 

#%%
    def raster2array(raster, array, outpath, OutPutName):

    # Write to TIFF
    kwargs = raster.meta
    kwargs.update(dtype=rasterio.float32, count=1, compress='lzw')

    with rasterio.open(os.path.join(outpath, str(OutPutName) + '.tif'), 'w', **kwargs) as dst:
        dst.write_band(1, tensor.astype(rasterio.float32))

    return ()
