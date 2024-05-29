from fastapi import APIRouter , HTTPException
from models.user import User 
from config.db import conn 
from schemas.user import userEntity , usersEntity
from bson import ObjectId
user = APIRouter() 

#to get all users
@user.get('/')
async def find_all_users():
    return usersEntity(conn.Students.user.find())

#create user
@user.post('/')
async def create_user(user: User):
    #check if student with same roll number is already exist 
    existing_user = conn.Students.user.find_one({"rollNumber": user.rollNumber})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this roll number already exists")
    
    user_dict = user.dict()
    user_dict['marks'] = user.marks.dict()  # Convert Marks object to dict
    conn.Students.user.insert_one(user_dict)
    return usersEntity(conn.Students.user.find())
    
#update user with roll number
@user.put('/{rollNumber}')
async def update_user(rollNumber: int,user: User):
    user_dict = user.dict()
    user_dict['marks'] = user.marks.dict()  # Convert Marks object to dict
    
    result = conn.Students.user.find_one_and_update({"rollNumber": rollNumber}, {
        "$set": user_dict
    }, return_document=True)
    
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return userEntity(result)
    
#delete user with roll number 
@user.delete('/{rollNumber}')
async def delete_user(rollNumber :int,user: User):
    user_dict = user.dict()
    user_dict['marks'] = user.marks.dict()  # Convert Marks object to dict
    
    result = conn.Students.user.find_one_and_delete({"rollNumber": rollNumber})
    
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return userEntity(result)
    