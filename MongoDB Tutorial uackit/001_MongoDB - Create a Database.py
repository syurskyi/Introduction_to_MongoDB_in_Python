import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

with client:
    db = client['music']