import pandas as pd
from xml.etree import ElementTree as ET

filename = 'Object ID 36'
# Load the KML file
with open(filename+'.kml', 'r') as file:
    tree = ET.parse(file)
    root = tree.getroot()

# Define the namespace for KML
namespace = {'kml': 'http://www.opengis.net/kml/2.2'}
coords = root.find('.//kml:coordinates', namespace).text.strip()

# Extract and process coordinates
points = [point.split(',')[:2] for point in coords.split()]  # Get only longitude and latitude
data = [{'Longitude': float(lon), 'Latitude': float(lat)} for lon, lat in points]

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = filename+'_coordinates.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Coordinates saved to {output_file}")