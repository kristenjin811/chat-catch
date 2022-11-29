from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os



from routers import users
from authenticator import authenticator
from routers import messages
from routers import poller
# from routers import chat




app = FastAPI()

app.include_router(users.router)
app.include_router(authenticator.router)
app.include_router(messages.router)
app.include_router(poller.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
