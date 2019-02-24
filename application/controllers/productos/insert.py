import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre_producto = formulario['nombre_producto'] # alamcena el nombre escrito en el input
        neto = formulario['neto'] # almacena el neto escrito en el input
        marca = formulario['marca'] # alamcena la marca escrito en el input
        precio = formulario['precio'] # alamcena el precio escrito en el input
        config.model_productos.insert_productos(nombre_producto,neto,marca,precio) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
