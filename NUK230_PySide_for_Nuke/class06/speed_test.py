import time
from pymongo import MongoClient
server = MongoClient()
db = server['test']
collection = db['test_collection']

start = time.time()
for i in range(500000):
    doc = dict()
    doc['hello'] = 'world'
    collection.save(doc)
end = time.time()
print(end - start)

# start = time.time()
# l = []
# for i in range(500000):
#     doc = dict()
#     doc['hello'] = 'world'
#     l.append(doc)
# collection.insert(l)
# end = time.time()
# print(end - start)
