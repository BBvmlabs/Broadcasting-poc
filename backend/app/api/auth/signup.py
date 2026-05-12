from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ...model.users import Users
from ...schema import UserSchema
from ...database.database import get_db
import uuid
from datetime import datetime, timedelta
from ...utils.response import *

router = APIRouter()

temp_user_db = {}

@router.post("/register")
async def register_user(data: UserSchema ,db: AsyncSession = Depends(get_db)):

    existing_user = await db.execute(
        select(Users).filter(Users.email == data.email)
    )
    existing_user = existing_user.scalar()
    if existing_user:
        return await response_409("User")

    
    new_user = Users(
        name = data.name,
        email= data.email,
        password = data.password
    )

    db.add(new_user)
    await db.commit()
    
    return await response_201(detials="User Created")
