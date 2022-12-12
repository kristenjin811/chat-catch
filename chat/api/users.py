from fastapi import (
    APIRouter,
    Depends,
)
from models import UserInDB
from pymongo import MongoClient
from controllers.users import (
    get_user_db,
    create_user,
    delete_user,
    get_all_users,
)
from mongodb import get_nosql_db
from config import MONGODB_DB_NAME
import logging
from request_forms import RegisterRequest

logger = logging.getLogger(__name__)
router = APIRouter()


@router.put("/register")
async def create_user_in_db(
    request: RegisterRequest, client: MongoClient = Depends(get_nosql_db)
):
    db = client[MONGODB_DB_NAME]
    collection = db.users
    new_user = await create_user(request, collection)
    return new_user


@router.get("/users/{name}")
async def get_user(name: str) -> UserInDB:
    response = await get_user_db(name)
    return response


@router.get("/users")
async def get_users(client: MongoClient = Depends(get_nosql_db)):
    users = await get_all_users()
    return users


@router.delete("/users/{name}")
async def delete_user_db(name: str):
    try:
        await delete_user(name)
    except Exception:
        return False
    return True
