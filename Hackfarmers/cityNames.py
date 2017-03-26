import json
import codecs
# -*- coding: utf-8 -*-

filename =  "C:\Users\lyj\Downloads\MAR_adm4 .json"
with open(filename, 'r') as f:
    data = json.load(f)

cities = {}

for each in data[u'features']:
    name = each[u'properties'][u'NAME_1']
    if each[u'geometry'][u'type'] == u'Polygon':
        points = each[u'geometry'][u'coordinates'][0]
    if each[u'geometry'][u'type'] == u'MultiPolygon':
        points = each[u'geometry'][u'coordinates'][0][0]
    no = len(points)
    avgLon = 0
    avgLat = 0

    for value in points:
        avgLon += value[0]
        avgLat += value[1]
    avgLon /= no
    avgLat /= no
    #print avgLon, avgLat
    if name not in cities.keys():
        cities[name] = []
    cities[name].append([avgLon, avgLat])

print cities
result = {}
for eachKey in cities:
    avgLon = 0
    avgLat = 0
    no = len(cities[eachKey])
    for value in cities[eachKey]:
        avgLon += value[0]
        avgLat += value[1]
    avgLon /= no
    avgLat /= no
    result[eachKey] = [avgLon, avgLat]

print result

f = codecs.open("result", 'w', 'utf-8')
f.write(json.dumps(result))

'''

#print len(cities)
#print cities
filewrite  =  "C:\Users\lyj\Downloads\cities.txt"
fw = codecs.open(filewrite, 'wb', 'utf-8')
for eachcity in cities:
    #print unicode(eachcity)
    fw.write(eachcity)
    fw.write('\n')
fw.close()'''