from textwrap import fill
import folium
from numpy import size
import pandas

data = pandas.read_csv('Volcanoes.txt')  # readin all values in the file

# Creates a list for each value on LAT column in the file
latitude = list(data['LAT'])

# Creates a list for each value on LON column in the file
longetude = list(data['LON'])

# Creates a list with elevation from the column in the file
elevation = list(data['ELEV'])


def color_by_elevation(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev <= 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles='Stamen Terrain')

feature_group = folium.FeatureGroup(name='My Map')

for lat, long, elev in zip(latitude, longetude, elevation):

    # feature_group.add_child(folium.Marker(
    #     location=[lat, long],
    #     popup=f'Elevation: {elev} m',
    #     icon=folium.Icon(color=color_by_elevation(elev))))
    feature_group.add_child(
        folium.Circle(
            location=[lat, long],
            radius=elev,
            popup=f'Elevation: {elev} m',
            color=color_by_elevation(elev),
            fill=color_by_elevation(elev)
        )
    )

map.add_child(feature_group)

map.save("Map.html")
