# from pydantic import BaseModel, EmailStr
# from fastapi import Response
# from models import PydanticObjectId, UserIn, UserOut
# from config import MONGODB_DB_NAME
# from mongodb import get_nosql_db


# async def create_user(self, info=UserIn, response_model=UserOut):
#     client = await get_nosql_db()
#     db = client[MONGODB_DB_NAME]
#     props = info.dict()
#     try:
#         self.collection.insert_one(props)
#     except:
#         pass
#     props["id"] = str(props["_id"])
#     return UserOut(**props)

# async def get_all_users(self):
#     users = []
#     props = self.collection.find({})
#     for document in props:
#         document["id"] = str(document["_id"])
#         users.append(UserOut(**document))
#     return users

# async def get_user(self, id):
#     user = self.collection.find_one({"_id": id})
#     user["id"] = str(user["_id"])
#     return user

# async def delete_user(self, id):
#     self.collection.delete_one({"_id": id})
