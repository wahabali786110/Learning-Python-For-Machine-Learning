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
mask=((movies['genres'].str.contains('Action'))  & (movies['imdb_rating']>7.5))
print(movies[mask][['genres','title_x','imdb_rating']])



