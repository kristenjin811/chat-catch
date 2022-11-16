import os
from pymongo import MongoClient


client = pymongo.MongoClient(os.environ["DATABASE_URL"])
dbname = os.environ['MONGODATABASE']
# host_info = mongo_client["HOST"]
db = client[dbname]
