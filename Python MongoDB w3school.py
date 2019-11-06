import pymongo

# ### Creating a Database
# ######################################################################################################################
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

# ### Check if Database Exists
# ######################################################################################################################
print(myclient.list_database_names())

# OR

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

# ### Creating a Collection
# ######################################################################################################################
mycol = mydb["customers"]

# ### Check if Database Exists

print(mydb.list_collection_names())

# OR

collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")


# ### Insert Into Collection
# ######################################################################################################################
mydict = {"name": "John", "address": "Highway 37"}

x = mycol.insert_one(mydict)

# ### Return the _id Field
# ######################################################################################################################
mydict = {"name": "Peter", "address": "Lowstreet 27"}
x = mycol.insert_one(mydict)
print(x.inserted_id)

# ### Insert Multiple Documents
# ######################################################################################################################
mylist = [
  {"name": "Amy", "address": "Apple st 652"},
  {"name": "Hannah", "address": "Mountain 21"},
  {"name": "Michael", "address": "Valley 345"},
  {"name": "Sandy", "address": "Ocean blvd 2"},
  {"name": "Betty", "address": "Green Grass 1"},
  {"name": "Richard", "address": "Sky st 331"},
  {"name": "Susan", "address": "One way 98"},
  {"name": "Vicky", "address": "Yellow Garden 2"},
  {"name": "Ben", "address": "Park Lane 38"},
  {"name": "William", "address": "Central st 954"},
  {"name": "Chuck", "address": "Main Road 989"},
  {"name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)

# ### Insert Multiple Documents, with Specified IDs
# ######################################################################################################################
mylist = [
  {"_id": 1, "name": "John", "address": "Highway 37"},
  {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  {"_id": 3, "name": "Amy", "address": "Apple st 652"},
  {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
  {"_id": 5, "name": "Michael", "address": "Valley 345"},
  {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
  {"_id": 8, "name": "Richard", "address": "Sky st 331"},
  {"_id": 9, "name": "Susan", "address": "One way 98"},
  {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
  {"_id": 12, "name": "William", "address": "Central st 954"},
  {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
  {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)

# ### Find One
# ######################################################################################################################
x = mycol.find_one()
print(x)

# ### Find All
# ######################################################################################################################
for x in mycol.find():
    print(x)

# ### Return Only Some Fields
# ######################################################################################################################
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field).
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:

for x in mycol.find({}, {"address": 0}):
    print(x)

# You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):

# for x in mycol.find({}, {"name": 1, "address": 0}):
#   print(x)

# ### Filter the Result
# ######################################################################################################################
myquery = {"address": "Park Lane 38"}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# ### Advanced Query
# ######################################################################################################################
myquery = {"address": {"$gt": "S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# ### Filter With Regular Expressions
# ######################################################################################################################
myquery = {"address": {"$regex": "^S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# ### Sort the Result
# ######################################################################################################################
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

# ### Sort Descending
# ######################################################################################################################
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)

# ### Delete Document
# ######################################################################################################################
myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)

# ### Delete Many Documents
# ######################################################################################################################
myquery = {"address": {"$regex": "^S"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

# ### Delete All Documents in a Collection
# ######################################################################################################################
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

# ### Delete Collection
# ######################################################################################################################
mycol.drop()

# ### Update Collection
# ######################################################################################################################
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

mycol.update_one(myquery, newvalues)

# print "customers" after the update:
for x in mycol.find():
    print(x)

# ### Update Many
# ######################################################################################################################
myquery = {"address": {"$regex": "^S"}}
newvalues = {"$set": {"name": "Minnie"}}

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

# ### Limit the Result
# ######################################################################################################################
myresult = mycol.find().limit(5)

# print the result:
for x in myresult:
    print(x)
