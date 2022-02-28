import json


# this opens the file and reads it
infile = open("eq_data_30_day_m1.json", "r")
# this creates a new file and writes in it
# this outfile is so that we can see it in our project instead of notephad
outfile = open("readable_eq_data.json", "w")

# this converts the json into a python version, or a dictionary
eq_data = json.load(infile)
# what does this do? does this dump the json into the new file?
# The json. dump() method allows us to convert a python object into an equivalent JSON object
# and store the result into a JSON file at the working directory.
json.dump(eq_data, outfile, indent=4)
# printing out the number of earthquakes
# the key is features, and this gives you the value, which is the number of earthquakes
list_of_eqs = eq_data["features"]
mags = []


for eq in list_of_eqs:
    # features is the first key
    # properties is the first key within the dictionary

    mag = eq["properties"]["mag"]
    mags.append(mag)
# this prints out the first 10
print(mags[:10])

# print(len(list_of_eqs))

mags, lons, lats, hover_texts = [], [], [], []
#this is how the map is changed (i think)

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    title = eq["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags[:10])
print(lons[:10])
print(lats[:10])

#[expression, iteration, condition]
#new_mags = [mag * 5 for mag in mags] this only has the expression and the iteration
#condition would continue after "mags" and would be "if mag > 3"
#list comprehension does things in a more concise way and thats what he did in the line above 

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size': [5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    },
    }]
my_layout = Layout(title="Global Earthquakes")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')
