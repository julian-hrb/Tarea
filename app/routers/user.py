from fastapi import APIRouter,Depends
from app.schemas import User,ShowUser,UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/",response_model=List[ShowUser])
def get_users(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data

@router.post("/")
def create_user(user:User,db:Session = Depends(get_db)):
    user = user.dict()
    new_user = models.User(
        name=user["name"],
        username=user["username"],
        password=user["password"],
        phone=user["phone"],
        user_creation=user["user_creation"],
        email=user["email"],
        status=user["status"],
        observations=user["observations"]
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(user)
    return {"Notification":"User created succesfully"}

@router.get("/{id}",response_model=ShowUser)
def get_user(id:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return {"Notification":"User not found"}
    return user

@router.delete("/{id}")
def delete_user(id:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        return {"Notification":"User not found or does not exists"}
    user.delete(synchronize_session=False)
    db.commit()
    return {"Notification":"User deleted succesfully"}

@router.patch("/{id}")
def update_user(id:int,updateUser:UpdateUser,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        return {"Notification":"User not found or does not exists"}
    user.update(updateUser.dict(exclude_unset=True))
    db.commit()
    return {"Notification":"User updated succesfully"}
    