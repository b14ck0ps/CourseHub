from typing import List, Optional

import fastapi
from fastapi import HTTPException
from pydantic import BaseModel

router = fastapi.APIRouter()
users = []


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool


@router.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user


@router.get("/users/", response_model=List[User])
def read_users():
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")
