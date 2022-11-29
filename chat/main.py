from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import users
from authenticator import authenticator
from routers import users, messages, auth, websocket


app = FastAPI()
app.include_router(users.router)
app.include_router(authenticator.router)
app.include_router(messages.router)
app.include_router(auth.auth.router)
app.include_router(websocket.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
