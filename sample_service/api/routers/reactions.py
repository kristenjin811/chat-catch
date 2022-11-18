from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ReactionOut(BaseModel):
    picture_url: str

class ReactionsOut(BaseModel):
    reactions: list[ReactionOut]

@router.get("/api/reactions", response_model=ReactionsOut)
def reactions_list():
    return {
        "picture_url": str
    }
