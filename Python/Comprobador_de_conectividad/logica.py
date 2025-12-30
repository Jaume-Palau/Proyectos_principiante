from urllib import request

# Funcion que comprueba la conexion a la url
def comprobar_conexion(url:str):
    try:
        respuesta = request.urlopen(url)
        codigo = respuesta.getcode()
        return codigo
    
    except Exception as e:
        return f'{e}'