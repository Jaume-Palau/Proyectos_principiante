'''Esta alarma selecciona y reproduce, al azar, una url del archivo urls.txt,
que contiene urls de youtube'''
import sys
import os
import random
import webbrowser
from time import sleep
from datetime import datetime, date

# Input de la hora por el usuario:
alarma_usuario = input('Introduzca la hora de la alarma(HH:MM): ')

## Convertir la hora de str a objeto:
try:
    hora_objeto = datetime.strptime(alarma_usuario, "%H:%M").time() #Extraigo la hora
except ValueError:
    print('Error de formato introducido')
    sys.exit(1)

alarma_usuario = datetime.combine(date.today(),hora_objeto) #Formato datetime: 2025-12-26 07:30:00

# Calcular el tiempo de espera en segundos:
hora_actual = datetime.now()
delta = alarma_usuario - hora_actual
tiempo_espera = delta.total_seconds() 
try:
    sleep(tiempo_espera)
    #Sonar alarma
except KeyboardInterrupt:
    print('\nAlarma cancelada')
    sys.exit(0)


#Obtener ruta absoluta del archivo urls.txt: de esta forma se ejecuta desde cualquier directorio
##Directorio donde se encuentra
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
##Construir la ruta absoluta al archivo urls.txt
RUTA_URLS = os.path.join(BASE_DIR,"urls.txt")

# Listar las url
with open(RUTA_URLS,'r') as archivo:
    urls = [linea.strip() for linea in archivo]

# Seleccionar una url al azar:
url_random = random.choice(urls)

# Reproducir la url en el navegador:
webbrowser.open_new(url_random) #En una nueva ventana