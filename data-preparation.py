import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd


# Read csv file to dataframe
race =  pd.read_csv('data/race_data/georgia_race_data.csv',  index_col = 1, skiprows = 1)

pd.options.display.width=None
pd.set_option('max_row', None)
pd.set_option('display.max_rows', race.shape[0] + 1)
pd.set_option('display.expand_frame_repr', False)

race.columns = race.columns.str.lstrip()

race.columns = race.columns.map(str)

race.rename(columns={'!!Total:!!Not Hispanic or Latino:!!Population of two or more races:':'Mixed'}, inplace = True)

race['Others'] = race['!!Total:!!Not Hispanic or Latino:!!Population of one race:!!American Indian and Alaska Native alone'] + race['!!Total:!!Not Hispanic or Latino:!!Population of one race:!!Native Hawaiian and Other Pacific Islander alone'] + race['!!Total:!!Not Hispanic or Latino:!!Population of one race:!!Some Other Race alone']

# Create a new dataframe with the desired columns
race = race[['Geographic Area Name', 'id', '!!Total:', '!!Total:!!Hispanic or Latino', '!!Total:!!Not Hispanic or Latino:!!Population of one race:!!White alone', '!!Total:!!Not Hispanic or Latino:!!Population of one race:!!Black or African American alone','!!Total:!!Not Hispanic or Latino:!!Population of one race:!!Asian alone', 'Mixed', 'Others' ]].copy()

# Rename the columns
race.columns = ['Area Name', 'id', 'Total', 'Hispanic', 'White', 'Black', 'Asian', 'Mixed', 'Others']

georgia_race = race.loc[0]

race.drop([0], inplace=True)

race.to_csv('data/race_data/cleaned_georgia_race_precinct.csv')
georgia_race.to_csv('data/race_data/cleaned_georgia_race_total.csv')