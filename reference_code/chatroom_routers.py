# from fastapi import APIRouter, Depends
# from queries.chatrooms import ChatroomIn, ChatroomOut, ChatroomQueries

# router = APIRouter()


# @router.post("/api/chatrooms/", response_model=ChatroomOut)
# async def create_chatroom(
#     info: ChatroomIn,
#     chatrooms: ChatroomQueries = Depends(),
# ):
#     try:
#         info = chatrooms.create(info)
#     except:
#         pass
#     return info

# @router.get("/api/chatrooms/", response_model=ChatroomOut)
# async def get_all_chatrooms(
#     info: ChatroomIn,
#     chatrooms: ChatroomQueries = Depends(),
# ):
#     try:
#         info = chatrooms.get_all(info)
