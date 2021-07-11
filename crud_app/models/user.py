from typing import List
from pydantic import BaseModel
from blog import Blog


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
