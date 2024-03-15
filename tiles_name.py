#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:01:22 2023

@author: pierreaudisio
"""
from sentinelsat import SentinelAPI

def S2tile_fromLATLON (lat,lon):
    
    USER = "XXX"
    PASSWORD = "XXX"
    
    # query scenes
    api = SentinelAPI(USER, PASSWORD, 'https://scihub.copernicus.eu/dhus')
    
    footprint = 'POINT(%s %s)' % (lon, lat)
    
  
    product = api.query(footprint, 
                    date=('20210101', '20211201'), 
                    platformname='Sentinel-2', 
                    producttype= 'S2MSI1C', 
                    area_relation='Contains',
                    )
    # get tile
    tiles=[]
    for value in product.values():
        tile = value['tileid']
        if len(tiles)==0:
            print(tile)
            tiles.append(tile)
        aux=0
        for j in range(0,len(tiles)):
            if tile==tiles[j]:
                aux=1
        if aux==0:
            print(tile)
            tiles.append(tile)
              
    return tiles
