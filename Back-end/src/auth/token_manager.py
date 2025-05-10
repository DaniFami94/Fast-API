from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from src.dataBase.mongodb_interface import MongoDBInterface
from datetime import datetime, timedelta
from jose import jwt
import os
from dotenv import load_dotenv
# poner en este archivo solo las funciones para generar token y login

# Load environment variables from .env.development

load_dotenv('.env.development')

# Get environment variables with fallback values
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-secret-key")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def encode_token(payload: dict) -> str:
    to_encode = payload.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )



