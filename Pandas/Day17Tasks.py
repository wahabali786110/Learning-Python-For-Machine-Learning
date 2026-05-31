import pandas as pd
import numpy as np

# Task 1 Q1:
dict1=data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills', 'Cranes'], 
        'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4, 3.5], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2, 2], 
        'priority': ['yes', 'yes', 'no', np.nan, 'no', 'no', 'no', 'yes', 'no', 'no','yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
birds=pd.DataFrame(dict1,index=labels)
# print(birds.info())
# print(birds.describe())
# print(birds.loc['a'::2])

# Q2:

# 1.
# print(birds.loc[birds.index[[0,2,6]],['birds','age']])

# 2.
# mask=birds['visits']<4
# print(birds[mask])

# Q3:

# 1.
mask=(birds['age'].isnull()) | (birds['visits'].isnull())
# print(birds[mask])

# 2.
birds['age']=birds['age'].fillna(birds['age'].mode()[0])
birds['priority']=birds['priority'].fillna(birds['priority'].mode()[0])

# Q4:

# 1.
# mask=birds['birds']=='Cranes'
# print(birds[mask]['visits'].sum())

# # 2.
# unique_birds=birds['birds'].value_counts()
# print(unique_birds)

# # 3.
# print(birds.duplicated().sum())

# # 4.
# birds.drop_duplicates(inplace=True)
# print(birds)

# Task 2 Q1:
ipl_matches=pd.read_csv('ipl-matches.csv')

team_name_changes={
    'Delhi Daredevils':'Delhi Capitals',
    'Kings XI Punjab':'Punjab Kings',
    'Rising Pune Supergiants':'Rising Pune Supergiant'
}

ipl_matches.replace(team_name_changes,inplace=True)


# Q2:
# import matplotlib.pyplot as plt
# total_matches = (ipl_matches['Team1'].value_counts()+ipl_matches['Team2'].value_counts()).sort_values(ascending=False).head(5)
# total_matches.plot(kind='bar')

# plt.title('Top 5 Teams by Total Matches Played')
# plt.xlabel('IPL Teams')
# plt.ylabel('Number of Matches')

# plt.show()

# Q3:
mask=((ipl_matches['Team1']=='Mumbai Indians')|(ipl_matches['Team2']=='Mumbai Indians')) & (ipl_matches['WinningTeam']!='Mumbai Indians')
# print(ipl_matches[mask]['Player_of_Match'].value_counts().head(1))

# Q4:
def team1_vs_team2(team1,team2):
    mask=(ipl_matches['Team1']==team1) & (ipl_matches['Team2']==team2) | (ipl_matches['Team2']==team1) & (ipl_matches['Team1']==team2)
    win_loss_record=ipl_matches[mask]['WinningTeam'].value_counts()
    player_of_match=ipl_matches[mask]['Player_of_Match'].value_counts().head(1)
    return win_loss_record,player_of_match

print(team1_vs_team2('Kolkata Knight Riders','Chennai Super Kings'))



# Q5:
import matplotlib.pyplot as plt
mask=(ipl_matches['Team1']=='Kolkata Knight Riders') | (ipl_matches['Team2']=='Kolkata Knight Riders')
top_cities=ipl_matches[mask]['City'].value_counts().head(7)
top_cities.plot(kind='bar')
# plt.show()

# Q6:
mask=(ipl_matches['WinningTeam']=='Mumbai Indians') & (ipl_matches['Season']=='2011')
# print(ipl_matches[mask]['Margin'].mean())













