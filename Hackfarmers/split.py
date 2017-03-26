import json
import codecs
# -*- coding: utf-8 -*-

filename =  "ReginalArablePotential.json"
with open(filename, 'r') as f:
    data = json.load(f)

region = {}

for each in data[u'features']:
    name = each[u'properties'][u'NAME_1']
   # if name ==
    if name not in region:
        region[name] = {"type": "FeatureCollection", "features": []}
    region[name]["features"].append(each)


#print region

for eachKey in region:
    l = eachKey.split('- ')
    s = ""
    for eachL in l:
        s += eachL[0]

    f = codecs.open(s+".json", 'w', 'utf-8')
    f.write(json.dumps(region[eachKey]))
    f.closed