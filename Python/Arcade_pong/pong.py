# Proyecto: Pong en Python con Turtle
# Juego arcade básico inspirado en Pong.
# Incluye control del jugador, paleta automática para la CPU,
# movimiento de pelota, detección de colisiones y marcador.


import turtle

# VENTANA 

window = turtle.Screen()
window.bgcolor('black')
window.title('PING PONG')
window.setup(width=1400,height=1000)
window.listen()
window.tracer(0)


# MARCADOR

player = 0
CPU = 0

marcador = turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.color("white")
marcador.goto(0, 400)
marcador.write(f"{player} - {CPU}", align="center", font=("Arial", 40, "normal"))


# PALETAS

paleta_left = turtle.Turtle()
paleta_left.penup()
paleta_left.shape('square')
paleta_left.color('white')
paleta_left.shapesize(stretch_wid=10,stretch_len=1)
paleta_left.goto(-600,0)

paleta_right = turtle.Turtle()
paleta_right.penup()
paleta_right.shape('square')
paleta_right.color('white')
paleta_right.shapesize(stretch_wid=10,stretch_len=1)
paleta_right.goto(600,0)


# PELOTA

pelota = turtle.Turtle()
pelota.penup()
pelota.shape('circle')
pelota.color('white')
pelota.dx = 0.3
pelota.dy = 0.3

# FUNCIONES DE MOVIMIENTO

def subir_paleta(paleta):
    y = paleta.ycor()
    if y < 400:
        y += 20
        paleta.sety(y)


def bajar_paleta(paleta):
    y = paleta.ycor()
    if y > -400:
        y -= 20
        paleta.sety(y)


def mover_pelota():
    x = pelota.xcor()
    y = pelota.ycor()

    pelota.setx(x + pelota.dx)
    pelota.sety(y + pelota.dy)

    if pelota.ycor() >= 490:
        pelota.sety(490)
        pelota.dy *= -1

    elif pelota.ycor() <= -490:
        pelota.sety(-490)
        pelota.dy *= -1



def mover_maquina():

    if pelota.ycor() > paleta_right.ycor():
        if paleta_right.ycor() < 400:
            paleta_right.sety(paleta_right.ycor() +0.25) 
    
    if pelota.ycor() < paleta_right.ycor():
        if paleta_right.ycor() > -400:
            paleta_right.sety(paleta_right.ycor()-0.25)


def colisiones_paleta_izquierda():

    if (pelota.xcor() <= -590 and pelota.xcor() > -600 ) and abs(pelota.ycor() - paleta_left.ycor()) <= 99:
        pelota.setx(-590)
        pelota.dx *= -1

def colisiones_paleta_derecha():

    if (pelota.xcor() >= 590 and pelota.xcor() < 600) and abs(pelota.ycor() - paleta_right.ycor()) <= 99:
        pelota.setx(590)
        pelota.dx *= -1


def marcador_puntuaciones():

    global player, CPU

    if pelota.xcor() > 700:
        player += 1
        pelota.setx(0)
        pelota.sety(0)
        pelota.dx *= -1

    elif pelota.xcor() < -700:
        CPU +=1
        pelota.setx(0)
        pelota.sety(0)
        pelota.dx *= -1

    marcador.clear()
    marcador.write(f"{player} - {CPU}", align="center", font=("Arial", 40, "normal"))

# MOVIMIENTO PALETAS
window.onkeypress(lambda: subir_paleta(paleta_left),"w")
window.onkeypress(lambda: bajar_paleta(paleta_left),"s")


while True:

    window.update()

    mover_pelota()
    mover_maquina()

    colisiones_paleta_derecha()
    colisiones_paleta_izquierda()

    marcador_puntuaciones()