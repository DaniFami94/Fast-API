```bash

# GET:

- El método GET se utiliza para solicitar recursos desde el servidor.
- Cuando escribes una URL en tu navegador y presionas Enter, o cuando refrescas la página, el navegador automáticamente hace una solicitud GET al servidor para obtener el contenido de esa URL.

# POST:

- El método POST se utiliza para enviar datos al servidor, generalmente como parte de un formulario o una solicitud de API que necesita procesar datos en el cuerpo de la solicitud.

- El navegador no utiliza POST al refrescar la página a menos que tú lo configures específicamente, como al enviar un formulario en HTML con el método POST.

# Parametros de ruta

- Un parametro de ruta son valores que podemos pasar dentro de la URL

- con "status_code = " podemos controlar los mensajes de las respuestas

# Middleware

En FastAPI, un middleware es una función que se ejecuta antes y/o después de cada solicitud HTTP. Se usa para modificar la solicitud o la respuesta, agregar funcionalidades globales (como autenticación, logging o manejo de errores), y controlar el flujo de la aplicación.

FastAPI se basa en Starlette, un framework ASGI ligero que gestiona las operaciones HTTP principales, incluyendo enrutamiento, middleware y compatibilidad con WebSockets . Starlette proporciona las herramientas básicas que FastAPI utiliza para gestionar las solicitudes HTTP, lo que lo convierte en una base estable y de alto rendimiento para el desarrollo de aplicaciones web.

Los archivos __init__.py vacíos en tu proyecto FastAPI cumplen funciones importantes aunque no contengan código:
Marcar Directorios como Paquetes Python
Los archivos __init__.py convierten los directorios models, routes y utils en paquetes Python
Esto permite usar importaciones relativas entre módulos
Sin estos archivos, Python no trataría estos directorios como paquetes


Jinja2Templates en FastAPI permite renderizar HTML dinámico usando Jinja2, ideal para aplicaciones web con contenido generado en Python, Jinja2 permite usar variables, bucles, condicionales y filtros dentro del HTML.

#Dependencies

La inyección de dependencias nos va a servir para evitar duplicar código y reutilizar una funcionalidad ya existente de una función, como por ejemplo una función de "path operation de tipo: get,post,delete,update"

*pip install motor pymongo: dependencia necesaria para que funcione mongoDB*


OAuth 2.0, que significa “Open Authorization” (autorización abierta), es un estándar diseñado para permitir que un sitio web o una aplicación accedan a recursos alojados por otras aplicaciones web en nombre de un usuario.

JSON Web Token (JWT) es un estándar abierto que permite transmitir información de forma segura entre partes. Los JWT se utilizan para autenticar usuarios y compartir información.

Un token bearer, o token al portador, es un tipo de token que permite a quien lo posee acceder a recursos protegidos. Se utiliza en aplicaciones web y APIs.

```
