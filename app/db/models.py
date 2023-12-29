from app.db.database import Base
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    username = Column(String(32),unique=True)
    password = Column(String(32))
    phone = Column(Integer)
    user_creation = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    email = Column(String(255),unique=True)
    status = Column(Boolean,default=False)
    observations = Column(String(255))