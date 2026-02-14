from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My Web BE")

@app.get("/")
async def root():
    return {"message": "Hello from Python BE!", "status": "live"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "Dev User"}

class User(BaseModel):
    name: str
    email: str

@app.post("/users/")
async def create_user(user: User):
    return {"created": user.name, "email": user.email}
