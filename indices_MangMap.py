
NDVI = (array_B08-array_B04)/(array_B08+array_B04)

NDWI1 = (array_B03-array_B08)/(array_B03+array_B08)

NDWI2 = (array_B08-array_B11)/(array_B08+array_B11)

MNDWI1 = (array_B03-array_B11)/(array_B03+array_B11)

MNDWI2 = (array_B03-array_B12)/(array_B03+array_B12)

NDRE = (array_B07-array_B05)/(array_B07+array_B05)
NDRE_MangMap = (array_B08-array_B05)/(array_B08+array_B05)

BIGR = ((array_B03**2 + array_B04**2) / 2)**(0.5)  

SAVI = (array_B08 - array_B04)*1.5 / (array_B08 + array_B04 + 0.5)

CMRI = ((array_B08 - array_B04) / (array_B08 + array_B04)) - ((array_B03 - array_B08) / (array_B03 + array_B08))

MVI = (array_B08 - array_B03) / (array_B11 - array_B03)

EVI = 2.5*(array_B08 - array_B04) / (array_B08 + 6*array_B04 - 7.5*array_B02 + 1)

IRECI = (array_B07 - array_B04) / (array_B05 / array_B06)
