import pymongo
client = pymongo.MongoClient("mongodb+srv://navneet:steel98@cluster0.6i5c2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
# print(db)

d = {'name':'monkey','surname':'D.Luffy','email':'one.piece@gmail.com'}  # creating a dictionary

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

