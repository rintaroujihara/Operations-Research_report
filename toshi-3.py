import pandas as pd
import codecs
import sys
import io
#sys.stdout= io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from urllib import request
from bs4 import BeautifulSoup
import csv
import pandas as pd
import xlwt
import re
import folium
import xlrd
import os
import os.path 
import json
xl_bk = xlrd.open_workbook('airport-adress.xls')
xl_sh = xl_bk.sheet_by_index(0)
name = []
ido = []
keido  = []
tiriti = []
line = [[[]for i in range(2)]for i in range(600)]
for i in range(0, 78):
    name.append(xl_sh.cell(i, 1).value)
    ido.append(xl_sh.cell(i, 2).value)
    keido.append(xl_sh.cell(i, 3).value)
    tiriti.append(xl_sh.cell(i, 4).value)
    i +=1
k = 0
for i in range(1,79):
    for j in range(6,84):
        if  xl_sh.cell(i, j).value ==1:
            if i == 1 or j == 6 or i == 4 or j == 9 or i == 2 or j == 7 or i == 5 or j == 10:
                line[k] = [[xl_sh.cell(i-1,2).value,xl_sh.cell(i-1, 3).value]]
                line[k] += [[xl_sh.cell(j-6,2).value,xl_sh.cell(j-6, 3).value]]
                k += 1
print(line)
airport_adress = pd.DataFrame({
    'city': name,
    'latitude': ido,
    'longtude': keido,
    'tiriti': tiriti,
})
airport_map = folium.Map(location=[35.549393, 139.779839], zoom_start=9)
folium.TileLayer('Mapbox Bright').add_to(airport_map)

for i, r in airport_adress.iterrows():
    folium.CircleMarker(
            location=[r['latitude'], r['longtude']],
            radius = r['tiriti']*100,
            fill=True,
            fill_color = "red",
            color = "red",
            popup=r['city']).add_to(airport_map)

for i in range(k):
    folium.PolyLine(line[i] ,color = "blue", weight = 0.3, opacity = 1).add_to(airport_map)

airport_map.save("airport_map4.html")
