from fastapi import FastAPI, status
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response 



class HTTPErrorHandler(BaseHTTPMiddleware): # Creamos la clase HTTPErrorHandler que nos permitirá manejar los errores de la aplicación
    
    def __init__ (self, app: FastAPI) -> None: # constructor de la clase HTTPErrorHandler que recibe un objeto de tipo FastAPI y no devuelve nada 
        super().__init__(app) # llamamos al constructor de la clase padre BaseHTTPMiddleware por eso usamos super() y le pasamos el objeto app

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse: # método dispatch que recibe dos parámetros request y call_next y devuelve un objeto de tipo Response o JSONResponse
        
        try:
        
           return await call_next(request) # retornamos el resultado de la función call_next que recibe el objeto Request
        
        except Exception as e: # si hay un error en la aplicación, se ejecutará el bloque de código dentro del except
            
            content = f"exc: {str(e)}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content = content, status_code = status_code)