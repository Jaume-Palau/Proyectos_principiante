import pygame as pg
import numpy as np

def create_line_coordinates(size:tuple ,n_cells:int) -> list[list[tuple]]:

    cell_size = size[0] // n_cells
    points = []

    # lineas horizontales
    for y in range(0,n_cells+1):
        temp = []
        
        temp.append((0, y*cell_size)) #puntos iniciales
        temp.append((size[0],y*cell_size)) #puntos finales

        points.append(temp)

    # lineas verticales
    for x in range(0,n_cells+1):
        temp = []

        temp.append((x*cell_size,0)) #puntos iniciales
        temp.append((x*cell_size,size[1])) #puntos finales

        points.append(temp)

    return points


class Grid:

    def __init__(self,size:tuple,n_cells:int):
        
        self.size = size
        self.n_cells = n_cells
        self.cell_size = size[0] // n_cells
        self.line_coordinates = create_line_coordinates(size,n_cells)
        self.cell_coordinates = self.get_cell_coordinates()
        self.grid = np.zeros((n_cells,n_cells))
        self.font = pg.font.SysFont('Arial',20)
        self.color = pg.Color('white')

    def draw_all(self,surface):
        self.draw_lines(surface)
        self.draw_on_cell(surface)


    def create_grid_level(self,level):
        self.n_cells = level
        self.cell_size = self.size[0] // level
        self.grid = np.zeros((level,level))
        self.line_coordinates = create_line_coordinates(self.size,level)
        self.cell_coordinates = self.get_cell_coordinates()


    def draw_lines(self,surface) -> None:

        for line in self.line_coordinates:
            pg.draw.line(surface,self.color,line[0],line[1])


    def get_cell_coordinates(self) -> list[tuple]:

        coordinates = []

        for y in range(0,self.n_cells):
            for x in range(0,self.n_cells):

                coordinates.append((x*self.cell_size,y*self.cell_size))

        return coordinates


    def on_cell(self,mouse_pos:tuple,cell_coord:tuple) -> bool:

        return (cell_coord[0] < mouse_pos[0] < cell_coord[0]+self.cell_size) and (cell_coord[1] < mouse_pos[1] < cell_coord[1]+self.cell_size)


    def cell_hover(self,cell_coord:tuple) -> bool:

        mouse_pos = pg.mouse.get_pos()

        return self.on_cell(mouse_pos,cell_coord)


    def draw_on_cell(self,surface) -> None:

        for coord in self.cell_coordinates:

            if self.cell_hover(coord):
                pg.draw.rect(surface,self.color,(coord[0],coord[1],self.cell_size,self.cell_size))




if __name__ == "__main__":


    pg.font.init()
    window_game = pg.display.set_mode((1200,1200))
    surface_grid = (900,900)

    grid = Grid(surface_grid,3)

    print(grid.cell_coordinates)

