import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_productos():
    try:
        return db.select('productos') # Selecciona todos los registros de la tabla productos
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_nombre(nombre_producto):
    try:
        return db.select('productos',where='nombre_producto=$nombre_producto', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro 
'''
def insert_productos(nombre_producto,neto,marca,precio):
    try:
        return db.insert('productos', nombre_producto=nombre_producto,neto=neto,marca=marca,precio=precio) # inserta un registro en producto
    except Exception as e:
        print "Model insert_productos Error {}".format(e.args)
        print "Model insert_productos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_productos(nombre_producto):
    try:
        return db.delete('productos', where='nombre_producto=$nombre_producto',vars=locals()) # borra un registro de producto
    except Exception as e:
        print "Model delete_producto Error {}".format(e.args)
        print "Model delete_producto Message {}".format(e.message)
        return None

'''
Metodo para actualizar los datos, del nombre recibido
'''
def update_productos(nombre_producto,neto,marca,precio): # actualiza el email de personas que coincidan con el nombre
    try:
        return db.update('productos', 
            neto=neto,
            marca=marca,
            precio=precio, 
            where='nombre_producto=$nombre_producto',
            vars=locals())
    except Exception as e:
        print "Model update_producto Error {}".format(e.args)
        print "Model update_producto Message {}".format(e.message)
        return None
