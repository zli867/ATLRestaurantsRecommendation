# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 23:00:56 2020

@author: lzx3x3
"""
import pandas as pd
df = pd.read_json (r'restaurant_atl.json')
df.to_csv (r'restaurant.csv', index = None)