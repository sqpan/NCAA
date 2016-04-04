__author__ = 'weiyushen'

import pandas as pd
import os
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk('/Users/weiyushen/Documents/Fordham/NCAA/data/team_data'):
    f.extend(filenames)
    break

#team names Library
os.chdir('/Users/weiyushen/Documents/Fordham/NCAA/data/')

team_name_library_csv = pd.read_csv('Teams.csv')
team_name_library = {}
for i in range(0, len(team_name_library_csv)):
    tmp = team_name_library_csv.iloc[i]
    team_name_library[tmp[1]] = tmp[0]


col = ['fgm', 'fga', 'fgm3', 'fga3', 'ftm', 'fta', 'or', 'dr', 'ast', 'to', 'stl', 'blk', 'pf']

def process_one_team(teamname):
    data = pd.read_csv(teamname)
    teamId = team_name_library[teamname[:-4]]
    res = [0] * len(col)

    for j in range(0, len(data)):
        #calculate parameters
        if data.iloc[j]['Wteam'] == teamId:
            start = 8
        else:
            start = 21
        p = 8.0 / (8.0 + data.iloc[j]['Numot'])

        for i in range(start, start + len(col)):
            res[i - start] = res[i - start] + data.iloc[j][data.columns[i]] * p

    for i in range(0, len(res)):
        res[i] = res[i] / len(data)

    return res

for i in range(1, len(f)):
    os.chdir('/Users/weiyushen/Documents/Fordham/NCAA/data/team_data')
    data = process_one_team(f[i])
    result = pd.DataFrame([data], columns=col)
    fName = f[i][:-4] + '.csv'

    os.chdir('/Users/weiyushen/Documents/Fordham/NCAA/data/TeamAvg')
    result.to_csv(fName, index=False)
    print f[i][:-4], 'is finished'





