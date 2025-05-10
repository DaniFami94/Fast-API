from fastapi import FastAPI, Query, Request, Depends,Form
from src.dataBase.mongodb_interface import MongoDBInterface
from fastapi.responses import PlainTextResponse, JSONResponse
from src.routes.login_router import login_router
from src.routes.movie_router import movie_router # importamos el router de movie_router
from src.routes.user_router import user_router # importamos el router de user_router
from src.routes.login_router import login_router # importamos el router de login_router
from typing import Annotated
import os
from src.utils.http_error_handler import HTTPErrorHandler # importamos la clase HTTPErrorHandler
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

app = FastAPI() # Creamos la aplicación, podemos utilizar dependencias globales para todos los endpoints 

app.add_middleware(HTTPErrorHandler) # Otra manera de añadir el middleware a la aplicación con starlette
#app.middleware("http") # se puede usar el middleware de esta manera directa con FASTAPI 

# instancia de MongoDB para inicializar la conexión a la base de datos
mongodb = MongoDBInterface()

@app.on_event("startup") # evento de inicio de la aplicación
async def startup_db_client():
    await mongodb.connect()

@app.on_event("shutdown") # evento de cierre de la aplicación
async def shutdown_db_client():
    await mongodb.close()



# Middleware para manejar errores
async def http_error_handler(request:Request,call_next) -> Request | JSONResponse: # definimos el middleware que recibe dos parámetros request y call_next y devuelve un objeto de tipo Request o JSONResponse
 print("Middleware is running")
 return await call_next(request) # retornamos el resultado de la función call_next que recibe el objeto Request 



# dependencia common_params
# def common_params(start_date:str, end_date:str): # creamos una función que recibe dos parámetros start_date y end_date, esta función actua como dependencia para los endpoints
#     return {"start_date": start_date, "end_date":end_date} # retornamos los parámetros como un diccionario 

# CommonDep = Annotated[dict,Depends(common_params)] # creamos una variable de tipo Annotated que contiene el tipo de dato de la función common_params y la dependencia de la función common_params, esta variable se usará como parámetro en los endpoints


# class CommonDep:# creamos la clase CommonDep que va a funcionar como dependencia para los endpoints 
#    def __init__(self, start_date: str, end_date: str):
#       self.start_date = start_date
#       self.end_date = end_date

# Rutas de la aplicación
app.include_router(prefix='/login', router = login_router)
app.include_router(prefix='/movies', router = movie_router)
app.include_router(prefix='/users', router = user_router) 


#crear login de usuario
