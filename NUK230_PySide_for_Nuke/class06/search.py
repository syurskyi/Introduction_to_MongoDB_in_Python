from pymongo import MongoClient
server = MongoClient()
db = server['test']
collection = db['users']

# search = collection.find()
# search = collection.find({"age":20})
search = collection.find({"age":20, "country":"france"})
print(search.count())

for i in search:
    print(i)