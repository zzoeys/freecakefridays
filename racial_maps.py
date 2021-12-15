import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

geoData = "tl_2020_us_county.shp"
map_geo = gpd.read_file(geoData)
# check the GeoDataframe
map_geo.head()

final=map_geo.loc[map_geo['STATEFP']=='13']

final.plot()

plt.rcParams['figure.figsize'] = [15, 10] #height, width
final.plot()

race =  pd.read_csv("./racial_distribution.csv")
race

race.GEO_ID=race['GEO_ID'].str.slice(start=-5)
race

# join the geodataframe with the csv dataframe
merged = final.merge(race, how='left', left_on="GEOID", right_on="GEO_ID")
merged = merged[['GEOID', 'geometry', 'NAMELSAD', 'P1_003N']]
merged

# set the value column that will be visualised
variable = 'P1_003N'
# set the range for the choropleth values
vmin, vmax = 0, 100
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
ax.axis('off')
# add a title and annotation
ax.set_title('White Choropleth Map', fontdict={'fontsize': '25', 'fontweight' : '3'})
#ax.annotate('Source: Wikipedia - https://en.wikipedia.org/wiki/Provinces_of_Indonesia', xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='#555555')
# Create colorbar legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm.set_array([]) # or alternatively sm._A = []. Not sure why this step is necessary, but many recommends it
# add the colorbar to the figure
fig.colorbar(sm)
# create map
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
