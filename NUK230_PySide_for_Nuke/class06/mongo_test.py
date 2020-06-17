from pymongo import MongoClient
import datetime

server = MongoClient()

db = server['test']
country_collection = db['country']
country_collection.drop()

canada = dict()
canada['name'] = 'canada'
canada['population'] = 36000000
canada['fondation'] = datetime.datetime(1867, 7, 1)
# country_collection.save(canada)

usa = dict()
usa['name'] = 'usa'
usa['population'] = 316000000
usa['fondation'] = datetime.datetime(1776, 7, 4)

country_collection.insert([canada, usa])