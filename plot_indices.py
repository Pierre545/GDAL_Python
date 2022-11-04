#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:25:12 2022

@author: pierreaudisio
"""

from matplotlib import pyplot as plt
import numpy as np
import csv
import pandas as pd

filename = '/valeurs_indices.csv'

df = pd.read_csv(filename)
print(df.to_string()) 

#%%
# Affichage des indices normalisés

df = pd.read_csv(filename)
# copy the data
df_max_scaled = df.copy()

# apply normalization techniques on Column 
for i in range (1,len(df.columns)):
    column = df.columns[i]
    df_max_scaled[column] = df_max_scaled[column] /df_max_scaled[column].abs().max()
 
# view normalized data
df_max_scaled.plot(kind='line', subplots=True, grid=True, title="2018_01_04 T58KEC",
        layout=(4, 3), sharex=True, sharey=False, legend=True,    
        style=['b-*', 'b-*', 'b-*', 'b-*', 'g-*', 'g-*', 'g-*',
               'g-*', 'y-*', 'r-*', 'g-*', 'r-*'],
        xticks=np.arange(10), yticks=np.arange(-1,1.2,0.2))
#a =df["Nom"].to_list()
a = ['0_Foret','1_Mangrove', '2_Mangrove','3_Pont','4_Embouchure','5_Embouchure','6_Mangrove','7_Mangrove','8_Plage','9_Ocean']
plt.gcf().text(0.5,0.04,a, ha="center")
