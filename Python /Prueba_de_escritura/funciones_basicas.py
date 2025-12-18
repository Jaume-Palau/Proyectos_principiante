'''En este archivo se encuentras las funciones basicas de funcionaliad'''

import random
from timeit import default_timer as timer
from time import sleep

# Crear stock de oraciones:
oraciones = [
    "El perro corre por el parque",
    "Hoy hace un día fantástico",
    "Me encanta aprender programación",
    "La inteligencia artificial es el futuro"
]

# Funcion que elige frases random:
def frase_random():
    return random.choice(oraciones)

# Funciones que miden el tiempo:
tiempo_inicio = 0
def iniciar_temporizador():
    global tiempo_inicio
    tiempo_inicio = timer()

def calcular_tiempo():
    return timer() - tiempo_inicio


    
