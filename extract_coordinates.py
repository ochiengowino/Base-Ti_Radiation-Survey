from xml.etree import ElementTree as ET

with open('Object ID 9.kml', 'r') as file:
    tree = ET.parse(file)
    root = tree.getroot()

namespace = {'kml': 'http://www.opengis.net/kml/2.2'}
coords = root.find('.//kml:coordinates', namespace).text.strip()

points = [point.split(',')[:2] for point in coords.split()]
print(points)  # List of [longitude, latitude]