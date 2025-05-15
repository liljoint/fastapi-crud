
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from ...infrastructure.database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean, default=False)
    
    
