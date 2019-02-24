import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre_producto):  
        productos = config.model_productos.select_nombre_producto(nombre_producto) # Selecciona el registro que coincida con nombre
        return config.render.view(productos) # Envia el registro y renderiza view.html
