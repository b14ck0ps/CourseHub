from fastapi import FastAPI, Query
from pydantic import BaseModel 
from typing import Optional, List

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    age: Optional[int] = None

@app.get("/users/",response_model=List[User])
async def get_users(
    active: bool = Query(True, description="Filter users by active status"),
):
    if active:
        return [user for user in users if user.is_active]
    return users

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"message":"User not found"}