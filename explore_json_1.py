import json


# this opens the file and reads it
infile = open("eq_data_1_day_m1.json", "r")
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

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])



from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

data = [Scattergeo(lon=lons, lat = lats)]
my_layout = Layout(title="Global Earthquakes")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')
