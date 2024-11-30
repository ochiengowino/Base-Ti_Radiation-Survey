import pandas as pd
from xml.etree import ElementTree as ET

# Load the KML file
kml_file = 'site 1_hotspot point 1.kml'

with open(kml_file, 'r') as file:
    tree = ET.parse(file)
    root = tree.getroot()

# Define the KML namespace
namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

# Extract all <Placemark> elements
placemarks = root.findall('.//kml:Placemark', namespace)

# Prepare a list to store coordinates and point names
data = []

for placemark in placemarks:
    # Extract the name of the point
    name = placemark.find('kml:name', namespace).text if placemark.find('kml:name', namespace) is not None else "Unnamed"

    # Extract the coordinates (if available)
    point = placemark.find('.//kml:Point/kml:coordinates', namespace)
    if point is not None:
        coords = point.text.strip()
        lon, lat, *_ = coords.split(',')
        data.append({'Name': name, 'Longitude': float(lon), 'Latitude': float(lat)})

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = kml_file+'.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Point coordinates saved to {output_file}")
