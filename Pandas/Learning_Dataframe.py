import pandas as pd
import numpy as np

# Dataframe: Any tabular data.
# 1. Ways to create it
# List:
students_list=[
    [100,95,10],
    [80,90,12],
    [70,50,2],
    [85,78,9]
]

students=pd.DataFrame(students_list,columns=['iq','marks','package'])
# print(students)

# Dictionary:
# students_dict={
#     'iq':[100,80,70,85],
#     'marks':[95,90,50,78],
#     'package':[10,12,2,9]
# }

# from_dict=pd.DataFrame(students_dict)
# print(from_dict)

# From datasets:
movies=pd.read_csv('movies.csv')

ipl_matches=pd.read_csv('ipl-matches.csv')

# Attribues and Methods of DataFrame:
#1: dtypes, index, shape, columns, values
# print(movies.dtypes)
# print(ipl_matches.index)
# print(movies.shape)
# print(ipl_matches.columns)
# print(movies.values)

# 2: Head and Tail, Sample, info, describe, rename
# print(movies.head(10))
# print(ipl_matches.tail(10))
# print(movies.sample(5))
# print(ipl_matches.info())
# print(movies.info())
# print(ipl_matches.describe())
# students.rename(columns={'marks':'percent','package':'LPA'},inplace=True) 
# # If we make inplace true it will make permanent changes in the original dataframe permanently
# print(students)

# Filetering DataFrame:
# 1. find all the final winners from ipl
# mask=ipl_matches['MatchNumber']=='Final'
# new_df=ipl_matches[mask]
# print(new_df[['City','Season','WinningTeam']])

# 2. How many superover finishes have occured
# no_of_matches_with_superover=(ipl_matches['SuperOver']=='Y').sum()
# print(no_of_matches_with_superover)

# 3. how many matches has csk won in kolkata
# mask=(ipl_matches['WinningTeam']=='Chennai Super Kings') & (ipl_matches['City']=='Kolkata')
# new_df=ipl_matches[mask]
# print(new_df[['WinningTeam','City']])

# 4. Toss winner is match winner in percentage
# mask=(ipl_matches['TossWinner']==ipl_matches['WinningTeam'])
# new_df=ipl_matches[mask]
# print((new_df.shape[0]/ipl_matches.shape[0])*100)
# # print((len(new_df.index)/len(ipl_matches.index))*100)

# 5. Movies with rating higher than 8 and votes>10000
# mask=(movies['imdb_rating']>8) & (movies['imdb_votes']>10000)
# print(movies[mask][['title_x','imdb_rating','imdb_votes']].shape[0])

# 6. Action movies with rating higher than 7.5
# mask=((movies['genres'].str.split('|').apply(lambda x:'Action' in x))  & (movies['imdb_rating']>7.5))
# Second way:
# mask=((movies['genres'].str.contains('Action'))  & (movies['imdb_rating']>7.5))
# print(movies[mask][['genres','title_x','imdb_rating']])


# Important dataframe methods:

# value_counts(), sort_values(), rank(), sort_index(), set_index(), reset_index(), Rename(), unique(),nunique(), dropna(),drop_duplicates()
# apply()

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]
        
    }
)

# print(students.sort_values('name',na_position='first'))

# Way to sort on the basis of 2 columns
# print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False])[['title_x','year_of_release']].head())

# Rank:
batsman=pd.read_csv('batsman_runs_ipl.csv')
batsman['batsman_rank']=batsman['batsman_run'].rank(ascending=False)
# print(batsman.sort_values('batsman_rank'))

# Set index(), Reset Index():
batsman.set_index('batter',inplace=True)
# print(batsman)

# We use reset to change the index without loosing any column
# print(batsman.reset_index().set_index('batsman_rank'))
# print(batsman)

# rename(): # Can rename index and column names
movies.set_index('title_x',inplace=True) 
movies.rename(columns={'imdb_id':'imdb','poster_path':'links'},inplace=True)
movies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'},inplace=True)
# print(movies)

# unique(),nunique()
# Unique finds all the unique values in a specific series or column and returns a numpy array
# print(ipl_matches['Season'].unique())

# nUnique returns the no: of unique values in a specific column or series. It ignores the NaN values
# And if we make dropna False i will also count the nan value 
# print(ipl_matches['Season'].nunique())
# print(students['cgpa'].nunique(dropna=False))

# dropna():
# print(students['name'].dropna())

# print(students.dropna())

# print(students.dropna(how='all'))

# print(students.dropna(subset=['name','college']))

# last match played by vk in Delhi (Usage of drop_duplicates on dataframe)
ipl_matches['all players']=ipl_matches['Team1Players']+ipl_matches['Team2Players']

def did_kohli_play(players_list):
    return 'V Kohli' in players_list

ipl_matches['did_kohli_play']=ipl_matches['all players'].apply(did_kohli_play)
mask=(ipl_matches['City']=='Delhi') & (ipl_matches['did_kohli_play']==True)
# print(ipl_matches[mask].drop_duplicates(subset=['City','did_kohli_play'],keep='first'))

# apply()
points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)

def euclidean_distance(row):
    point_A=row['1st point']
    point_B=row['2nd point']

    return ((point_A[0]-point_B[0])**2 + (point_A[1]-point_B[1])**2)**0.5

points_df['euclidean_distance']=points_df.apply(euclidean_distance,axis=1)
print(points_df)





