from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name:str
    username:str
    password:str
    phone:Optional[int]
    user_creation:datetime = datetime.now()
    email:str
    status:bool
    observations:Optional[str]

class ShowUser(BaseModel):
    name:str
    username:str
    phone:int
    user_creation:datetime = datetime.now()
    email:str
    class ConfigDict:
        from_attributes = True

class UpdateUser(BaseModel):
    name:str = None
    username:str = None
    password:str = None
    phone:Optional[int] = None
    user_creation:datetime = None
    email:str = None
    status:bool = None
    observations:Optional[str] = None