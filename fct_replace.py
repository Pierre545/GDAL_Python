#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:09:38 2022

@author: pierreaudisio
"""

import numpy as np

def replace(x1, x2, array):
    
    r,c = np.shape(array)
    for i in range(r):
        for j in range(c):
            if (array[i,j]==x1):
                array[i,j] = x2
    
    return( array )