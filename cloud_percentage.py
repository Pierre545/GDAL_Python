#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:28:20 2023

@author: pierreaudisio
"""

import os
from zipfile import ZipFile
from zipfile import BadZipFile


# Repository containing the product folder
directory = "/media/pierreaudisio/Maxtor/IRD/Sentinel2/Nouvelle_Calédonie"
folders = os.listdir(directory)

#Extracting from zip file utf-8, the xml file
n = 0
cloud_percent= {}

for i in folders:
    directory_zip = directory + "/" + i

    try:
        with ZipFile(directory_zip) as myzip:
            a = ZipFile.namelist(myzip)
            file_xml = a[0] 
            file_xml = file_xml[:48] + "/" + file_xml[:48] + "_MTD_ALL.xml"
            
            with myzip.open(file_xml) as myfile:
                _xml = (myfile.read())

# Searching cloud percentage on xml file
                cloud_file = _xml.decode("utf-8")
                position = cloud_file.find("CloudPercent")
                cloud_percent[directory_zip[61:]] = cloud_file[position+14:position+16]
                n += 1

# Using except to avoid inturreption of the processing because of a corrupt file
    except BadZipFile:
            print("Error with:  ",directory_zip)
            
            
            
                
