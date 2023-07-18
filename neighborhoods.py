import json

# Load the GeoJSON file
with open('denver.geojson', 'r') as file:
    denver_geojson = json.load(file)

# Extract the neighborhood names
neighborhoods = [feature['properties']['name'] for feature in denver_geojson['features']]

# Print the neighborhood names
for neighborhood in neighborhoods:
    print('"' + neighborhood + '",')