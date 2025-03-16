from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse,PlainTextResponse,RedirectResponse,FileResponse
from pydantic import BaseModel, Field, validator
from typing import List, Optional
import datetime

# Creamos la aplicación
app = FastAPI()

# Creación de esquemas de datos#####################################################################################################


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


########################################################################################################################################

movies: List[Movie] = []  # Creamos una lista de peliculas vacia


# Método GET
# Creación de rutas y endpoints
@app.get("/", tags=["Home"])  # endPoint para la ruta home
def home():
    return PlainTextResponse(content = "Te amo Mariester", status_code = 200)  # Respuesta del servidor, status_code 200 es un mensaje de éxito


@app.get("/movies", tags=["Movies"], status_code = 200, response_description = "Nos debe devolver una respuesta exitosa") 
def get_movies() -> List[Movie]:  # añadimos la lista de peliculas
   content = [movie.model_dump() for movie in movies]
   return JSONResponse(content = content, status_code = 200)  # Convertimos la lista de diccionarios a una lista de objetos Movie, usamos la clase JSONResponse para devolver la respuesta en formato JSON


@app.get("/movies/{id}", tags=["Movies"])  # definimos parametro de ruta {id}
def get_movie(id: int = Path(gt=0),) -> Movie | dict:  # añadimos validación por parametro de id "gt" significa que el valor debe ser mayor a 0 añadimos id como parametro de la función
    for movie in movies:  # recorremos el array movies
        if movie.id == id:  # Si es igual a dicho id,  devuelve el diccionario
           return JSONResponse(content = movie.model_dump(), status_code = 200)  # model_dump() es un método que convierte el diccionario a un objeto Movie, JSONResponse convierte el diccionario a un objeto JSON
    return JSONResponse(content = {}, status_code = 404)  # si no coincide con ningún id


@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:  # declaramos parámetro query dentro de la función y su tipo
    for movie in movies:
        if (movie.category == category):  # Si la categoria de la pelicula coincide con la categoria de la query
            return JSONResponse(content = movie.model_dump(), status_code = 200)  # model_dump() es un método que convierte el diccionario a un objeto Movie, JSONResponse convierte el diccionario a un objeto JSON
    return JSONResponse(content = {}, status_code = 404)  # si no coincide con ningún id, status_code 404 es un error de no encontrado



# 'http://192.168.0.157:8000/movies/?category=comedia&year=2022' respuesta de un parametro query vemos que empieza con ? y separa los elementos con &


# Método POST
@app.post("/movies", tags=["Movies"])
def create_movie(movie: MovieCreate,) -> List[Movie]:  # añadimos el parametro movie de tipo Movie
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]  
    return JSONResponse(content = content, status_code = 201) # status_code 201 es un mensaje de creado, se usa para indicar que se ha creado un nuevo recurso
    #return RedirectResponse('/movies', status_code = 303)  # el código 303 es una redirección en nuestra aplicación, hay que ponerlo para evitar error de CORS

# Método PUT para actualizar datos
@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:  # añadimos el parametro id y movieUpdate
    for item in movies:
        if item.id == id: # accedemos a los atributos de la clase Movie
            item.title = movie.title
            item.overview = movie.overview
            item.year = movie.year
            item.rating = movie.rating
            item.category = movie.category
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content = content, status_code = 200)


# Método DELETE para eliminar datos
@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)  # Eliminamos la pelicula que coincida con el id actual
    content = [movie.model_dump() for movie in movies] 
    return JSONResponse(content = content, status_code = 200)


@app.get('/get_file') # ruta para descargar un archivo
def get_file():
    return FileResponse('CV Daniel Famiglietti.pdf') # devuelve un archivo en la ruta especificada

# video 16 