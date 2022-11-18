from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
import os
import reactions

app = FastAPI()

app.include_router(reactions.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "year": 2022,
            "month": 12,
            "day": "9",
            "hour": 19,
            "min": 0,
            "tz:": "PST"
        }
    }


@router.get("/api/reactions")
def reactions():
    return {
        "reactions":{
            "picture_url": str
        }
    }

@app.get("/api/reaction")
def reaction():
    return {
        "reaction":{
            "picture_url": str
        }
    }

@app.post("/api/reaction")
def post_reaction():
    return {
        "reaction":{
            "picture_url": str
        }
    }
