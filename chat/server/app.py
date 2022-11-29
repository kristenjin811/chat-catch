from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
from mongodb import connect_to_mongo, close_mongo_connection, get_nosql_db
from pydantic import BaseModel
from controllers import create_user
from config import MONGODB_COLLECTION

app = FastAPI()

client = get_nosql_db()
db = client[MONGODB_COLLECTION]

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"Send: {data}")
        await websocket.send_tet(f"{data}")


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/register")
def register_user(
    request: RegisterRequest,
    client: AsyncIOMotorClient = Depends(get_nosql_db()),
):
    collection = client["MONGODB_COLLECTION"]["users"]
    user = create_user(request)
    response = await collection.insert_one(user)
    return {"response": {"user_id": response.inserted_id}}
