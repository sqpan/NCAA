__author__ = 'weiyushen'

import pandas as pd
import os

path = '/Users/weiyushen/Documents/Fordham/NCAA/data'

os.chdir(path)

#regular season data
reg_season = pd.read_csv('RegularSeasonDetailedResults.csv')

#post season data
post_season = pd.read_csv('TourneyDetailedResults.csv')

#get columns
col = reg_season.columns

#team names Library
team_name_library_csv = pd.read_csv('Teams.csv')
team_name_library = {}
for i in range(0, len(team_name_library_csv)):
    tmp = team_name_library_csv.iloc[i]
    team_name_library[tmp[1]] = tmp[0]


#get one team's data function
def getOneTeam(team_name):
    #team_name = 'Arkansas'
    team_id = team_name_library[team_name]

    result = pd.DataFrame(columns=col)

    #get regular season data
    for i in range(0, len(reg_season)):
        tmp = reg_season.iloc[i]
        if team_id == tmp['Wteam'] or team_id == tmp['Lteam']:
            result = result.append(tmp, ignore_index=True)

    #get post season data
    for i in range(0, len(post_season)):
        tmp = post_season.iloc[i]
        if team_id == tmp['Wteam'] or team_id == tmp['Lteam']:
            result = result.append(tmp, ignore_index=True)


    file_name = team_name + '.csv'
    save_path = '/Users/weiyushen/Documents/Fordham/NCAA/data/team_data'
    os.chdir(save_path)
    result.to_csv(file_name, index=False)
    os.chdir(path)
    print team_name, "finished"


#iterate team names
for i in range(0, len(team_name_library_csv)):
    tmp = team_name_library_csv.iloc[i]
    getOneTeam(tmp[1])

