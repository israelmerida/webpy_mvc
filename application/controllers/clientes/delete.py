import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre_cliente): 
        clientes = config.model_clientes.select_nombre(nombre_cliente) # Selecciona el registro que coincida con nombre
        return config.render.delete(clientes) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre_cliente):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre_cliente = formulario['nombre_cliente'] # Obtine el nombre almacenado en el formulario
        config.model_clientes.delete_clientes(nombre_cliente) # Borra el registro del nombre seleccionado
        raise web.seeother('/clientes') # Redirecciona a raiz
