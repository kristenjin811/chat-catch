from fastapi import APIRouter, Depends, Response, Request
from queries.users import UserIn, UserOut, UserQueries


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
def get_user(
    response: Response, users: UserQueries = Depends()
):
    response = users.get_all_users()
    return response
