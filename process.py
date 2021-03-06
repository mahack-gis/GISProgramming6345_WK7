#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import shapely
import fiona


# In[2]:


from shapely.geometry import Point, mapping
from fiona import collection

schema = {'geometry': 'Point', 'properties': {'name': 'str'}}
with collection("some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['lon']), float(row['lat']))
            output.write({'properties':{'name': row['name']}, 'geometry': mapping(point)})


# In[ ]:




