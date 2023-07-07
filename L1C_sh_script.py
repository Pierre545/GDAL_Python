#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:05:18 2023

@author: pierreaudisio
"""

import os
import touch

# Répertoire où se trouvent les fichiers L1C
directory = '/mnt/NasespaceSentinel/Sentinel2/L1C/Caledonie'
folders = os.listdir(directory)

list_L1C = []

for i in folders:
    if str(2022) in i : 
        if not "zip" in i :
            a = "\n" + "/home/pierreaudisio/Sen2Cor-02.11.00-Linux64/bin/L2A_Process" + "  " + directory + "/" + str(i)
            list_L1C.append(a)

touch.touch("L1C_processing.sh")

f = open("L1C_processing.sh","w")
f.writelines(list_L1C)
f.close


#%%

f = open("L1C_processing.sh", "a")
folders = os.listdir('/home/pierreaudisio/Bureau/Mangrove/Franck/L2A_Fidji/KXF')
list_L1C = []
for i in folders:
    a =  "/home/pierreaudisio/Sen2Cor-02.11.00-Linux64/bin/L2A_Process" + " " + path + "/KXF/" +str(i)
    f.writelines(a + "\n")
f.close()

#open and read the file after the appending:
f = open("L1C_processing.sh", "r")
print(f.read())
