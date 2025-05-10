from typing import List
from fastapi import Path, Query, APIRouter,Depends
from src.dataBase.mongodb_interface import MongoDBInterface
from fastapi.responses import FileResponse, JSONResponse
from src.models.movie_models import Movie,MovieCreate, MovieUpdate

movies: List[Movie] = []  # Creamos una lista de peliculas vacia

movie_router = APIRouter()  # Creamos un router

# Dependency para obtener la instancia de MongoDB
async def get_mongodb():
    from src.main import mongodb
    return mongodb

# Creación de rutas y endpoints

# En FastAPI, el orden de las rutas importa: las rutas más específicas deben ir antes que las más generales. by_category debe ir antes que {id} para que no se confunda con un id. Si se pone {id} primero, FastAPI lo interpretará como una categoría y no como un id y generará un error.

@movie_router.get("/", tags=["Movies"], status_code = 200, response_description = "Nos debe devolver una respuesta exitosa") 
async def get_movies(mongodb: MongoDBInterface = Depends(get_mongodb)) -> List[Movie]:  # añadimos la lista de peliculas
   movies = await mongodb.get_all_movies()
   return JSONResponse(content = movies, status_code = 200)  # Convertimos la lista de diccionarios a una lista de objetos Movie, usamos la clase JSONResponse para devolver la respuesta en formato JSON


@movie_router.get("/by_category", tags=["Movies"])
async def get_movie_by_category( category: str = Query(min_length=5, max_length=20),mongodb: MongoDBInterface = Depends(get_mongodb)) -> Movie | dict:
    movies = await mongodb.get_movies_by_category(category)
    if movies:
        return JSONResponse(content=movies, status_code=200)
    return JSONResponse(content={}, status_code=404)

@movie_router.get("/{id}", tags=["Movies"])  # definimos parametro de ruta {id}
async def get_movie(id: int = Path(gt=0),mongodb: MongoDBInterface = Depends(get_mongodb)) -> Movie | dict:  # añadimos validación por parametro de id "gt" significa que el valor debe ser mayor a 0 añadimos id como parametro de la función
    movies = await mongodb.get_movie_by_id(id)  # llamamos a la función get_movie_by_id de la clase MongoDBInterface
    if not movies:  # si no hay peliculas
        return JSONResponse(content = {}, status_code = 404)  # devolvemos un error 404
    for movie in movies:  # recorremos la lista de peliculas
        if movie.id == id:  # Si es igual a dicho id,  devuelve el diccionario
           return JSONResponse(content = movie.model_dump(), status_code = 200)  # model_dump() es un método que convierte el diccionario a un objeto Movie, JSONResponse convierte el diccionario a un objeto JSON
    return JSONResponse(content = {}, status_code = 404)  # si no coincide con ningún id

# 'http://192.168.0.157:8000/movies/?category=comedia&year=2022' respuesta de un parametro query vemos que empieza con ? y separa los elementos con &

# Método POST
@movie_router.post("/", tags=["Movies"])
async def create_movie(movie: MovieCreate, mongodb: MongoDBInterface = Depends(get_mongodb)) -> List[Movie]:  # añadimos el parametro movie de tipo Movie
    movie_data = movie.model_dump()
    result = await mongodb.create_movie(movie_data)  
    if result:
        return JSONResponse(
            content={"message": "Movie created", "id": str(result)},
            status_code=201
        )
    return JSONResponse(
        content={"message": "Error creating movie"},
        status_code=400
    )
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


# Terminar rutas asincronas!!!!!!!