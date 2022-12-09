
import os
from jwtdown_fastapi.authentication import Authenticator
from fastapi import Depends
from queries.accounts import AccountQueries, AccountOut, AccountOutWithPassword

class MyAuthenticator(Authenticator):

    async def get_account_data(
        self,
        username: str,
        accounts: AccountQueries,
    ):

        return accounts.get(username)

    def get_account_getter(
        self,
        accounts: AccountQueries = Depends(),
    ):

        return accounts

    def get_hashed_password(self, account: AccountOutWithPassword):

        return account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOut):

        return account.email, AccountOut(**account.dict())

print("auth line 32", os.environ ["SIGNING_KEY"] )
authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
print("auth line 34")
