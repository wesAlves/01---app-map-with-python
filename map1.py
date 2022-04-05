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

vulcanos = folium.FeatureGroup(name='Vulcanos')
population = folium.FeatureGroup(name='Population')

for lat, long, elev in zip(latitude, longetude, elevation):

    vulcanos.add_child(
        folium.Circle(
            location=[lat, long],
            radius=elev,
            popup=f'Elevation: {elev} m',
            color=color_by_elevation(elev),
            fill=color_by_elevation(elev)
        )
    )

population.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    # lambda is an anonymous function that create a possible to createand call a functuin in one line
    style_function=lambda x: {
        'fillColor': 'green' if x['properties']['POP2005'] < 1000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
        else 'red'
    }
))


map.add_child(vulcanos)
map.add_child(population)

# this layer control needs to come after the feature_group, otherwise it will not find the layers
map.add_child(folium.LayerControl())

map.save("Map.html")
