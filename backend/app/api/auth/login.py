from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ...model.users import Users
from ...schema import UserLoginSchema as LoginRequest
from ...database.database import get_db
from ...utils.response import *
from ...utils.jwt_token import create_access_token

router = APIRouter()

@router.post("/login")
async def login_user(user: LoginRequest, db: AsyncSession = Depends(get_db)):

    query = select(Users).filter(
        (Users.email == user.email)
    )
    existing_user = await db.execute(query)
    existing_user = existing_user.scalar()
    
    if not existing_user:
        return await response_404(data="Account")
    
    if existing_user.status != True:
        return await response_404(detials="Account Not found")
    
    # Verify the password
    if existing_user.password != user.password:
        return await response_401(data="Wrong Password")
    # Create access and refresh tokens
    access_token = await create_access_token(data={"sub": existing_user.email,"id":existing_user.id})
    
    return await response_201(data= {
            "token_type": "bearer",
            "access_token": access_token,
        }
    )
