import os
import pygame as pg 
from grid import Grid
from level import LevelSelection

pg.init()
pg.font.init()

# Screen resolution
screen_info = pg.display.Info()

# Window game resolution
window_w = 1200
window_h = 905

# Window position in screen
x = (screen_info.current_w - window_w) // 2
y = (screen_info.current_h - window_h) // 2

# Window at center of the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
window_game = pg.display.set_mode((window_w,window_h))

# Objects creation
size_grid = (900,900)
grid = Grid(size_grid,n_cells=1)
btn_levels = LevelSelection()

running = True
level = None
hay_grid = False

while running:

    window_game.fill('Black')
    btn_levels.draw_buttons(window_game)

    if hay_grid:
        grid.draw_all(window_game) 
 

    # Event loop
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            # Captura la posicion del mouse al hacer click izquierdo
            if pg.mouse.get_pressed()[0]:
                if not hay_grid:
                    mouse_pos = pg.mouse.get_pos()
                    level = btn_levels.get_level_button(mouse_pos) # Nivel de juego seleccionado 

                    # Dibuja el tablero cuando el usuario ha seleccionado un nivel
                    if level is not None:
                        grid.create_grid_level(level)
                        hay_grid = True


        




    pg.display.flip()

pg.quit()