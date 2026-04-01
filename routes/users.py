from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
router = APIRouter()

# Mock database
database = {
    "users": {},
}

class User(BaseModel):
    username: str
    password: str
    email: str
    balance: float = 0.0

class UserProfileUpdate(BaseModel):
    email: Optional[str] = None
    balance: Optional[float] = None

@router.post("/register")
async def register(user: User):
    if user.username in database["users"]:
        raise HTTPException(status_code=400, detail="Username already exists")
    database["users"][user.username] = user
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: User):
    db_user = database["users"].get(user.username)
    if db_user and db_user.password == user.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=400, detail="Invalid username or password")

@router.get("/profile/{username}")
async def get_profile(username: str):
    user = database["users"].get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/profile/{username}")
async def update_profile(username: str, user_update: UserProfileUpdate):
    user = database["users"].get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user_update.email:
        user.email = user_update.email
    if user_update.balance is not None:
        user.balance = user_update.balance
    return {"message": "Profile updated successfully"}

@router.get("/balance/{username}")
async def get_balance(username: str):
    user = database["users"].get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"balance": user.balance}

app.include_router(router, prefix="/users")
