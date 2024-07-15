import pandas as pd
from collections import Counter
import json


df=pd.read_excel("Short Name Master (corrected).xlsx")
subcategories = df["sub category"].unique().tolist()
print(subcategories)
print(len(subcategories))

import json
a=Counter(subcategories)
print(a)
# lis)t of integer & string

subcategories = [i.strip() for i in subcategories]
print(len(subcategories))

# convert to Json
json_str = json.dumps(list(set(subcategories)))
# displaying
# print(type(json_str))
# print(len(json_str))
# print("Json List:", json_str)
# formatted_items = [{"name": item, "type": "any", "attributes": []} for item in subcategories]
# print(formatted_items)

l = []

for subcategory in subcategories:
    d = {}  # Create a new dictionary for each subcategory
    d['name'] = subcategory
    d['type'] = 'any'
    d['attributes'] = []
    l.append(d)
print('lololololooll',l)
# with open('output.json','w') as file:
#     json.dump(lol,file,indent=2)
# print("l is : ", l)

# # Save to JSON file
# with open('output12.json', 'w') as file:
#     json.dump(l, file, indent=2)
conversion_dict = {}
with open('raw.json','r') as file:
   data = json.load(file)


print('data : ',data)
for i in range(len(data)):
    conversion_dict[data[i]['name']] = i
    print("k;ojojojliolihjilh",i,data[i])
print('conversion_dict : ',conversion_dict)