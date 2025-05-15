from datetime import datetime
from sqlalchemy.orm import Session
from ...infrastructure.schemas.userSchemas import UserCreateSchema
from ...infrastructure.models.user import Users

class CRUD:
    async def listUsers(self, db: Session):
        return db.query(Users).all()

    async def findUser(self, id: int, db: Session):
        return db.query(Users).filter(Users.id == id).first()
        
    async def addUser(self,user: UserCreateSchema, db: Session):
        newUser = Users(
            username = user.username,
            role = user.role,
            first_name  = user.first_name,
            last_name = user.last_name,
            email = user.email,
            active = user.active,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        return user
        
    async def updateUser(self, id: int, user: UserCreateSchema, db: Session):
        userFinded = await self.findUser(id, db)
        if userFinded:
            print(userFinded)
            userFinded.username = user.username
            userFinded.first_name = user.first_name
            userFinded.last_name = user.last_name
            userFinded.active = user.active
            userFinded.email = user.email
            userFinded.updated_at = datetime.now()
            db.commit()
            db.refresh(userFinded)
            return userFinded
        else: 
            return {}

    async def deleteUser(self, id: int, db: Session):
        userFinded = await self.findUser(id, db)
        if userFinded:
            db.delete(userFinded)
            db.commit()
            return True
        else: 
            return False