
import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import AccountRepository, AccountOut, Account


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        email: str,
        accounts: AccountRepository,
    ):
        print("GET ACCOUNT DATA AUTHEN.PY:::::::::::::::::::::::::::::::::::::::::")
        print("ACOUNTSSSS:::::::::::::::::::::::::::::::::::::::::", accounts)
        return accounts.get_one(email)

    def get_account_getter(
        self,
        accounts: AccountRepository = Depends(),
    ):
        print("22222222222222222222222222222222222222222222222222:::::::::::::::::::::::::::::::::::::::")
        return accounts

    async def get_hashed_password(self, account: Account):
        print("GET HASHED PASSED::::::::::::::::::::::::::::::::::::::::", account)
        return await account.hashed_password

    def get_account_data_for_cookie(self, account: Account):
        print("4444444444444444444444444444444444444444444444444:::::::::::::::::::::::::::::::::::::::::")
        return account.email, AccountOut(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
