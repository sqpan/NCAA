__author__ = 'weiyushen'

import pandas as pd
import os
from os import walk
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

#team names Library
os.chdir('/Users/weiyushen/Documents/Fordham/NCAA/data/')

team_name_library_csv = pd.read_csv('Teams.csv')
team_name_library = {}
for i in range(0, len(team_name_library_csv)):
    tmp = team_name_library_csv.iloc[i]
    team_name_library[tmp[0]] = tmp[1]

#import data
os.chdir('/Users/weiyushen/Documents/Fordham/NCAA/data/Training')

regSeason = pd.read_csv('RegularSeasonDetailedResults.csv')
posSeason = pd.read_csv('TourneyDetailedResults.csv')

def start_learning(season):
    X = []
    Y = []
    for i in range(0, len(season)):
        Y.append(season.iloc[i][season.columns[13]])
        tmp = []
        for j in range(0, 13):
            tmp.append(season.iloc[i][season.columns[j]])
        X.append(tmp)

    #Training Model:
    #clf = tree.DecisionTreeClassifier()
    clf = RandomForestClassifier(n_estimators=100)
    clf = clf.fit(X, Y)
    return clf

def testing(team1_file, team2_file, clf):
    os.chdir('/Users/weiyushen/Documents/Fordham/NCAA/data/TeamAvg')
    team1 = pd.read_csv(team1_file)
    team2 = pd.read_csv(team2_file)

    X = []
    for i in range(0, 13):
        tmp = team1.iloc[0][team1.columns[i]] - team2.iloc[0][team2.columns[i]]
        X.append(tmp)

    #print clf.predict_proba([X])
    return clf.predict([X])

#Main
trained_model = start_learning(posSeason)


f = []
for (dirpath, dirnames, filenames) in walk('/Users/weiyushen/Documents/Fordham/NCAA/data/TeamAvg'):
    f.extend(filenames)
    break

'''
for i in range(0, 9):
    tmp = ''
    for j in range(0, 8):
        if i * 8 + j is not 0 and i * 8 + j <= 68:
            tmp = tmp + f[i * 8 + j][:-4] + '        '
    print tmp

while True:
    team1 = input('input team1: ')
    team2 = input('input team2: ')

    testing(team1 + '.csv', team2 + '.csv', trained_model)
    print
'''

#print testing('Tulsa.csv', 'Temple.csv', trained_model)[0]


#testing
os.chdir('/Users/weiyushen/Documents/Fordham/NCAA/data/')
testingData = pd.read_csv('TourneyDetailedResults.csv')

correct = 0
count = 0

for i in range(1, 848):
    try:
        count = count + 1
        team1 = team_name_library[testingData.iloc[i]['Wteam']]
        team2 = team_name_library[testingData.iloc[i]['Lteam']]
        predict = testing(team1 + '.csv', team2 + '.csv', trained_model)[0]
        if predict == 1.0:
            correct = correct + 1

    except:
        continue

print correct, count
print correct * 100.0 / count, '%'









