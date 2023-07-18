import pandas as pd
import geopandas as gpd

csv_data = pd.read_csv('new_data.csv')

geojson_data = gpd.read_file('denver.geojson')

# Merge the two data sets based on a common column
merged_data = geojson_data.merge(csv_data, how='left', left_on='name', right_on='Neighborhood')

merged_data.to_file('merged_data.geojson', driver='GeoJSON')
