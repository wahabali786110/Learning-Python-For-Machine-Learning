import pandas as pd
import numpy as np

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT3D_x_4DS6d51LKJ7ze1sxT5WpV5uiSVOFYHLwBiGru6vFyVv5h5-83AwFjxWYiWfCDjDAaarHAV-k/pub?gid=0&single=true&output=csv"
football = pd.read_csv(url)

# Question 1
# total_teams=football['Team'].unique()
# dict1={}
# for team in total_teams:
#     mask=football['Team']==team
#     total_attempts=football[mask]['Total Attempts'].sum()
#     total_on_target=football[mask]['On Target'].sum()
#     total_percentage=round((total_on_target/total_attempts)*100,2)
#     dict1[team]=float(total_percentage)

# sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
# print(sorted_dict)

# Question 2
total_teams=football['Team'].unique()

# dict1={
#     'Teams':[],
#     'Mathces':[]
# }
# for team in total_teams:
#     mask=(football['Team']==team)
#     total_matches=football[mask]['Team'].size
#     dict1['Teams'].append(team)
#     dict1['Mathces'].append(total_matches)

# new_df=pd.DataFrame(dict1)
# new_df['Rank']=new_df['Mathces'].rank(ascending=False,method='dense')
# print(new_df.sort_values(by='Rank'))

# Question 3:
# print(football.info())
# print(football.describe())
# print(football.isnull().sum())
# football.fillna(football.mean(numeric_only=True), inplace=True)
# football.drop_duplicates(keep='first',inplace=True)
football.drop(columns=['Sl. No','Match No.','Red Cards','Pts'],inplace=True)
# print(football.info())

# Question 4
football['Rank']=football['Team'].rank(method='dense')
football['Rank']=football['Rank'].astype(np.int16)
football.set_index('Rank',inplace=True)
football.sort_index(inplace=True)
# print(football)

# Q5:
# 1.

# url2='https://www.google.com/url?q=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh%2Fpub%3Fgid%3D1562145139%26single%3Dtrue%26output%3Dcsv'
# train=pd.read_csv(url2)
# train.dropna(subset='Age',inplace=True)
# print(train)

# 2.
# train2=pd.read_csv('test - test.csv')
# train2['Age']=train2['Age'].fillna(20)
# print(train2)

# Q6:
ipl_matches=pd.read_csv('ipl-matches.csv')
team_name_changes={
    'Delhi Daredevils':'Delhi Capitals',
    'Kings XI Punjab':'Punjab Kings',
    'Rising Pune Supergiants':'Rising Pune Supergiant'
}

ipl_matches.replace(team_name_changes,inplace=True)

# dict1={
#     'Team Name':[],
#     'Total Matches':[],
#     'Win%':[],
#     'Home Win%':[],
#     'Away Win%':[]
# }
# total_teams=ipl_matches['Team1'].unique()
# ipl_matches.dropna(subset=['WinningTeam'],inplace=True)
# for team in total_teams:
#     mask=(ipl_matches['Team1']==team) | (ipl_matches['Team2']==team)
#     matches_played=mask.sum()

#     mask2=(ipl_matches['WinningTeam']==team)
#     wins=mask2.sum()
#     win_percentage=round((wins/matches_played)*100,2)

#     mask3=(ipl_matches['Team1']==team) & (ipl_matches['WinningTeam']==team)
#     home_wins=mask3.sum()
#     home_win_percentage=round((home_wins/matches_played)*100,2)

#     mask4=(ipl_matches['Team2']==team) & (ipl_matches['WinningTeam']==team)
#     away_wins=mask4.sum()
#     away_win_percentage=round((away_wins/matches_played)*100,2)

#     dict1['Team Name'].append(team)
#     dict1['Total Matches'].append(matches_played)
#     dict1['Win%'].append(win_percentage)
#     dict1['Home Win%'].append(home_win_percentage)
#     dict1['Away Win%'].append(away_win_percentage)

# new_df=pd.DataFrame(dict1)
# new_df.sort_values(by='Win%',inplace=True,ascending=False)
# print(new_df,end="\n\n")

# Q7:
# no_result_venues = ipl_matches[ipl_matches['WonBy'] == 'NoResults']['Venue'].value_counts()

