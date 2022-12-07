from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel

from queries.accounts import (
    AccountIn,
    AccountOut,
    AccountQueries,
    DuplicateAccountError,
)


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.post("/api/accounts", response_model=AccountToken | HttpError)
async def create_account(

    info: AccountIn,
    request: Request,
    response: Response,
    accounts: AccountQueries = Depends(),
    ):
    print("info::::::::", info)
    print("request::::::::", request)
    print("response::::::::", response)
    print("repo::::::::", accounts)
    hashed_password = authenticator.hash_password(info.password)
    print("hashed_password:::::::", hashed_password)
    # try:
    #     account = repo.create(info, hashed_password)
    # except DuplicateAccountError:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Error, email already in use",
    #     )
    try:
        account = accounts.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    print("account router::::::::::", account)
    form = AccountForm(username=info.email, password=info.password)
    print("form:::::::::::::", form)
    token = await authenticator.login(response, request, form, accounts)
    print("token::::::::::::", token)
    return AccountToken(account=account, **token.dict())


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: AccountOut = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }

# @router.get("/gathering/accounts/{email}", response_model=[Account])
# def get_one_account(
#   email: str,
#   response: Response,
#   repo: AccountRepository = Depends(),
# ) -> Account:
#   account = repo.get_one(email)
#   if account is None:
#     response.status_code = 404
#   return account
