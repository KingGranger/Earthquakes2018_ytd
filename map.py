import folium
import requests
import json
from datetime import datetime
import pdb


earthquakes = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2018-01-01&minlatitude=22&maxlatitude=50&minlongitude=-83&maxlongitude=-63&orderby=magnitude").json()['features']
map = folium.Map(location=[37.50, -73], zoom_start=5, max_zoom=10, min_zoom=4, prefer_canvas=True, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="vacation")

for earthquake in earthquakes:
    # pdb.set_trace()
    date = datetime.fromtimestamp(earthquake['properties']['time']/1000).strftime('%Y-%m-%d %H:%M:%S')
    place = earthquake['properties']['place']
    mag = earthquake['properties']['mag']
    if mag > 2:
        color = 'orange'
    else:
        color = 'green'
    fg.add_child(folium.CircleMarker(location=[earthquake['geometry']['coordinates'][1],earthquake['geometry']['coordinates'][0]], radius=15, popup="Date: %s \n Place: %s \n Magnitude: %s" %(date, place, mag), fill_color=color, color= 'grey', fill=True, fill_opacity=0.7))

# fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fg)
map.save('index.html')
