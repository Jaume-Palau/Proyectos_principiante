'''En este archivo se encuentra la configuracion del GUI (graphic user interface)'''
'''VENTANA PRINCIPAL'''

import tkinter as tk
from tkinter import messagebox
from funciones_basicas import frase_random,iniciar_temporizador,calcular_tiempo

#####################################

'''CREACION DE FUNCIONES'''

def iniciar_prueba():
    '''Cuando pulsan el boton de inicio,genera una frase random,
    limpia la etiqueta donde escribe el usuario,muestra la nueva frase,
    centra el cursor directo para escribir, ocula el boton e inicia el tiempo'''

    frase_rnd = frase_random()
    # Modificar etiqueta en pantalla:
    etiqueta_frase.config(text=frase_rnd)
    # Limpiar campo de usuario
    entrada_usuario.delete(0,tk.END)
    entrada_usuario.focus()
    # Ocultar el boton de inicair:
    boton_inicio.pack_forget()
    # Iniciar temporizador:
    iniciar_temporizador()


def finalizar_prueba():
    '''Cuando pulsan el boton de fin de prueba,hace la comprobacion del resultado,
    mide el tiempo total, crea el toplevel donde muestra los resultados'''
    # Comprobar la frase:
    texto_usuario = entrada_usuario.get()
    frase_correcta = etiqueta_frase.cget('text')
    if texto_usuario == frase_correcta:
        correcto = True
    else:
        correcto = False

    # Medir el tiempo final:
    tiempo_total = calcular_tiempo()

    # Crear el Toplevel(ventana de resultados)
    resultado = tk.Toplevel(ventana)
    resultado.title('RESULTADO')
    label_resultado = tk.Label(resultado,text= 'Correcto' if correcto else 'Incorrecto')
    label_tiempo = tk.Label(resultado,text=f'Tiempo\n{tiempo_total:.2f} segundos')
    label_resultado.pack()
    label_tiempo.pack()

    # Crear el boton para cerrar el Toplavel
    boton_cerrar = tk.Button(resultado,text='Cerrar', 
                             command=lambda:cerrar_resultado(resultado))
    boton_cerrar.pack()

def cerrar_resultado(resultado):
    '''Cuando se pulsa el boton de cerrar el Toplavel,reinicia todo para 
    dejarlo como al principio'''
    # Cerrar la ventana de resultados:
    resultado.destroy()
    # Limpiar la etiqueta del texto de usuario:
    entrada_usuario.delete(0,tk.END)
    # Volver a mostrar el boton de inicio:
    boton_inicio.pack(before=entrada_usuario)

#####################################

'''CREACION DE LA INTERFAZ'''

# Crear ventana principal:
ventana = tk.Tk()

# Crear titulo:
ventana.title('Prueba de escritura veloz')

# Crear etiqueta vacia para la frase random:
etiqueta_frase = tk.Label(ventana,text='',font=('Arial',14))
etiqueta_frase.pack()
# Crear boton inicio de prueba: (ejecuta iniciar_prueba())
boton_inicio = tk.Button(ventana,text='Iniciar prueba', command=iniciar_prueba)
boton_inicio.pack()

# Campo de entrada del usuario: (donde el usuario escribe la frase)
entrada_usuario = tk.Entry(ventana,width=50,font=('Arial',12))
entrada_usuario.pack(pady=10)

# Crear el boton fin de prueba: (ejecuta finalizar_prueba())
boton_fin = tk.Button(ventana,text='Finalizar prueba', command=finalizar_prueba)
boton_fin.pack()

# Bucle principal: SIEMPRE DEBE SER LA ULTIMA LINIA DEL ARCHIVO!! (mantiene la ventana abierta)
ventana.mainloop()