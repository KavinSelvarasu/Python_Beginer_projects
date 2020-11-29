import json

with open('list.json', 'r') as f:
    items = json.load(f)
print(items['cat'])
