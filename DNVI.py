#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:17:47 2022

@author: pierreaudisio

Calcul de l'indice DNVI (Manna et Raychaudhuri 2020)

"""

from osgeo import gdal
import numpy as np
from raster2array import *


#Importation des bandes 11 et 12 de Sentinel2
path_SWIR1 = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/Nouvelle-Calédonie/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0_FRE_B11.tif'
path_SWIR2 = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/Nouvelle-Calédonie/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0_FRE_B12.tif'


ds_SWIR1 = gdal.Open(path_SWIR1)
array_SWIR1 = ds_SWIR1.ReadAsArray() 

ds_SWIR2 = gdal.Open(path_SWIR2)
array_SWIR2 = ds_SWIR2.ReadAsArray() 


#Calcul de l'indice DNVI
array_DNVI = (array_SWIR1-array_SWIR2)**2/(array_SWIR1+array_SWIR2)**(1/2)


#Sauvegarde de l'indice DNVI
raster = ds_SWIR1
dir_folder = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/Nouvelle-Calédonie/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/Projet_mangrove'

dst_filename = dir_folder+'/'+'DNVI'
array_to_raster(raster, array_DNVI, dst_filename)


    