from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)

# # from models import UserIn, UserOut
from models import User, UserInDB
from pymongo import MongoClient

# # from jwtdown_fastapi.authentication import Token
# # from routers.auth import auth
from requests import RegisterRequest
from bson.objectid import ObjectId
from pydantic import BaseModel
from controllers.users import get_user_db, create_user
from mongodb import get_nosql_db
from config import MONGODB_DB_NAME
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post
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


@router.post("/register")
async def create_user_in_db(
    request: RegisterRequest, client: MongoClient = Depends(get_nosql_db())
):
    db = client[MONGODB_DB_NAME]
    collection = db.users
    new_user = await create_user(request, collection)
    return new_user


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


# @router.get("/api/users")
# def get_users(response: Response, users: UserQueries = Depends()):
#     response = users.get_all_users()
#     return response


@router.get("/users/{name}")
async def get_user(name: str) -> UserInDB:
    response = await get_user_db(name)
    return response


# @router.get("/api/users/{id}")
# def get_user(id: str, user: Response, users: User = Depends()):
#     user = users.get_user_db(Response.username)
#     return User(**user)


# @router.delete("/api/users/{id}", response_model=bool)
# async def delete_user(
#     id: str, user: Response, users: UserQueries = Depends()
# ) -> bool:
#     users.delete_user(ObjectId(id))
#     return True
