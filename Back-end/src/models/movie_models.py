import datetime
from pydantic import BaseModel, Field


class Movie(BaseModel):# definimos el esquema de la clase Movie, lo usamos para validar y consultar datos, , Movie hereda de BaseModel
    id: int  # añadimos los atributos de la clase Movie
    title: str
    overview: str
    year: int
    rating: float
    category: str


class MovieCreate(BaseModel):  # Modelo para crear una pelicula
    id: int
    title: str = Field(min_length = 5, max_length = 15,)  # añadimos validaciones de longitud
    overview: str = Field(min_length = 10, max_length= 50,)  # añadimos validaciones de longitud
    year: int = Field(le = datetime.datetime.now().year, ge = 1900, default=datetime.datetime.now().year)  # añadimos validaciones de año, este código hace que la validación del año debe ser menor o igual al actual
    rating: float = Field(ge =0 , le = 10,)  # añadimos validaciones de rating
    category: str = Field( min_length = 5, max_length = 20,)  # añadimos validaciones de longitud

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "My movie",
                "overview": "Esta pelicula trata acerca de...",
                "year": datetime.datetime.now().year,
                "rating": 10,
                "category": "Acción",
            }
        }
    }

# @validator("title")  # validaciones personalizadas más avanzadas para title en este caso
# def validate_title(cls,value):
#     if len(value) < 5:
#         raise ValueError("title file must be at least 5 characters")
#     if len(value) > 15:
#         raise ValueError("title file must be at most 15 characters")
#     return value


class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str

