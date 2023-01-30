import pymongo

# connect to the database
client = pymongo.MongoClient("mongodb+srv://archy:archy123@arcade.te1xd84.mongodb.net/test")

# create a database
db = client["Titus"]

#column
mycol = db["code"]

#insert a document
mydict = { "name": "Titus", "address": "Highway 37 Karatina Town" }

x = mycol.insert_one(mydict)