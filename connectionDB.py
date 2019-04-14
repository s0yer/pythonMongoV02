from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['database']

books = db['books']

for b in books.find():
    print (b)