# print(no_result_venues)

# Q8
# final_df=ipl_matches[ipl_matches['MatchNumber']=='Final']
# total_players=pd.concat([final_df['Team1Players'],final_df['Team2Players']])
# final_players=total_players.str.split(',').explode()
# cleaned_players=final_players.str.strip()
# print(cleaned_players.value_counts().head(1))

# Q9:

total_ipl_teams=ipl_matches['Team1'].unique()
match_name_changes = {
    'Elimination Final': 'Eliminator',
    'Preliminary Final': 'Qualifier 2',
   
}


ipl_matches.replace(match_name_changes, inplace=True)

Valid_Seasons=['2022', '2021', '2020/21', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2009/10', '2009', '2007/08']

def point_table(Season):
    dict1={
    'TeamName':[],
    'MatchesPlayed':[],
    'MatchesWon':[],
    'NoResult':[],
    'Points':[],

    }
    
    if Season not in Valid_Seasons:
        return "Please enter a valid Season"
   
    for team in total_ipl_teams:
        mask= (ipl_matches['Season']==Season) & ((ipl_matches['Team1']==team) | (ipl_matches['Team2']==team))
        mask2= (ipl_matches['Season']==Season) & (ipl_matches['WinningTeam']==team)
        mask3= (ipl_matches['Season']==Season) & (((ipl_matches['Team1']==team) | (ipl_matches['Team2']==team)) & (ipl_matches['WonBy']=='NoResults'))

        matches_played = int(mask.sum())
        matches_won = int(mask2.sum())
        no_results = int(mask3.sum())

        points=(matches_won*2)+(no_results*1)
       
        dict1['TeamName'].append(team)
        dict1['MatchesPlayed'].append(matches_played)
        dict1['MatchesWon'].append(matches_won)
        dict1['NoResult'].append(no_results)
        dict1['Points'].append(points)
       


    new_df=pd.DataFrame(dict1)
    new_df=new_df[new_df['MatchesPlayed']>0]
    new_df.sort_values(by=['Points','TeamName'],ascending=[False,True],inplace=True)
    new_df.set_index('TeamName',inplace=True)
    

    new_df_copy=new_df.copy()
    new_df_copy['SeasonPosition']=new_df_copy['Points'].rank(ascending=False,method='dense').astype('int').astype('object')

    final_match=ipl_matches[(ipl_matches['Season']==Season)&(ipl_matches['MatchNumber']=='Final')]
    winner_team_name=final_match['WinningTeam'].iloc[0]
        
    team1=final_match['Team1'].iloc[0]
    team2=final_match['Team2'].iloc[0]
    if team1==winner_team_name:
            runner_up=team2
    else:
            runner_up=team1


    semi_final1=ipl_matches[(ipl_matches['Season']==Season)&(ipl_matches['MatchNumber']=='Qualifier 2')]
    if not semi_final1.empty:
        qualifier_winner_name=semi_final1['WinningTeam'].iloc[0]
        qteam1=semi_final1['Team1'].iloc[0]
        qteam2=semi_final1['Team2'].iloc[0]
        if qteam1==qualifier_winner_name:
                qualifier_loser_name=qteam2
        else:
                qualifier_loser_name=qteam1
        
        new_df_copy.at[qualifier_loser_name,'SeasonPosition']=3


    eliminator=ipl_matches[(ipl_matches['Season']==Season)&(ipl_matches['MatchNumber']=='Eliminator')]
    if not eliminator.empty:
        eliminator_winner_name=eliminator['WinningTeam'].iloc[0]
        eteam1=eliminator['Team1'].iloc[0]
        eteam2=eliminator['Team2'].iloc[0]
        if eteam1==eliminator_winner_name:
                eliminator_loser_name=eteam2
        else:
                eliminator_loser_name=eteam1
        
        new_df_copy.at[eliminator_loser_name,'SeasonPosition']=4

    new_df_copy.at[winner_team_name,'SeasonPosition']='Winner'
    new_df_copy.at[runner_up,'SeasonPosition']='Runner Up'
    
    
    return new_df_copy
    

print(point_table('2007/08'))




