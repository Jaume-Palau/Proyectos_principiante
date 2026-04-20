import pygame as pg

class LevelSelection:

    def __init__(self):

        self.font = pg.font.SysFont('Arial',25)
        self.color = pg.Color('white')
        self.color_selection = pg.Color('green')
        self.btn_size = (180,50)
        self.btn_coords = [(1000,50),(1000,110),(1000,170)]
        self.level_string = ['Easy','Normal','Hard']
        self.levels = [10,15,20]
        self.selected_btn = None


    def get_offset(self, text_surface, btn_size:tuple) -> tuple:
        
        text_x = text_surface.get_width()
        text_y = text_surface.get_height()

        offset_x = (btn_size[0]-text_x) // 2
        ofset_y = (btn_size[1]-text_y) // 2

        return(offset_x,ofset_y)
    

    def on_button(self,mouse_pos:tuple,cell_coord:tuple) -> bool:

        return (cell_coord[0] < mouse_pos[0] < cell_coord[0]+self.btn_size[0]) and (cell_coord[1] < mouse_pos[1] < cell_coord[1]+self.btn_size[1])
    

    def button_hover(self,cell_coord:tuple) -> bool:

        mouse_pos = pg.mouse.get_pos()

        return self.on_button(mouse_pos,cell_coord)


    def draw_buttons(self,surface) -> None:

        for index, coord in enumerate(self.btn_coords):
            if self.button_hover(coord):
                pg.draw.rect(surface,self.color_selection,(coord[0],coord[1],self.btn_size[0],self.btn_size[1]),1,10)
                text_surface = self.font.render(self.level_string[index],False,self.color_selection)
                
            else:
                pg.draw.rect(surface,self.color,(coord[0],coord[1],self.btn_size[0],self.btn_size[1]),1,10)
                text_surface = self.font.render(self.level_string[index],False,self.color)

            # Mantiene de color el boton seleccionado
            if self.selected_btn == index:
                pg.draw.rect(surface,self.color_selection,(coord[0],coord[1],self.btn_size[0],self.btn_size[1]),1,10)
                text_surface = self.font.render(self.level_string[index],False,self.color_selection)

            offset = self.get_offset(text_surface,self.btn_size)

            surface.blit(text_surface,(coord[0]+offset[0], coord[1]+offset[1]))


    def get_level_button(self,mouse_pos:tuple) -> int:

        for index, coords in enumerate(self.btn_coords):

            if self.on_button(mouse_pos,coords):

                self.selected_btn = index

                return self.levels[index]


