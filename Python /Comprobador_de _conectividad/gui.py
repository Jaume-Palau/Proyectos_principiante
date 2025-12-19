import tkinter as tk
from tkinter import messagebox
from logica import comprobar_conexion

'''CREACION DE FUNCIONES'''
def iniciar_prueba():
    url = entrada_usuario.get()
    resp = comprobar_conexion(url)
    if resp == 200:
        mensaje = 'Web operativa'
    elif resp == 404:
        mensaje = 'No existe la pagina'
    else:
        mensaje = None

    # Crear TopLevel (ventana de resultados)
    resultado = tk.Toplevel(ventana)
    resultado.title('RESPUESTA')
    label_resultado1 = tk.Label(resultado,text=f'{resp}',fg='white')
    label_resultado2 = tk.Label(resultado,text=mensaje,fg='white')
    label_resultado1.pack()
    label_resultado2.pack()

    # Cerrar TopLevel
    boton_cerrar = tk.Button(resultado,text='Cerrar',command=
                             lambda: cerrar_resultado(resultado))
    boton_cerrar.pack()

def cerrar_resultado(resultado):
    resultado.destroy()
    entrada_usuario.delete(0,tk.END)
    boton_inicio.pack()



'''CREACION DE LA INTERFAZ'''

# Creacion de la ventana con titulo:
ventana = tk.Tk()
ventana.title('Comprobador de conexion a web')
ventana.geometry("600x150")

# Entrada del usuario para la url
# Falta poner mensaje... introduzca la url:
entrada_usuario = tk.Entry(ventana,width=50,font=('Arial',12))
entrada_usuario.pack(pady=10)
entrada_usuario.focus_force()

# Creacion del boton de inicio:
boton_inicio = tk.Button(ventana,text='Probar conexion',command=iniciar_prueba)
boton_inicio.pack()

ventana.mainloop()