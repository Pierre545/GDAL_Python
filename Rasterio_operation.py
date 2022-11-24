path_RGB_L1C = '/media/pierreaudisio/Maxtor/OGS/Sentinel-2 _ Data/Images_Jupyter_Notebook/L1C_RGB_20170402.tif' 

RGB_L1C = rasterio.open(path_RGB_L1C)

array_L1C = RGB_L1C.read([1,2,3])


#%%

import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Open the file:
raster = rasterio.open('path/to/your/image/m_3511642_sw_11_1_20140704.tif')

# Normalize bands into 0.0 - 1.0 scale
def normalize(array):
    array_min, array_max = array.min(), array.max()
    return (array - array_min) / (array_max - array_min)

# Convert to numpy arrays
nir = raster.read(4)
red = raster.read(3)
green = raster.read(2)

# Normalize band DN
nir_norm = normalize(nir)
red_norm = normalize(red)
green_norm = normalize(green)

# Stack bands
nrg = np.dstack((nir_norm, red_norm, green_norm))

# View the color composite
plt.imshow(nrg)

#%%

import rasterio
from rasterio.plot import show
src = rasterio.open("path/to/your/image/m_3511642_sw_11_1_20140704.tif")

show(src)
