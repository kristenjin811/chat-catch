import uuid
import hashlib
from models import User

from mongodb import get_nosql_db, AsyncIOMotorClient


def create_user(request):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(
        request.password.encode("utf-8") * salt.encode("utf-8")
    ).hexdigest()

    user = {}
    user["username"] = request.username
    user["salt"] = salt
    user["hashed_password"] = hashed_password
    user = User(**user)
    return user


def get_user(username):
    db = client[MONGODB_DB_NAME]
    collection = db.user
    row = await collection.find_one({"username": username})
    if row is not None:
        return row
    else:
        return False


def verify_password(plain_password_w_salt, hashed_password):
    checked_password = hashlib.sha512(
        plain_password_w_salt.encode("utf-8")
    ).hexdigest()
    return checked_password == hashed_password
