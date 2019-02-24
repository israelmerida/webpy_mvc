import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre_cliente): 
        clientes = config.model_clientes.select_nombre(nombre_cliente) # Selecciona el registro que coincida con nombre
        return config.render.update(clientes) # Envia el registro y renderiza update.html
    
    def POST(self,nombre_cliente):
        formulario = web.input() # almacena los datos del formulario web
        nombre_cliente = formulario['nombre_cliente'] # alamcena el nombre escrito en el input
        apellidos_cliente = formulario['apellidos_cliente'] # almacena los apellids escrito en el input
        colonia = formulario['colonia'] # alamcena la colonia escrito en el input
        calle = formulario['calle'] # alamcena el calle escrito en el input
        config.model_clientes.update_clientes(nombre_cliente,apellidos_cliente,colonia,calle)
        raise web.seeother('/clientes') # redirecciona al index


