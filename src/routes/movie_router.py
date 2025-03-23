from typing import List
from fastapi import Path, Query, APIRouter
from fastapi.responses import FileResponse, JSONResponse
from src.models.movie_models import Movie,MovieCreate, MovieUpdate

movies: List[Movie] = []  # Creamos una lista de peliculas vacia

movie_router = APIRouter()  # Creamos un router

# Creación de rutas y endpoints

# En FastAPI, el orden de las rutas importa: las rutas más específicas deben ir antes que las más generales. by_category debe ir antes que {id} para que no se confunda con un id. Si se pone {id} primero, FastAPI lo interpretará como una categoría y no como un id y generará un error.


@movie_router.get("/", tags=["Movies"], status_code = 200, response_description = "Nos debe devolver una respuesta exitosa") 
def get_movies() -> List[Movie]:  # añadimos la lista de peliculas
   content = [movie.model_dump() for movie in movies]
   return JSONResponse(content = content, status_code = 200)  # Convertimos la lista de diccionarios a una lista de objetos Movie, usamos la clase JSONResponse para devolver la respuesta en formato JSON


@movie_router.get("/by_category", tags=["Movies"])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:  # declaramos parámetro query dentro de la función y su tipo
      
    for movie in movies:
        if movie.category == category:  # Si la categoria de la pelicula coincide con la categoria de la query
            return JSONResponse(content = movie.model_dump(), status_code = 200)  # model_dump() es un método que convierte el diccionario a un objeto Movie, JSONResponse convierte el diccionario a un objeto JSON
    return JSONResponse(content = {}, status_code = 404)  # si no coincide con ningún id, status_code 404 es un error de no encontrado

@movie_router.get("/{id}", tags=["Movies"])  # definimos parametro de ruta {id}
def get_movie(id: int = Path(gt=0),) -> Movie | dict:  # añadimos validación por parametro de id "gt" significa que el valor debe ser mayor a 0 añadimos id como parametro de la función
    for movie in movies:  # recorremos el array movies
        if movie.id == id:  # Si es igual a dicho id,  devuelve el diccionario
           return JSONResponse(content = movie.model_dump(), status_code = 200)  # model_dump() es un método que convierte el diccionario a un objeto Movie, JSONResponse convierte el diccionario a un objeto JSON
    return JSONResponse(content = {}, status_code = 404)  # si no coincide con ningún id

# 'http://192.168.0.157:8000/movies/?category=comedia&year=2022' respuesta de un parametro query vemos que empieza con ? y separa los elementos con &

# Método POST
@movie_router.post("/", tags=["Movies"])
def create_movie(movie: MovieCreate,) -> List[Movie]:  # añadimos el parametro movie de tipo Movie
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]  
    return JSONResponse(content = content, status_code = 201) # status_code 201 es un mensaje de creado, se usa para indicar que se ha creado un nuevo recurso
    #return RedirectResponse('/movies', status_code = 303)  # el código 303 es una redirección en nuestra aplicación, hay que ponerlo para evitar error de CORS

# Método PUT para actualizar datos
@movie_router.put("/{id}", tags=["Movies"])
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
@movie_router.delete("/{id}", tags=["Movies"])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)  # Eliminamos la pelicula que coincida con el id actual
    content = [movie.model_dump() for movie in movies] 
    return JSONResponse(content = content, status_code = 200)


@movie_router.get('/get_file') # ruta para descargar un archivo
def get_file():
    return FileResponse('CV Daniel Famiglietti.pdf') # devuelve un archivo en la ruta especificada

# video 17
