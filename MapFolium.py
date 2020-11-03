import folium
import json
# from shapely.geometry import shape, Point
from bs4 import BeautifulSoup
from folium.plugins import LocateControl, MarkerCluster

# Create the map
MyMap = folium.Map(location=[41.763854980,-70.076103210], tiles='OpenStreetMap', zoom_start=10, max_zoom=19, control_scale=True)

# Save the map
MyMap.save('MyMap.html')

