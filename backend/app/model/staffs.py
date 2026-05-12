from sqlalchemy import Column, String, DateTime, Integer, Boolean
from sqlalchemy.sql import func
from ..database.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Staffs(Base):
    __tablename__ = "staffs"

    id = Column(Integer, primary_key=True)  
    name = Column(String, nullable = False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable= False)
    password = Column(String, nullable=False)
    status = Column(Boolean,default=True, nullable = False) 
    created_at = Column(DateTime(timezone=False), default = datetime.now() )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
