from src.dataBase.mongodb_interface import MongoDBInterface
from fastapi.responses import FileResponse, JSONResponse
from fastapi import Path, Query, APIRouter,Depends, HTTPException, status
from src.auth.token_manager import encode_token, decode_token
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
"""
Annotated es una función que nos permite añadir metadatos a los parámetros de la función, en este caso le estamos diciendo que el parámetro form_data es de tipo OAuth2PasswordRequestForm y que depende de la función Depends()
"""

login_router = APIRouter()  # Creamos un router

async def get_mongodb(): # Dependency para obtener la instancia de MongoDB
    from src.main import mongodb
    return mongodb

@login_router.post("/token", tags=["Auth"])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],mongodb: MongoDBInterface = Depends(get_mongodb)) -> JSONResponse:
    """
    Login endpoint to authenticate users.
    """
    # Aquí iría la lógica de autenticación
    user = await mongodb.get_user_by_credentials(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username")
    if form_data.password != user["password"]:  
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    token = encode_token({
        "username": user["username"],
        "email": user["email"],
        "sub": str(user["id"])  # Add user ID to token claims
    })
    return JSONResponse({
        "access_token": token,
        "token_type": "bearer"
    })

# proteger rutas de usuarios con el token
#crear variable de entorno para el token