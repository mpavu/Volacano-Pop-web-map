import folium 
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
title=list(data["NAME"])
elev=list(data["ELEV"])

#create map object
map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")

#adding marker
fg=folium.FeatureGroup(name="My Map")
for lt, ln, name, el in zip(lat, lon, title, elev):
    fg.add_child(folium.Marker(location= [lt, ln] , popup=name+str(elev), icon=folium.Icon(color='green')))
    
map.add_child(fg)

#excute/run/open/save map object
map.save("Map1.html")
