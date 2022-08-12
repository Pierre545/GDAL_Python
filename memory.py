#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:43:50 2022

@author: pierreaudisio
"""

# Check how much memory a python program is using

import tracemalloc
tracemalloc.start()

#
# code to test here
#

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**3}KB; Peak was {peak / 10**3}KB; Diff = {(peak - current) / 10**3}KB")
tracemalloc.stop()


#%%

#clean the Garbage Collector to release unreferenced memory 
import gc
del my_object
gc.collect()


#%%

class MyClass:
  name = "John"

del MyClass
