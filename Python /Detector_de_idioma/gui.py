import tkinter as tk
from tkinter import Tk, Label, Text, Button, END
from logica import detect_language

'''Diccionario de idiomas'''
idiomas = {
    "es": "Español",
    "en": "Inglés",
    "fr": "Francés",
    "de": "Alemán",
    "it": "Italiano",
    "pt": "Portugués",
    "ca": "Catalán",
    "eu": "Euskera",
    "gl": "Gallego",
    "nl": "Neerlandés",
    "sv": "Sueco",
    "no": "Noruego",
    "da": "Danés",
    "fi": "Finés",
    "pl": "Polaco",
    "cs": "Checo",
    "sk": "Eslovaco",
    "hu": "Húngaro",
    "ru": "Ruso",
    "zh": "Chino"
}


'''Crecion de funciones'''
def iniciar_prueba():

    texto = entrada_usuario.get("1.0", "end-1c")
    lng = detect_language(texto)
    texto_idioma = idiomas.get(lng,'Desconocido')

    #Crear el TopLavel,ventana de resultados:
    resultado = tk.Toplevel(ventana)
    resultado.title('IDIOMA')
    resultado.geometry("600x150")

    label_resultado = tk.Label(resultado,text=f'{texto_idioma}')
    label_resultado.pack(pady=10)

    #Cerrar Toplabel
    boton_cerrar = tk.Button(resultado,text='Cerrar',command=
                            lambda: cerrar_resultado(resultado))
    boton_cerrar.pack(pady=10)

def cerrar_resultado(resultado):
    resultado.destroy()
    entrada_usuario.delete("1.0", "end")


''' Interfaz gráfica para el detector de idioma '''

ventana = tk.Tk()
ventana.title('Detector de idioma')
ventana.geometry("600x400")

entrada_usuario = tk.Text()
entrada_usuario.pack(pady=10) 
entrada_usuario.focus_force()


boton_inicio = tk.Button(ventana,text='Buscar idioma',command= iniciar_prueba)
boton_inicio.pack()


ventana.mainloop()
    