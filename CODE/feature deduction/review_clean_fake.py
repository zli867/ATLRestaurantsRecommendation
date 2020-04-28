# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:10:08 2020

@author: lzx3x3
"""

import pandas as pd
import numpy as np

df = pd.read_csv('reviews_of_100_restaurants.csv')

df2 = pd.read_csv('fakedate.csv')
dff = df.merge(df2,how='left', left_on=['biz_id','date'], right_on=['id','fake_date'])
dff = dff.replace({'id':{'':0}})
dff.to_csv('review_100_fake.csv')

