from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    status,
    HTTPException,
)
from queries.users import UserIn, UserOut, UserQueries
from jwtdown_fastapi.authentication import Token
from routers.auth import auth
from bson.objectid import ObjectId
from pydantic import BaseModel


class UserForm(BaseModel):
    username: str
    password: str


class UserToken(Token):
    account: UserOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.get("/api/token", response_model=UserToken | None)
async def get_token(
    request: Request,
    user: UserOut = Depends(auth.try_get_current_account_data),
) -> UserToken | None:
    if auth.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[auth.cookie_name],
            "type": "Bearer",
            "user": user,
        }
    else:
        raise Exception("No cookie in request")


@router.post("/api/users", response_model=UserOut | HttpError)
async def create_account(
    info: UserIn,  # this is what should be in the body
    users: UserQueries = Depends(),
):
    hashed_password = auth.hash_password(info.password)
    try:
        users.create(info, hashed_password)
    except DuplicateUserError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create a user with those credentials",
        )
    UserForm(username=info.username, password=info.password)
    print("USER IN::::::", UserIn)
    print("USER OUT::::::", UserOut)
    return info


@router.get("/api/users")
def get_users(response: Response, users: UserQueries = Depends()):
    response = users.get_all_users()
    return response


@router.get("/api/users/{id}")
def get_user(id: str, user: Response, users: UserQueries = Depends()):
    user = users.get_user(ObjectId(id))
    return UserOut(**user)


@router.delete("/api/users/{id}", response_model=bool)
async def delete_user(
    id: str, user: Response, users: UserQueries = Depends()
) -> bool:
    users.delete_user(ObjectId(id))
    return True
