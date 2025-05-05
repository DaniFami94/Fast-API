import datetime
from pydantic import BaseModel, Field

class User(BaseModel):  # definimos el esquema de la clase User, lo usamos para validar y consultar datos, , User hereda de BaseModel
    id: int  # añadimos los atributos de la clase User
    username: str
    email: str
    password: str
    creation_date: str

class UserCreate(BaseModel):
    id:int
    username: str = Field(min_length = 5, max_length = 15,)  # añadimos validaciones de longitud
    email: str = Field(min_length = 5, max_length = 15,)  # añadimos validaciones de longitud
    password: str = Field(min_length = 5, max_length = 25,)  # añadimos validaciones de longitud
    creation_date: str = Field(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # código para saber cuando se ha creado un usuario
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "username": "my_user",
                "email": "my_email",
                "password": "my_password",
                "creation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        }
    }

class UserUpdate(BaseModel):
    username:str
    email:str
    password:str