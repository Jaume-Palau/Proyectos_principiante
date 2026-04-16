import pygame
import os
from grid import Grid

pygame.init()

# RESOLUCION DE VENTANA JUEGO
window_w = 1200
window_h = 900


# RESOLUCION DE PANTALLA
info = pygame.display.Info()

# POSICION PARA LA VENTANA JUEGO
x = (info.current_w - window_w) // 2
y = (info.current_h - window_h) // 2

# POSICIONAR VENTANA DE JUEGO EN EL CENTRO DE PANTALLA
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# CREACION DE LA VENTANA
surface = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption('Sudoku') #TITULO

# INICIALIZAR MODULO PARA FUENTE(LETRAS/NUMEROS)
pygame.font.init()
game_font = pygame.font.SysFont('Arial',70)

# CREACION DEL GRID(REJILLA)
grid = Grid(game_font)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # El usuario clica X para cerrar ventana
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse_click(pos[0],pos[1])


    grid.draw_all(pygame,surface)

    pygame.display.flip()

pygame.quit()