from pydantic import BaseModel


class UserCreateSchema(BaseModel):
        username: str  = None
        email: str = None
        first_name: str = None
        last_name: str = None
        role: str = None
        active: bool = None
        
class UserUpdateSchema(BaseModel):
        username: str
        email: str
        first_name: str
        last_name: str
        role: str
        active: bool
