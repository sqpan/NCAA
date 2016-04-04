__author__ = 'shaoqing'

import pandas as pd
import os

path = '/Users/ShaoqingPan/Desktop/Semester 3/Fusion/Project/Data'

os.chdir(path)

#post season data
post_season = pd.read_csv('TourneyDetailedResults.csv')

#seed table
seed_table = pd.read_csv('TourneySeeds.csv')

col = ['w_seed', 'l_seed']
res = pd.DataFrame(columns=col)


for i in range(0, len(post_season)):
#for i in range(0, 10):
    tmp = post_season.iloc[i]

    season = tmp['Season']
    w_team = tmp['Wteam']
    l_team = tmp['Lteam']

    print season, w_team, l_team

    b = [-1,-1]

    for j in range(0, len(seed_table)):
        table = seed_table.iloc[j]


        if season == table['Season'] and w_team == table['Team']:
            a = table['Seed']
            b[0] = int(a[1:3])

        if season == table['Season'] and l_team == table['Team']:
            a = table['Seed']
            b[1] = int(a[1:3])


    newA = pd.DataFrame(data=[b], columns=col)
    res = res.append(newA)

print res
res.to_csv('tmp.csv', index = False)


