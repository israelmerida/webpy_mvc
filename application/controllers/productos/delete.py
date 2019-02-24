import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre_producto): 
        productos = config.model_productos.select_nombre(nombre_producto) # Selecciona el registro que coincida con nombre
        return config.render.delete(productos) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre_producto):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre_producto = formulario['nombre_producto'] # Obtine el nombre almacenado en el formulario
        config.model_productos.delete_productos(nombre_producto) # Borra el registro del nombre seleccionado
        raise web.seeother('/') # Redirecciona a raiz
