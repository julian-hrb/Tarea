from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id:int
    name:str
    user_creation:datetime = datetime.now()
    notes:str