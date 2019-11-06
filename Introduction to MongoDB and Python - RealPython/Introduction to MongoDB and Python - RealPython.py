import pymongo

# Establishing a Connection
from pymongo import MongoClient
client = MongoClient()

# Using the snippet above, the connection will be established to the default host (localhost) and port (27017).
# You can also specify the host and/or port using:
client = MongoClient('localhost', 27017)

# Or just use the Mongo URI format:
client = MongoClient('mongodb://localhost:27017')

# Accessing Databases
db = client.pymongo_test

# Or you can also use the dictionary-style access:
db = client['pymongo_test']

# Inserting Documents
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

# We can even insert many documents at a time, which is much faster than using insert_one()
# if you have many documents to add to the database.
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

# Retrieving Documents
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)

scotts_posts = posts.find({'author': 'Scott'})
print(scotts_posts)

for post in scotts_posts:
    print(post)
