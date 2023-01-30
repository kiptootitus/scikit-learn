import pymongo

# connect to the database
client = pymongo.MongoClient("mongodb+srv://archy:archy123@arcade.te1xd84.mongodb.net/test")

# create a database
db = client["Titus"]

#column
mycol = db["code"]

#insert a document
# myList = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]

#  x = mycol.insert_many(myList)

# print(x.inserted_ids)

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

# #query

# myquery = { "address": "Apple st 652" }

# # delete 
# mycol.delete_one(myquery)

# # updating values in a document
# myquery = { "address": "Valley 345" }

# newvalues = { "$set": { "address": "Canyon 123" } }

# mycol.update_one(myquery, newvalues)

# for x in mycol.find():
#     print(x)

myresult = mycol.find().limit(5)

for x in myresult:
  print(x)