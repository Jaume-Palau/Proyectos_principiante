import pygame as pg
from random import sample
from selection import NumberSelection

def create_line_coordinates(cell_size: int) -> list[list[tuple[int,int]]]:
    """Crea las coordenadas de las linias. Punto inicio y punto final para luego dibujarlas"""

    points = []

    # Lineas horizontrales
    for y in range(0,10):
        temp = []
        temp.append((0, y * cell_size))
        temp.append((900, y * cell_size))
        points.append(temp)

    points.append([(0, 899), (900, 899)]) # Dibuja la linea inferior del greed. sino se queda fuera y no se ve
    
    # Lineas verticales
    for x in range(0,10):
        temp = []
        temp.append((x * cell_size, 0))
        temp.append((x * cell_size,900))
        points.append(temp)

    return points


SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE

def pattern(row_num: int, col_num: int) -> int:
    return (SUB_GRID_SIZE * (row_num % SUB_GRID_SIZE) + row_num // SUB_GRID_SIZE + col_num) % GRID_SIZE


def shuffle(samp: range) -> list:
    return sample(samp, len(samp))


def create_grid(sub_grid: int) -> list[list]:
    """ Creates the 9x9 grid filled with random numbers. """
    row_base = range(sub_grid)
    rows = [g * sub_grid + r for g in shuffle(row_base) for r in shuffle(row_base)]
    cols = [g * sub_grid + c for g in shuffle(row_base) for c in shuffle(row_base)]
    nums = shuffle(range(1, sub_grid * sub_grid + 1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


def remove_numbers(grid: list[list]) -> None:
    '''Pone numeros a 0 al azar. La cantidad es empties'''

    n_cells = GRID_SIZE * GRID_SIZE
    empties = 30 
    for i in sample(range(n_cells),empties):
        grid[i//GRID_SIZE][i%GRID_SIZE] = 0


class Grid:
    def __init__(self,font):

        self.cell_size = 100
        self.x_offset = 30 # Ajustar la posicion de los numeros
        self.y_offset = 17 # Ajustar la posicion de los numeros
        self.line_coordinates = create_line_coordinates(self.cell_size)
        self.grid = create_grid(SUB_GRID_SIZE)
        self.game_font = font 
        remove_numbers(self.grid) # Elimina los numeros de forma aleatoria
        self.occupied_cell_coordinates = self.pre_occupied_cell() # Guardar coordenadas de las celdas ocupadas
        self.number_selection = NumberSelection(self.game_font)

        #self.user_inserted_cell = set()

    def is_cell_preocupied(self, x: int, y: int) -> bool:
        """Comprueba si la celda esta en la lista de las ocupadas"""

        for cell in self.occupied_cell_coordinates:
            if cell[0] == y and cell[1] == x :
                return True
        
        return False
        
    def get_mouse_click(self, x: int, y: int)->None:
        """Obtiene las coordenadas del click y si la celda esta vacia pone el num seleccionado"""
    
        if x < 900:
            grid_x, grid_y = x // 100, y // 100

            if not self.is_cell_preocupied(grid_x,grid_y):
                if self.number_selection.selected_number is not None:
                 self.set_cell(grid_x,grid_y,self.number_selection.selected_number)
        
        self.number_selection.get_clicked_number(x,y)


    def _draw_lines(self,pg,surface) -> None:
        """Dibuja las linias en el tablero"""

        for index, points in enumerate(self.line_coordinates):
            if index in(0,3,6,9,11,14,17,20):
                pg.draw.line(surface,pg.Color('white'),points[0],points[1],width=10)
            else:
                pg.draw.line(surface,pg.Color('white'),points[0],points[1])


    def _draw_numbers(self,surface) -> None:
        """Dibuja los numeros en el tablero"""

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):

                if self.get_cell(x,y) != 0:
                    if (y,x) in self.occupied_cell_coordinates:
                        text_surface = self.game_font.render(str(self.get_cell(x,y)),False,pg.Color('white'))
                    else:
                        text_surface = self.game_font.render(str(self.get_cell(x,y)),False,pg.Color('green'))
                    surface.blit(text_surface,(self.x_offset + x * self.cell_size, self.y_offset + y * self.cell_size))
                    
                # if (y,x) in self.user_inserted_cell:
                #     text_surface = self.game_font.render(str(self.get_cell(x,y)),False,pg.Color('green'))
                #     surface.blit(text_surface,(self.x_offset + x * self.cell_size, self.y_offset + y * self.cell_size))


    def draw_all(self,pyg,surface):
        self._draw_lines(pyg,surface)
        self._draw_numbers(surface)
        self.number_selection.draw(surface)


    def get_cell(self,x:int,y:int)-> int:
        return self.grid[y][x]


    def pre_occupied_cell(self:list[list]) -> list[tuple]:
        """Guarda las coordenadas de las celdas ocupadas"""

        occupied_cell_coordinates = []

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x,y) != 0:
                    occupied_cell_coordinates.append((y,x))
        
        return occupied_cell_coordinates


    def set_cell(self, x: int, y: int, value: int)-> None:
        """Dar un valor a la celda de las coordenadas(y,x)"""
        #self.user_inserted_cell.add((y,x)) # Guarda las coordenadas de la celda que clica el usuario
        self.grid[y][x] = value
        self.number_selection.selected_number = None

    def show(self):
        """Muestra los numeros"""

        for row in self.grid:
            print(row)

    


if __name__ == "__main__":
    
    grid = Grid()
    grid.show()
