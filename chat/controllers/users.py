from models import UserInDB
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db
from utils import format_ids


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


async def get_all_users():
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    users_collection = db.users
    rows = users_collection.find()
    row_list = []
    for row in rows:
        f_row = format_ids(row)
        row_list.append(f_row)
    return row_list


async def create_user(request, collection):
    user = {}
    user["username"] = request.username
    dbuser = UserInDB(**user)
    try:
        response = collection.insert_one(dict(dbuser))
        return {"id_inserted": str(response.inserted_id)}
    except Exception as e:
        raise Exception(f"{e}")


async def delete_user(name: str):
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    users_collection = db.users
    users_collection.delete_one({"username": name})
