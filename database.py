from pymongo import MongoClient
import urllib
import json

#file = {"person":{"age":1, "name": ["Vincent", "Vinny", "Vindicator"], "gender": "male"}}


#client = MongoClient("mongodb://pktrieu:"+urllib.parse.quote("Muffin_2008")+"@otter14-shard-00-00-tzahm.mongodb.net:27017,otter14-shard-00-01-tzahm.mongodb.net:27017,otter14-shard-00-02-tzahm.mongodb.net:27017/test?ssl=true&replicaSet=Otter14-shard-0&authSource=admin")
client = MongoClient(host='localhost', port=27017)
db = client.test

cursor = list(db.index.find({"person.age":1}))
print(len(cursor))
