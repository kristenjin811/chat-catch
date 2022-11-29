import pymongo
import os
import time
from bson.json_util import dumps


MONGO_URL = os.environ.get("DATABASE_URL")
client = pymongo.MongoClient(MONGO_URL)

# change= client.users.collection.watch()

# for user in users:
#     print(dumps(change))
#     print("")
# print(client.test2.test2.insert_one({"Hello": "world"}).inserted_id)
print(client.chat.userVO.insert_one({"Hello": "world"}).inserted_id)
# change_stream = client.changestream.collection.watch()
# for change in change_stream:
#     print(dumps(change))
#     print("")

class Queries:
    @property
    def collection(self):
        db = client[self.DB_NAME]
        return db[self.COLLECTION]
