# ### Making a Connection with MongoClient
# ######################################################################################################################

import pymongo

# Establishing a connection in MongoDB requires us to create a MongoClient to the running MongoDB instance.
from pymongo import MongoClient
client = MongoClient()

# The above code will connect to the default host and port, but we can specify the host and port as shown below:
# client = MongoClient("localhost", 27017)

# MongoDB also has a URI format for doing this.
# client = MongoClient('mongodb://localhost:27017/')

# ### Creating a Database
# ######################################################################################################################
db = client['datacampdb']

# ### Data in MongoDB
# ######################################################################################################################
article = {"author": "Derrick Mwiti",
            "about": "Introduction to MongoDB and Python",
            "tags":
                ["mongodb", "python", "pymongo"]}

# ### Inserting a Document
# ######################################################################################################################
articles = db.articles
result = articles.insert_one(article)
print("First article key is: {}".format(result.inserted_id))
db.list_collection_names()

article1 = {"author": "Emmanuel Kens",
            "about": "Knn and Python",
            "tags":
                ["Knn","pymongo"]}
article2 = {"author": "Daniel Kimeli",
            "about": "Web Development and Python",
            "tags":
                ["web", "design", "HTML"]}
new_articles = articles.insert_many([article1, article2])
print("The new article IDs are {}".format(new_articles.inserted_ids))

# ### Retrieving a Single Document with find_one()
# ######################################################################################################################
print(articles.find_one())

# ### Finding all Documents in a Collection
# ######################################################################################################################
for article in articles.find():
  print(article)

# When building web applications, we usually get document IDs from the URL and try to retrieve them from our
# MongoDB collection. In order to achieve this, we first have to convert the obtained string ID into an ObjectId.

from bson.objectid import ObjectId
def get(post_id):
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

# ### Return Some Fields Only
# ######################################################################################################################
for article in articles.find({},{ "_id": 0, "author": 1, "about": 1}):
  print(article)

# ### Sorting the Results
# ######################################################################################################################
doc = articles.find().sort("author", -1)

for x in doc:
  print(x)

# ### Updating a Document
# ######################################################################################################################
query = { "author": "Derrick Mwiti" }
new_author = { "$set": { "author": "John David" } }

articles.update_one(query, new_author)

for article in articles.find():
  print(article)

# ### Limiting the Result
# ######################################################################################################################
limited_result = articles.find().limit(1)
for x in limited_result:
    print(x)

# ### MongoDB Delete Document
# ######################################################################################################################
db.articles.delete_one({"_id":ObjectId("5ba4d00e2e8ca029163417d4")})

# ### Deleting Many Documents
# ######################################################################################################################
delete_articles = articles.delete_many({})
print(delete_articles.deleted_count, " articles deleted.")

# ### Dropping a Collection
# ######################################################################################################################
articles.drop()
db.list_collection_names()

# ### Creating a Database
# ######################################################################################################################

# ### Creating a Database
# ######################################################################################################################

# ### Creating a Database
# ######################################################################################################################
