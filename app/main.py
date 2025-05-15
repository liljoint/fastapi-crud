
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from .infrastructure.schemas.userSchemas import UserCreateSchema, UserUpdateSchema
from .infrastructure.crud.crud import CRUD
from .infrastructure.database import Base, engine, get_db


Base.metadata.create_all(bind=engine)

app = FastAPI()
crud = CRUD()

@app.get("/users", summary="Listar usuarios", description="Permite listar todos los usuarios registrados")
async def listUsers(db: Session = Depends(get_db)):
    return await crud.listUsers(db)

@app.get("/users/{id}", summary="Buscar usuarios", description="Permite buscar un usuario por ID")
async def findUser(id: int,  db: Session = Depends(get_db)):
    return await crud.findUser(id, db)
    
@app.post("/users", summary="Crear usuario", description="Permite crear un usuario mediante un objeto")
async def addUser(user:UserCreateSchema, db: Session = Depends(get_db)):
    return await crud.addUser(user, db)

@app.put("/users/{id}", summary="Actualizar usuario", description="Permite actualizar un usuario mediante su ID.")
async def updateUser(id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):

    return await crud.updateUser(id, user, db)

@app.delete("/users/{id}", summary="Borrar usuario", description="Permite borrar un usuario.")
async def deleteUser(id: int, db: Session = Depends(get_db)):
    return await crud.deleteUser(id, db)
