import pymongo

# Connection to Mongo DB
try:
    conn = pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
conn


# Databases

db = conn.mydb
db

# If you need to know what databases are available:
conn.database_names()

# Collections
collection = db.my_collection
collection
db.collection_names()

# Documents
doc = {"name": "Alberto", "surname": "Negron", "twitter": "@Altons"}
collection.insert(doc)
conn.database_names()
db.collection_names()


