from sqlalchemy import Column, String, DateTime, Integer, Boolean
from sqlalchemy.sql import func
from ..database.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index = True, autoincrement = True)
    name = Column(String, nullable = True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=True)
    status = Column(Boolean,default=True) 
    created_at = Column(DateTime(timezone=True), default = datetime.now() )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
