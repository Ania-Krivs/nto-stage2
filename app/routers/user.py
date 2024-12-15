from fastapi import APIRouter, HTTPException
from app.data.models import User
from app.data import schemas
from datetime import datetime

router = APIRouter(prefix="/store", tags=["users-controller"])

@router.post('/user')
async def Add_user(request: schemas.RequestUser) -> schemas.ResponseUser:
    users = await User.find_all().to_list()
    if not users:
        id = 1
    else:            
        for u in users:
            id_list = []
            id_list.append(u.id) 
        
        id = max(id_list) + 1
        
    user = User(
        id=id,
        userName=request.userName,
        password=request.password,
        firstName=request.firstName,
        lastName=request.lastName,
        telephone=request.telephone,
        createdAt=datetime.now(),
        modifiedAt=datetime.now()
    )
    
    await user.create()
    
    return schemas.ResponseUser(
        id=user.id,
        userName=user.userName,
        password=user.password,
        firstName=user.firstName,
        lastName=user.lastName,
        telephone=user.telephone,
        createdAt=user.createdAt,
        modifiedAt=user.modifiedAt
    )

@router.get('/user')
async def Get_user_with_id(id: int) -> schemas.ResponseUser:
    user = await User.find_one(User.id == id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return schemas.ResponseUser(
        id=user.id,
        userName=user.userName,
        password=user.password,
        firstName=user.firstName,
        lastName=user.lastName,
        telephone=user.telephone,
        createdAt=user.createdAt,
        modifiedAt=user.modifiedAt
    ) 
    
    
@router.put('/user')
async def Update_user_with_id(request: schemas.RequestUser) -> schemas.ResponseUser:
    user = await User.find_one(User.userName == request.userName)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.userName = request.userName
    user.password = request.password
    user.firstName = request.firstName
    user.lastName = request.lastName
    user.telephone = request.telephone
    user.modifiedAt = datetime.now()
    
    await user.save()
    
    return schemas.ResponseUser(
        id=user.id,
        userName=user.userName,
        password=user.password,
        firstName=user.firstName,
        lastName=user.lastName,
        telephone=user.telephone,
        createdAt=user.createdAt,
        modifiedAt=user.modifiedAt
    ) 
    
    
@router.delete('/user')
async def Delete_user_with_id(id: int) -> schemas.ResponseUser:
    user = await User.find_one(User.id == id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    await user.delete()
    
    return schemas.ResponseUser(
        id=user.id,
        userName=user.userName,
        password=user.password,
        firstName=user.firstName,
        lastName=user.lastName,
        telephone=user.telephone,
        createdAt=user.createdAt,
        modifiedAt=user.modifiedAt
    ) 