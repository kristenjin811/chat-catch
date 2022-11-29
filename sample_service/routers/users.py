from fastapi import APIRouter, Depends, Response, Request
from queries.users import UserIn, UserOut, UserQueries
from queries.messages import MessageQueries
from bson.objectid import ObjectId


router = APIRouter()


@router.post("/api/users", response_model = UserOut)
async def create_account(
    info: UserIn,  # this is what should be in the body
    users: UserQueries = Depends(),

):

    try:
       info = users.create(info)

    except:
        pass
    print("USER IN::::::", UserIn)
    print("USER OUT::::::", UserOut)

    return info

@router.get("/api/users")
def get_users(
    response: Response, users: UserQueries = Depends()
):
    response = users.get_all_users()
    return response

@router.get("/api/users/{id}")
def get_user(
    id: str,
    user: Response, users: UserQueries = Depends()
):
    user = users.get_user(ObjectId(id))
    return UserOut(**user)

@router.delete("/api/users/{id}", response_model=bool)
async def delete_user(
    id: str,
    user: Response, users: UserQueries = Depends()
) -> bool:
    users.delete_user(ObjectId(id))
    return True
