from fastapi import APIRouter, Depends
from queries.users import UserIn, UserOut, UserQueries


router = APIRouter()


@router.post("/api/users")
async def create_account(
    info: UserIn,  # this is what should be in the body
    users: UserQueries = Depends(),
):
    try:
        users.create(info)
    except:
        pass
    return UserOut
