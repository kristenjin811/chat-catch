import os
import pymongo


client = pymongo.MongoClient(os.environ["DATABASE_URL"])
dbname = os.environ["DATABASE_NAME"]
# host_info = mongo_client["HOST"]
db = client[dbname]
