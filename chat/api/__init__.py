from fastapi import APIRouter

from api.users import router as user_router
from api.chatrooms import router as chatrooms_router
router = APIRouter()

router.include_router(user_router)
router.include_router(chatrooms_router)
