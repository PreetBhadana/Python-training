# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI(title="My Web BE")

# @app.get("/")
# async def root():
#     return {"message": "Hello from Python BE!", "status": "live"}

# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     return {"user_id": user_id, "name": "Dev User"}

# class User(BaseModel):
#     name: str
#     email: str

# @app.post("/users/")
# async def create_user(user: User):
#     return {"created": user.name, "email": user.email}


## User CRUD APIs

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import UserDB
from schemas import UserCreate, UserResponse

app = FastAPI(title="My Web BE")

# Create tables
Base.metadata.create_all(bind=engine)

# Root
@app.get("/")
async def root():
    return {"message": "API running"}

# Get all users
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(UserDB).all()

# Create user
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserDB(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": f"User {user_id} deleted"}
