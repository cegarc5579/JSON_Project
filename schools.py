"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""

import json
from turtle import title
from typing import Type

#processing the file, readability 
infile = open("univ.json", "r")
outfile = open('readableuniv.json','w')
unidata = json.load(infile)
#this is for the new file where the information is being sent 
json.dump(unidata, outfile, indent=4)
#print(len(unidata))


univ = []
#creating this function to only get schools that are part of the wanted conferences
#not in any particular order 
for u in unidata:
    conf = u['NCAA']['NAIA conference number football (IC2020)']
    if conf == 102:
        univ.append(u)
    elif conf == 108:
        univ.append(u)
    elif conf == 107:
        univ.append(u)
    elif conf == 127:
        univ.append(u)
    elif conf == 130:
        univ.append(u)

#graduation rate of Women over 50%

lon1,lat1, totalstu, totalstu1, totalstu2, hover_texts,lon2,lat2,lon3,lat3,hover_texts1,hover_texts2= [],[],[],[],[],[],[],[],[],[],[],[]
#seearching for information by placing the keys and hoping to get values returned 
for u in univ:
    if u["Graduation rate  women (DRVGR2020)"] > 50:
        uniname = u["instnm"]
        wgradrate = u["Graduation rate  women (DRVGR2020)"]
        lon1.append(u["Longitude location of institution (HD2020)"])
        lat1.append(u["Latitude location of institution (HD2020)"])
        size = .00025* u["Total  enrollment (DRVEF2020)"]
        totalstu.append(size)
        hover_texts.append(f"{uniname}, {wgradrate}%")

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

#map for women grad rate over 50%
#importing lon and lats so it can be seen
#hover_texts allows you to view that info when hovering over the circles 

data = [
    {'type':'scattergeo',
    'lon':lon1,
    'lat':lat1,
    'text': hover_texts,
    'marker':{
        'size':totalstu,
        'color':size,
        'colorscale':'Viridis',
        'reversescale':True,
      },
      }]
#formatting and setting names of files, titles, etc
my_layout = Layout(title="Schools with Women Graduation Rate over 50%")
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename="womengradrate.html")



#instruction for map 2
#much of it is copied from the previos chart
#calling on the same information, only we are not pulling from 
#the percent of total enrollment for black/african american instead of women grad rate 
for u in univ:
    if u["Percent of total enrollment that are Black or African American (DRVEF2020)"] > 10:
        uniname2 = u["instnm"]
        baaenroll =u["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        lon2.append(u["Longitude location of institution (HD2020)"])
        lat2.append(u["Latitude location of institution (HD2020)"])
        size = .00025* u["Total  enrollment (DRVEF2020)"]
        totalstu1.append(size)
        hover_texts1.append(f"{uniname2}, {baaenroll}%")

#map for black/african american enrollment
data1 = [
    {'type':'scattergeo',
    'lon':lon2,
    'lat':lat2,
    'text': hover_texts1,
    'marker':{
        'size':totalstu1,
        'color':size,
        'colorscale':'Viridis',
        'reversescale':True,
      },
      }]
#formatting and setting names of files, titles, etc
my_layout = Layout(title="Schools with Black or African American Enrollment over 10%")
fig = {'data':data1, 'layout':my_layout}
offline.plot(fig, filename="africanamericanenroll.html")



#instructions for map 3 
#same instructions as above, can copy and paste the same commands
#actually the same way will not work because there are two different instances
#have to use the try except else
'''
for u in univ:
    if u["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
        uniname3 = u["instnm"]
        price = u["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        lon3.append(u["Longitude location of institution (HD2020)"])
        lat3.append(u["Latitude location of institution (HD2020)"])
        size = .00025* u["Total  enrollment (DRVEF2020)"]
        totalstu2.append(size)
        hover_texts2.append(f"{uniname3}, {price}")
'''
for u in univ:
    try:
        price = int(u["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])
    except TypeError:
        print("None")
    else:
        if price > 50000:
            uniname3 = u["instnm"]
            lon3.append(u["Longitude location of institution (HD2020)"])
            lat3.append(u["Latitude location of institution (HD2020)"])
            size = .00025* u["Total  enrollment (DRVEF2020)"]
            totalstu2.append(size)
            hover_texts2.append(f"{uniname3}, {price}")

data2 = [
    {'type':'scattergeo',
    'lon':lon3,
    'lat':lat3,
    'text': hover_texts2,
    'marker':{
        'size':totalstu2,
        'color':size,
        'colorscale':'Viridis',
        'reversescale':True,
      },
      }]
my_layout = Layout(title="Total Price for in-state students living off campus (not with family)")
fig = {'data':data2, 'layout':my_layout}
offline.plot(fig, filename="totalprices.html")
