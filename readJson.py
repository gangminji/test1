import json

f = 'test.json'

with open(f,'r') as fr:
    data = json.load(fr)

print(data)
