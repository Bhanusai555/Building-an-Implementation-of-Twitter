from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TweetBase(BaseModel):
    content: str

class TweetCreate(TweetBase):
    pass

class Tweet(TweetBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True