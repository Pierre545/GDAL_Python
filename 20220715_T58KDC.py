#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 08:33:45 2022

@author: pierreaudisio

Chaine de traitement pour l'estimation de l'emprise de la mangrove sur la tuile T58KDC du 15/07/2022
"""



from osgeo import gdal
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import cv2
from PIL import Image
import time 
import scipy.ndimage
import osr
import cv2
from raster2array import *
from fct_replace import *
from bin_fct import *

#%%
#Chemins dirigéant vers les différentes variables 
path_SWIR = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0_FRE_B11.tif'
path_B03 = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0_FRE_B3.tif'
path_B04 = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0_FRE_B4.tif'
path_B08 = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0_FRE_B8.tif'
path_CARNAMA = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/CARNAMA_ROI.tif'


#%%
#Importation des objets associés

ds_SWIR = gdal.Open(path_SWIR)
array_SWIR = ds_SWIR.ReadAsArray() 

ds_B03 = gdal.Open(path_B03)
array_B03 = ds_B03.ReadAsArray() 

ds_B04  = gdal.Open(path_B04)
array_B04 = ds_B04.ReadAsArray() 

ds_B08  = gdal.Open(path_B08)
array_B08 = ds_B08.ReadAsArray() 

ds_CARNAMA = gdal.Open(path_CARNAMA)
array_CARNAMA = ds_CARNAMA.ReadAsArray() 
    

#%%
# Changement de résolution 

# Resampled by a factor of 2 with nearest interpolation
array_SWIR = scipy.ndimage.zoom(array_SWIR, 2, order=0)


# # Resampled by a factor of 2 with bilinear interpolation
# print (scipy.ndimage.zoom(array, 2, order=1))


# # Resampled by a factor of 2 with cubic interpolation
# print( scipy.ndimage.zoom(array, 2, order=3))


#%%
# Calcul des indices NDVI et NDWI2

NDVI = (array_B08-array_B04)/(array_B08+array_B04)
NDWI2 = (array_B03-array_B08)/(array_B03+array_B08)

# invalid value encountered in true_divide == np.NaN


#%%
#Remplacement des NaN value par 0
r,c = np.shape(NDVI_NDWI2_bin)
for i in range(r):
    for j in range(c):
        if (NDVI_NDWI2_bin[i,j]>1):
            NDVI_NDWI2_bin[i,j] = 1
            
        if (array_CARNAMA[i,j]>0):
            array_CARNAMA[i,j]=1
            
NDVI = replace(np.NaN,0,NDVI)
            
            
#%%
# Binarisation du NDVI et du NDWI2

r,c = np.shape(NDVI)

NDVI_bin = bin(NDVI,0,0.3)
NDWI2_bin = bin(NDWI2,0,99999) 


#%%
# Application des masks NDVI et NDWI2 sur la bande11, sur la zone d'intéret choisis par l'utilisateur.

#Création d'un mask binaire commun entre NDVI, NDWI2 et CARNAMA

NDVI_NDWI2_bin = NDVI_bin + NDWI2_bin 

NDVI_NDWI2_bin = bin(NDVI,1,99999)
array_CARNAMA = bin(array_CARNAMA,0,99999)

array_SWIR_Mask = np.copy(array_SWIR)
array_SWIR_Mask = array_SWIR_Mask * NDVI_NDWI2_bin


#%%
# Détermination des Q1 et Q99 sur l'emprise de référence (concaténation des 4 vecteurs trimestriel de l'année précédente)
# On utilise ici comme emprise de référence initial celle fournit par CARNAMA

array_SWIR_Mask_ROI = array_SWIR_Mask*array_CARNAMA

array_SWIR_Mask_ROI = replace(0,np.NaN,array_SWIR_Mask_ROI)

#%%
Q1 = np.nanquantile(array_SWIR_Mask_ROI, .1)
Q99 = np.nanquantile(array_SWIR_Mask_ROI, .99)


#%%
#Application du seuillage Q1 et Q99 sur la zone d'interet choisis (array_SWIR_Mask * [ROI +buffer])

#Application du buffer
kernel = np.ones((20,20), np.uint8)
array_CARNAMA_buffer = cv2.dilate(array_CARNAMA, kernel, iterations=1)

array_SWIR_Mask_ROI = array_SWIR_Mask * array_CARNAMA_buffer

#Application du seuillage
r,c = np.shape(array_SWIR_Mask_ROI)
for i in range(r):
    for j in range(c):
        if (array_SWIR_Mask_ROI[i,j]<Q1):
            array_SWIR_Mask_ROI[i,j] = 0
            
        elif (array_SWIR_Mask_ROI[i,j]>Q99):
            array_SWIR_Mask_ROI[i,j] = 0


#%%
#Replace 0 by NaN

r,c = np.shape(array_SWIR_Mask_ROI)
for i in range(r):
    for j in range(c):
        if (array_SWIR_Mask_ROI[i,j]==0):
            array_SWIR_Mask_ROI[i,j] = np.NaN


#%%
#

r,c = np.shape(array_CARNAMA_buffer)
for i in range(r):
    for j in range(c):
        if (array_CARNAMA_buffer[i,j]==0):
            array_CARNAMA_buffer[i,j] = np.NaN


#%%
#Sauvegarde du résultat avec la projection correspondante
raster = ds_B08
array = array_SWIR_Mask_ROI

dst_filename = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/Projet_mangrove/array_CARNAMA_buffer'
array_to_raster(raster, array_CARNAMA_buffer, dst_filename)

dst_filename = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/Projet_mangrove/NDVI_NDWI2_bin'
array_to_raster(raster, NDVI_NDWI2_bin, dst_filename)

dst_filename = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/Projet_mangrove/SWIR_MASK'
array_to_raster(raster, array_SWIR_Mask, dst_filename)

dst_filename = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/Projet_mangrove/SWIR_MASK_Threshold'
array_to_raster(raster, array_SWIR_Mask_ROI, dst_filename)


dst_filename = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/Projet_mangrove/NDVI'
array_to_raster(raster,NDVI_bin, dst_filename)

dst_filename = '/home/pierreaudisio/Bureau/Mangrove/SENTINEL-2/SENTINEL2A_20220715-232215-638_L2A_T58KDC_C_V3-0/Projet_mangrove/NDWI2'
array_to_raster(raster, NDWI2_bin, dst_filename)

