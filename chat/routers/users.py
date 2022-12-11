from fastapi import (
    APIRouter,
    Depends,
    # Response,
    # Request,
    # status,
    # HTTPException,
)
from models import UserInDB
from pymongo import MongoClient

from queries.users import (
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


# # endpoints:
# # create_user <@router.post("/api/users")>
# # get_all_users <@router.get("/api/users")>
# # get_user <@router.get("/api/users/{user_id}")>
# # update_user <@router.put("/api/users/{user_id}">
# # delete_user <@router.delete("/api/users/{user_id}">

# # @router.get("/api/token", response_model=UserToken | None)
# # async def get_token(
# #     request: Request,
# #     user: UserOut = Depends(auth.try_get_current_account_data),
# # ) -> UserToken | None:
# #     if auth.cookie_name in request.cookies:
# #         return {
# #             "access_token": request.cookies[auth.cookie_name],
# #             "type": "Bearer",
# #             "user": user,
# #         }
# #     else:
# #         raise Exception("No cookie in request")


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


# @router.post("/api/users", response_model=UserOut | HttpError)
# async def create_user(
#     info: UserIn,  # this is what should be in the body
#     users: UserQueries = Depends(),
# ):
#     # hashed_password = auth.hash_password(info.password)
#     try:
#         users.create(info, hashed_password)
#     except DuplicateUserError:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Cannot create a user with those credentials",
#         )
#     UserForm(username=info.username, password=info.password)
#     print("USER IN::::::", UserIn)
#     print("USER OUT::::::", UserOut)
#     return info
