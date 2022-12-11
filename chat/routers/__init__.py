# Api directory will function much like what the routers
# directory was designed to do before. It has all the api endpoints
from fastapi import APIRouter

# import routers from all files in api directory
from routers.users import router as user_router
from routers.chatrooms import router as chatrooms_router
from routers.accounts import router as accounts_router

router = APIRouter()

# include the routers in this main router which will
# be imported into the main.py
router.include_router(user_router)
router.include_router(chatrooms_router)
router.include_router(accounts_router)
