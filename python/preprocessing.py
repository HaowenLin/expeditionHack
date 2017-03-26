import pandas as pd
import json


crop = pd.read_csv("CropDatabyType.csv")

crop = crop.dropna()

crop_1 = crop.drop('Domain Code',1).drop('Domain',1).drop('Area Code',1).drop('Area',1).drop('Element Code',1).drop('Item Code',1).drop('Year Code',1).drop('Flag',1).drop('Flag Description',1)
crop_2 = crop_1[(crop_1.Element == "Production")| (crop_1.Element =="Area harvested")]

year_dict = {}
year_dict1 = {}




for index, row in crop_2.iterrows():
    tu = (row['Year'],row['Item'])
    tu = (row['Year'],row['Item'])
    if tu not in year_dict:
        year_dict[tu] = ("a","p")


for index, row in crop_2.iterrows():
    if row['Element'] == 'Area harvested':
        tu2 = (row['Year'],row['Item'])
        flag = year_dict[tu2]
        flag = flag[1]
        year_dict[tu2] = (row['Value'],flag)

    if row['Element'] == 'Production':
        tu2 = (row['Year'],row['Item'])
        flag = year_dict[tu2]
        flag = flag[0]
        year_dict[tu2] = (flag,row['Value'])


for eachKey in year_dict:
    if year_dict[eachKey][0] != 'a' and year_dict[eachKey][1] != 'p':
        year_dict1[eachKey] = year_dict[eachKey][1]/year_dict[eachKey][0]



answer = []
product = []

for eachKey in year_dict1:
    answer.append([eachKey[1], [eachKey[0] ,year_dict1[eachKey]]])
    if eachKey[1] not in product:
        product.append(eachKey[1])

answer.sort()
#print answer

food_json = {}
for each in answer:
    if each[0] not in food_json.keys():
        food_json[each[0]] = []
    food_json[each[0]].append({each[1][0]: each[1][1]})

print food_json
'''
for food in answer:
    food_json
'''

f = open("result.json",'w')
f.write(json.dumps(food_json))

#print product
#data = pd.DataFrame(answer)

#print data
