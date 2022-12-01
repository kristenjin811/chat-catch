from pydantic import BaseModel, EmailStr
from fastapi import Response
from models import PydanticObjectId, User, UserInDB
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db


def format_ids(nested_dictionary):
    """
        Loops through nested dictionary (with arrays 1 layer deep) to
        properly format the MongoDB '_id' field to
    a string instead of an ObjectId
    """
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            nested_dictionary[key] = format_ids(value)
        elif type(value) is list:
            new_arr = []
            for item in value:
                if type(item) is dict:
                    new_arr.append(format_ids(item))
                else:
                    new_arr.append(item)
            nested_dictionary[key] = new_arr
        else:
            if key == "_id":
                nested_dictionary[key] = str(value)
    return nested_dictionary


async def get_user_db(name) -> UserInDB:
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    users_collection = db.users
    row = users_collection.find_one({"username": name})
    if row is not None:
        row = format_ids(row)
        return row
    else:
        return None


async def create_user(request, collection):
    # salt = bcrypt.gensalt().decode()
    # hashed_password = get_password_hash(request.password + salt)

    user = {}
    user["username"] = request.username
    # user["salt"] = salt
    # user["hashed_password"] = hashed_password
    dbuser = UserInDB(**user)
    try:
        response = collection.insert_one(dict(dbuser))
        return {"id_inserted": str(response.inserted_id)}
    except Exception as e:
        raise Exception(f"{e}")


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
