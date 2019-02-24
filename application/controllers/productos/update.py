import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre_producto): 
        productos = config.model_productos.select_nombre(nombre_producto) # Selecciona el registro que coincida con nombre
        return config.render.update(productos) # Envia el registro y renderiza update.html
    
    def POST(self,nombre_producto):
        formulario = web.input() # almacena los datos del formulario web
        nombre_producto = formulario['nombre_producto'] # alamcena el nombre escrito en el input
        neto = formulario['neto'] # almacena el neto escrito en el input
        marca = formulario['marca'] # alamcena la marca escrito en el input
        precio = formulario['precio'] # alamcena el precio escrito en el input
        config.model_productos.update_productos(nombre_producto,neto,marca,precio)
        raise web.seeother('/') # redirecciona al index


