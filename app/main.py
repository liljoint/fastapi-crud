
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from .infrastructure.schemas.userSchemas import UserCreateSchema, UserUpdateSchema
from .infrastructure.crud.crud import CRUD
from .infrastructure.database import Base, engine, get_db


Base.metadata.create_all(bind=engine)

app = FastAPI()
crud = CRUD()

@app.get("/users")
async def listUsers(db: Session = Depends(get_db)):
    return await crud.listUsers(db)

@app.get("/users/{id}")
async def findUser(id: int,  db: Session = Depends(get_db)):
    return await crud.findUser(id, db)
    
@app.post("/users")
async def addUser(user:UserCreateSchema, db: Session = Depends(get_db)):
    return await crud.addUser(user, db)

@app.put("/users/{id}")
async def updateUser(id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):

    return await crud.updateUser(id, user, db)

@app.delete("/users/{id}")
async def deleteUser(id: int, db: Session = Depends(get_db)):
    return await crud.deleteUser(id, db)
