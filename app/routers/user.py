from fastapi import APIRouter
from app.schemas import User

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

users = []

@router.get("/")
def get_users():
    return users

@router.post("/")
def create_user(user:User):
    user = user.dict()
    users.append(user)
    print(user)
    return {"Notification":"User created succesfully"}

@router.get("/{user_id}")
def get_user(user_id:int):
    for user in users:
        print(user,type(user))
        if user["id"] == user_id:
            return {"user":user}
    return {"Notification":"User not found"}

@router.delete("/{user_id}")
def delete_user(user_id:int):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            users.pop(index)
            return {"Notification":"User deleted succesfully"}
    return {"Notification":"User not found or does not exists"}

@router.put("/{user_id}")
def update_user(user_id:int,updateUser:User):
    for index,user in enumerate(users):
        if user["id"] == user_id:
            users[index]["title"] = updateUser.dict()["title"]
            users[index]["content"] = updateUser.dict()["content"]
            users[index]["author"] = updateUser.dict()["author"]
            return {"Notification":"User updated succesfully"}
    return {"Notification":"User not found or does not exists"}