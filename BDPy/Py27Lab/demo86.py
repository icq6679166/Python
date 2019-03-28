import pandas as pd
import folium

sample_data = pd.read_csv('data\\shilin.csv')
print sample_data.shape, sample_data.columns
sample_data.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print sample_data.head()

shilin_night_market = [25.089642, 121.524264]
map_osm = folium.Map(location=shilin_night_market, zoom_start=14)

for i in range(len(sample_data)):
    coordinate = [sample_data.iloc[i, 4], sample_data.iloc[i, 3]]
    message = "%s->%s" % (sample_data.iloc[i, 1], sample_data.iloc[i, 2])
    sampleIcon = folium.Icon(color='green', icon='info-sign')
    folium.Marker(coordinate, icon=sampleIcon, popup=unicode(message, 'utf-8')).add_to(map_osm)


current = [25.052151, 121.543881]
current2 = [25.052287, 121.606749]
folium.CircleMarker(current, radius=50, popup='here we are', fill_color='#C0FFEE', color='#FFC0EE').add_to(map_osm)
folium.Circle(current2, radius=200, popup='here we are', fill_color='#FFC0EE', color='#C0FFEE').add_to(map_osm)

map_osm.save("map\\demo86.html")
