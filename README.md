```python

#  uvicorn main:app --host 192.168.0.157 --reload , comando para ejecutar la aplicación, es accesible desde cualquier dispositivo que este en el rango de la IP

# GET:

- El método GET se utiliza para solicitar recursos desde el servidor.
- Cuando escribes una URL en tu navegador y presionas Enter, o cuando refrescas la página, el navegador automáticamente hace una solicitud GET al servidor para obtener el contenido de esa URL.

# POST:

- El método POST se utiliza para enviar datos al servidor, generalmente como parte de un formulario o una solicitud de API que necesita procesar datos en el cuerpo de la solicitud.

- El navegador no utiliza POST al refrescar la página a menos que tú lo configures específicamente, como al enviar un formulario en HTML con el método POST.

# Parametros de ruta

- Un parametro de ruta son valores que podemos pasar dentro de la URL

# Parametros query

sintaxis localhost:8000/movies/?id=123

http://192.168.0.157:8000/
http://192.168.0.157:8000/docs #para ver las rutas de la API

- con "status_code = " podemos controlar los mensajes de las respuestas 