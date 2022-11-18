import os
from pymongo import MongoClient


client = pymongo.MongoClient(os.environ["DATABASE_URL"])
dbname = os.environ["DATABASE_NAME"]
# host_info = mongo_client["HOST"]
db = client[dbname]



class ReactionQueries:
    def get_all_reactions(self):
        db = client[db]
        result = list(db.reactions.find())
        return result

    def get_reaction(self, id):
        db = client[db]
        result = db.reactions.find_one({"_id": id})
        if result:
            result["id"] = result["_id"]
        return result

    def create_reaction(self, data):
        db = client[db]
        result = db.reactions.insert_one(data.dict())
        return result
