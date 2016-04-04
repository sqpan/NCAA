__author__ = 'weiyushen'

import pandas as pd
import os
import csv

path = '/Users/weiyushen/Documents/Fordham/NCAA/data'

os.chdir(path)

tmp_seed = pd.read_csv('tmp_seed.csv')

res = []

for i in range(0, 16):
    b = [0] * 16
    res.append(b)

for i in range(0, len(tmp_seed)):
    tmp = tmp_seed.iloc[i]
    m = int(tmp['w_seed']) - 1
    n = int(tmp['l_seed']) - 1
    res[m][n] = res[m][n] + 1


panda = pd.DataFrame(data = [res[0]])
for i in range(1, 16):
    tmp = pd.DataFrame(data = [res[i]])
    panda = panda.append(tmp)

print panda
panda.to_csv('panda.csv', index=False)
