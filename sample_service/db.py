import os
import bson
from pymongo import MongoClient
from pydantic import BaseModel



client = pymongo.MongoClient(os.environ["DATABASE_URL"])
dbname = os.environ['MONGODATABASE']
# host_info = mongo_client["HOST"]
db = client[dbname]

class MessagesIn(BaseModel):
  message: str
  from_time: 

class MessagesQueries:
  def get_all_messages(self):
    result = list(db.messages.find())
    for message in result:
      message["id"] = message["_id"]
    return result
