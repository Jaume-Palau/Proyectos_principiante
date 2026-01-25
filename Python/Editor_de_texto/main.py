import tkinter as tk
from tkinter import filedialog

class EditorTexto:
    def __init__(self):
        self.ruta_actual = None
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.geometry('800x600')
        self.ventana.title('Editor de texto')

        # Crear recuadro para texto
        self.texto = tk.Text(self.ventana)
        self.texto.pack(expand=True,fill='both')

        self.crear_menu()

        # Siempre poner el mainloop al final
        self.ventana.mainloop()

    def crear_menu(self):
        '''Esta funcion crea el menu superior'''
        # Creacion de la barra superiro // Menú principal
        self.menu_principal = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu_principal)

        #Llama a todos los botones creados
        
        self.crear_menu_archivo()


    def crear_menu_archivo(self):
        '''Submenu del menu principal'''
        # Genera el menu
        self.menu_archivo = tk.Menu(self.menu_principal,tearoff=0)
        self.menu_guardar = tk.Menu(self.menu_archivo,tearoff=0)
        # Cuelga el menu
        self.menu_principal.add_cascade(label='Archivo',menu=self.menu_archivo)
        
        # Le da una funcion
        self.menu_archivo.add_command(label='Nuevo',command= self.nuevo_archivo)
        self.menu_archivo.add_command(label='Abrir',command= self.abrir_archivo)
        self.menu_archivo.add_cascade(label='Guardar', menu=self.menu_guardar)
        self.menu_guardar.add_command(label='Guardar como',command=self.guardar_archivo_como)##
        self.menu_guardar.add_command(label='Guardar',command=self.guardar_archivo)##
        self.menu_archivo.add_command(label='Salir', command=self.ventana.destroy)
        
    def nuevo_archivo(self):
        self.texto.delete("1.0", tk.END)

    def abrir_archivo(self):
        # Crear el objeto para abrir
        archivo = filedialog.askopenfile(mode='r')
        # Si el usuario cancela evita errores
        if archivo is None:
            return
        
        self.ruta_actual = archivo.name
        contenido = archivo.read()
        archivo.close()

        # Primero limpiar la ventana de texto
        self.texto.delete("1.0", tk.END)

        #Insertar el contenido en la caja de texto
        self.texto.insert("1.0",contenido)
    
    def guardar_archivo_como(self):
        '''Guarda el archivo como'''
        ruta = filedialog.asksaveasfilename(
            filetypes=
                [("Archivo de texto","*.txt"),
                ("Todos los archivos","*.*")],
            defaultextension= ".txt"
        )

        self.ruta_actual = ruta

        if not ruta:
            return
        
        contenido = self.texto.get("1.0", tk.END)

        with open(ruta,"w") as archivo:
            archivo.write(contenido)
        

    def guardar_archivo(self):
        '''Guarda el archivo'''

        if self.ruta_actual is None:
            self.guardar_archivo_como()
            return

        contenido = self.texto.get("1.0",tk.END)

        with open(self.ruta_actual,'w') as archivo:
            archivo.write(contenido)


EditorTexto()