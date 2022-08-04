#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:57:57 2022

@author: pierreaudisio
"""

import numpy as np

def bin(a,sup,egal_sup):
    
    r,c = np.shape(a)
    bin_array = np.copy(a)

    if(egal_sup!=99999):
        for i in range(r):
            for j in range(c):
                if (bin_array[i,j]>=egal_sup):
                    bin_array[i,j] = 1
                else:
                    bin_array[i,j] = 0
                    
                    
    else:
        for i in range(r):
            for j in range(c):
                if (bin_array[i,j]>sup):
                    bin_array[i,j] = 1
                else:
                    bin_array[i,j] = 0
                    
    return(bin_array)