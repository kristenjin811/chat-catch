
import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import AccountQueries, AccountOut, AccountOutWithPassword


class MyAuthenticator(Authenticator):
    async def get_account_data(
        self,
        username: str,
        accounts: AccountQueries,
    ):
        print("GET ACCOUNT DATA AUTHEN.PY:::::::::::::::::::::::::::::::::::::::::")
        print("ACOUNTSSSS:::::::::::::::::::::::::::::::::::::::::", accounts)
        return accounts.get(username)

    def get_account_getter(
        self,
        accounts: AccountQueries = Depends(),
    ):
        print("22222222222222222222222222222222222222222222222222:::::::::::::::::::::::::::::::::::::::")
        return accounts

    async def get_hashed_password(self, account: AccountOutWithPassword):
        print("GET HASHED PASSED::::::::::::::::::::::::::::::::::::::::", account)
        return await account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOut):
        print("4444444444444444444444444444444444444444444444444:::::::::::::::::::::::::::::::::::::::::")
        return account.email, AccountOut(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
