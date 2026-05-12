from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ...model.staffs import Staffs
from ...schema import StaffSchema
from ...database.database import get_db
import uuid
from datetime import datetime, timedelta
from ...utils.response import *

router = APIRouter()

@router.post("/register")
async def register_user(data: StaffSchema ,db: AsyncSession = Depends(get_db)):

    existing_user = await db.execute(
        select(Staffs).filter(Staffs.email == data.email)
    )
    existing_user = existing_user.scalar()
    if existing_user:
        return await response_409("User")

    
    new_user = Staffs(
        name = data.name,
        email= data.email,
        department = data.department,
        password = data.password
    )

    db.add(new_user)
    await db.commit()
    
    return await response_201(detials="User Created")
