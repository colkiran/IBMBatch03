import json
JFR = open("books.json", "r")
jsonFile = json.load(JFR)

# print(jsonFile)
for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>",  v)
    print("-" * 40)

print("-" * 60)
# data should be stored in single quotes (')
empdata = '{"name": "Steve", "age": 28, "city": "California"}'
print(empdata)
print(type(empdata))

# convert the string into python dictionary
res = json.loads(empdata)
print(res)
print(type(res))
for k, v in res.items():
    print(k, "=>", v)

