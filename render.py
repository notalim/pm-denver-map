import folium
import webbrowser
import os
import pandas as pd
import geopandas as gpd
import numpy as np

# Load the GeoJSON file
denver_geojson = r'merged_data.geojson'  # replace this with your actual file path

# Load the data from merged GeoJSON
data = gpd.read_file(denver_geojson)

# Convert 'Average Household Income' to numeric values (removing commas and dollar sign)
data['Average Household Income'] = data['Average Household Income'].replace('[\$,]', '', regex=True)
data['Average Household Income'] = pd.to_numeric(data['Average Household Income'])
data['Childrens Under 5, %'] = data['Childrens Under 5, %'].replace('-', np.nan)
data['Childrens Under 5, %'] = pd.to_numeric(data['Childrens Under 5, %'].str.replace('%', ''))

# these coordinates are for Denver
m = folium.Map(location=[39.7392, -104.9903], zoom_start=10)

# Add the color coding to the map
choro = folium.Choropleth(
    geo_data=denver_geojson,
    name='Average Household Income',
    data=data,
    columns=['name', 'Average Household Income'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Average Household Income',
    highlight=True
)

choro.geojson.add_child(
    folium.features.GeoJsonTooltip(fields=['name', 'zipcode', 'Average Household Income'])
)

# Add the choropleth layer to the map
choro.add_to(m)

choro_children = folium.Choropleth(
    geo_data=denver_geojson,
    name='Children Under 5',
    data=data,
    columns=['name', 'Childrens Under 5, %'],
    key_on='feature.properties.name',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Childrens Under 5, %',
    highlight=True
).add_to(m)

choro_children.geojson.add_child(
    folium.features.GeoJsonTooltip(fields=['name', 'zipcode', 'Childrens Under 5, %'])
)

# Add the LayerControl to the map to switch between layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
map_file = 'index.html'
m.save(map_file)

# Open the map file in a new browser tab
webbrowser.open('file://' + os.path.realpath(map_file))


