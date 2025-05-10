from typing import List
from fastapi import Path, Query, APIRouter,Depends
from src.dataBase.mongodb_interface import MongoDBInterface
from fastapi.responses import FileResponse, JSONResponse
from src.models.user_models import User,UserCreate, UserUpdate
from fastapi import HTTPException, status

user: List[User] = []  # Creamos una lista de usuarios vacia

user_router = APIRouter()  # Creamos un router

# Dependency para obtener la instancia de MongoDB
async def get_mongodb():
    from src.main import mongodb
    return mongodb


# GET
@user_router.get("/",tags=["Users"],status_code=200,response_description="successfuyl response") # definimos el endpoint para obtener todos los usuarios
async def get_users(mongodb: MongoDBInterface = Depends(get_mongodb)) -> List[User]:  # añadimos la lista de usuarios
    users = await mongodb.get_all_users()  # llamamos a la función get_all_users de la clase MongoDBInterface
    return JSONResponse(content = users, status_code = 200)  # Convertimos la lista de diccionarios a una lista de objetos User, usamos la clase JSONResponse para devolver la respuesta en formato JSON

@user_router.get("/{id}", tags=["Users"])  # definimos parametro de ruta {id}
async def get_user_by_id(id: int = Path(gt=0),mongodb: MongoDBInterface = Depends(get_mongodb)) -> User | dict:
    users = await mongodb.get_user_by_id(id)
    if not users:
        return JSONResponse(content = {}, status_code = 404)
    for user in users:
        if user.id == id:
            return JSONResponse(content=user.model_dump(),status_code=200)# model_dump() es un método que convierte el diccionario a un objeto User, JSONResponse convierte el diccionario a un objeto JSON
        return JSONResponse(content={}, status_code=404)

# POST

@user_router.post("/",tags=["Users"])
async def create_user(user: UserCreate, mongodb: MongoDBInterface = Depends(get_mongodb)) -> List[User]:
    user_data = user.model_dump()    
    result = await mongodb.create_user(user_data)
    if result:
        return JSONResponse(
            content={"message": "User created", "id": str(result)},
            status_code=201
        )
    return JSONResponse(
        content={"message":"Error creating user"},
        status_code = 400
    )

# PUT

@user_router.put("/{id}",tags=["Users"]) # modificar esta ruta para que cambie la contraseña del usuario!!!
async def update_user(id: int = Path(gt=0), user: UserUpdate = Depends(),mongodb: MongoDBInterface = Depends(get_mongodb)) -> User | dict:
    user_data = user.model_dump()
    users = await mongodb.update_user(id, user_data)
    if not users:
        return JSONResponse(content = {}, status_code = 404)
    for user in users:
        if user.id == id:
            return JSONResponse(content=user.model_dump(),status_code=200)
        return JSONResponse(content={}, status_code=404)


# DELETE

@user_router.delete("/{id}",tags=["Users"])
async def delete_user(id: int = Path(gt=0),mongodb: MongoDBInterface = Depends(get_mongodb)) -> User | dict:
    users = await mongodb.delete_user(id)
    if not users:
        return JSONResponse(content = {}, status_code = 404)
    for user in users:
        if user.id == id:
            return JSONResponse(content=user.model_dump(),status_code=200)
        return JSONResponse(content={}, status_code=404)
    


# @user_router.get("/users")
# def get_users(commons: CommonDep = Depends ()): # vamos a filtrar usuarios que se hayan registrado por un rango de fechas
#    return f"Users created between {commons.start_date} and {commons.end_date}" # retornamos un mensaje con el rango de fechas 

# @app.get("/customers")
# def get_customers(commons: CommonDep = Depends ()): # vamos a filtrar clientes que se hayan registrado por un rango de fechas
#    return f"Customers created between {commons.start_date} and {commons.end_date}" # retornamos un mensaje con el rango de fechas
