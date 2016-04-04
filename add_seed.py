# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:42:07 2016

@author: ShaoqingPan
"""

import pandas as pd
import os
import numpy as np

path = '/Users/ShaoqingPan/Desktop/Semester 3/Fusion/Project/Data'
os.chdir(path)

os.system('cls')
post_data = pd.read_csv('TourneyCompactResults.csv')
seed = pd.read_csv('TourneySeeds.csv')

#print seed.iloc[1,'Season']
#print post_data.iloc[1,'Season']
print seed.loc[1,:]
print post_data.loc[1,:]

#for i in range(0,len(post_data)):
#    if post_data.loc[i,] == post_data[1] and   