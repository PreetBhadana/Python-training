"""
Python excels as a backend for web apps—perfect complement to your React/Next.js frontend skills. Top 2026 frameworks: FastAPI (modern, fast APIs), Flask (lightweight), Django (full-stack). We'll start with FastAPI (async, auto-docs, type-safe).
"""

# Install in your python-training/backend folder

# Create a virtual environment and activate it (on terminal)
"""
$ mkdir Python-training && cd Python-training
$ python3 -m venv venv
$ source venv/bin/activate # this one is for running the environment
$ deactivate # this one is for deactivating the environment
"""

# Install FastAPI and Uvicorn (on terminal)
"""
$ pip install "fastapi[standard]" uvicorn
"""

# After this let make a small API server using unicorn and can access the FE to docs of the API

# Create a new file named main.py in your backend folder
"""
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
"""

# Run the server (on terminal)
"""
$ uvicorn main:app --reload
"""

# My Output was -- 
"""

# Access the API docs (on browser)
http://localhost:8000/docs


# if i run the curl command (on terminal)
$ curl -X 'GET' \
>   'http://127.0.0.1:8000/' \
>   -H 'accept: application/json'

# My Output was -- 
"{\"message\": \"Hello from Python BE!\", \"status\": \"live\"}"


$ curl http://localhost:8000/users/1

# My Output was -- 
"{\"user_id\": 1, \"name\": \"Dev User\"}"


$ curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Preet",
  "email": "preet@gmail.com"
}'

# My Output was -- 
"{\"created\": \"Preet\", \"email\": \"preet@gmail.com\"}"
 
"""



## Lets go in more advance to connect with DB and make CURD APIs with DB

# First we need to install sqlalchemy (on terminal)
"""
$ pip install sqlalchemy
"""

# And some more if like to go for JWT (optional)
"""
$ pip install sqlalchemy alembic python-jose[cryptography] python-multipart
"""

# Create a new file named database.py in your backend folder
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""

# Create a new file named models.py in your backend folder
"""
from sqlalchemy import Column, Integer, String
from database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
"""

# Create a new file named schemas.py in your backend folder
"""
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
"""

# Create a new file named main.py in your backend folder
"""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import UserDB
from schemas import UserCreate

app = FastAPI(title="My Web BE")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "API running"}

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(UserDB).all()

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserDB(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
"""

# Run the server (on terminal)
"""
$ uvicorn main:app --reload
"""

# My Output was -- 
"""
# if i run the curl command (on terminal)
$ curl -X 'GET'   'http://127.0.0.1:8000/'   -H 'accept: application/json'

# My Output was -- 
"{\"message\": \"API running\"}"


# if i run the curl command (on terminal)
$ curl -X 'GET' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json'

# My Output was -- 
"[]"


# if i run the curl command (on terminal)
$ curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Preet Bhadana 2",
  "email": "preet2@gmail.com"
}'

# My Output was -- 
"{\"created\": \"Preet Bhadana 2\", \"email\": \"preet2@gmail.com\"}"


# if i run the curl command (on terminal)
$ curl -X 'GET' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json'

# My Output was -- 
"[{\"name\":\"Preet Bhadana\",\"id\":1,\"email\":\"preet@gmail.com\"},{\"name\":\"Preet Bhadana 2\",\"id\":2,\"email\":\"preet2@gmail.com\"}]"


# if i run the curl command (on terminal)
$ curl -X 'GET' \
  'http://127.0.0.1:8000/users/1' \
  -H 'accept: application/json'

# My Output was -- 
"{\"name\":\"Preet Bhadana\",\"id\":1,\"email\":\"preet@gmail.com\"}"

"""


## Let ass user details, and Delete API -- 

# In Schema.py
"""
class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True
"""

# In main.py
"""
from schemas import UserCreate, UserResponse

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
"""

# if i run the curl command (on terminal)
# My Output was -- 

"""
curl -X 'GET'   'http://127.0.0.1:8000/users/1'   -H 'accept: application/json'

# My Output was -- 
"{\"name\":\"Preet Bhadana\",\"id\":1,\"email\":\"preet@gmail.com\"}"


# if i run the curl command (on terminal)
$ curl -X 'DELETE' \
  'http://127.0.0.1:8000/users/1' \
  -H 'accept: application/json'

# My Output was -- 
"{\"message\":\"User 1 deleted\"}"

# Then run the curl command (on terminal)
$ curl -x 'GET \
  'http://127.0.0.1:8000/users/1' \
  -H 'accept: application/json'

# My Output was -- 
"{\"detail\":\"User not found\"}"


$ curl -X 'GET' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json'

# My Output was -- 
"[{\"name\":\"Preet Bhadana 2\",\"id\":2,\"email\":\"preet2@gmail.com\"}]"

"""
