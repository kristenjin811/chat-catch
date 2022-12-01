# import os
# from fastapi import Depends
# from jwtdown_fastapi.authentication import Authenticator
# from queries.users import UserQueries, UserOut, UserPasswordDB


# class Auth(Authenticator):
#     async def get_account_data(
#         self,
#         username: str,
#         users: UserQueries,
#     ):
#         # Use your repo to get the account based on the
#         # username (which could be an email)
#         return users.get(username)

#     def get_account_getter(
#         self,
#         users: UserQueries = Depends(),
#     ):
#         # Return the users. That's it.
#         return users

#     def get_hashed_password(self, user: UserPasswordDB):
#         # Return the encrypted password value from your
#         # account object
#         return user.password

#     def get_account_data_for_cookie(self, user: UserOut):
#         # Return the username and the data for the cookie.
#         # You must return TWO values from this method.
#         return user.username, UserOut(**user.dict())


# auth = Auth(os.environ.get("SIGNING_KEY"))
