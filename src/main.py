from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse,PlainTextResponse,RedirectResponse,FileResponse
from pydantic import BaseModel, Field, validator
from typing import List, Optional
import datetime
from src.routes.movie_router import movie_router # importamos el router de movie_router

# Creamos la aplicación
app = FastAPI()



@app.get("/", tags=["Home"])  # endPoint para la ruta home
def home():
    return PlainTextResponse(content = "Te amo Mariester", status_code = 200)  # Respuesta del servidor, status_code 200 es un mensaje de éxito


app.include_router(prefix='/movies', router= movie_router)