import json
with open('list.json', 'r') as f:
    items = json.load(f)
    items['cat']="karupida"
    items['bar'] = [4,5,6]
print(items)

#verify every methods in josn file manipulation



