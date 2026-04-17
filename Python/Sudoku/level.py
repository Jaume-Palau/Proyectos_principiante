import pygame as pg

class LevelSelection:

    def __init__(self):

        self.size = (150,40)
        self.font = pg.font.SysFont('Arial',27)
        self.color = pg.Color('white')
        self.selection_color = [pg.Color('green'),pg.Color('yellow'),pg.Color('Red')]
        self.btn_coordinates = [(975,650),(975,700),(975,750)]
        self.btn_levels = [30,35,40]
        self.btn_string = ['Facil','Normal','Dificil']


    def on_button(self,mouse_pos:tuple, btn_coord:tuple, size:tuple) -> bool:
        """Returns True if given coordinates ara inside the button"""

        return btn_coord[0] < mouse_pos[0] < btn_coord[0] + size[0] and btn_coord[1] < mouse_pos[1] < btn_coord[1] + size[1]
    

    def button_hover(self,btn_coord:tuple, size:tuple) -> bool:
        """Returns True if mouse currently hovering over button"""

        mouse_pos = pg.mouse.get_pos()
        return self.on_button(mouse_pos,btn_coord,size)
        

    def get_level_button(self,mouse_pos:tuple) -> int:
        """Returns de level of the button pressed"""

        for index, coord in enumerate(self.btn_coordinates):

            if self.on_button(mouse_pos,coord,self.size):
                return self.btn_levels[index]


    def get_offset(self, text_surface, btn_size:tuple) -> tuple:
        
        text_x = text_surface.get_width()
        text_y = text_surface.get_height()

        offset_x = (btn_size[0]-text_x) // 2
        ofset_y = (btn_size[1]-text_y) // 2

        return(offset_x,ofset_y)
            
    
    def draw_buttons(self,surface) -> None:

        for index, coord in enumerate(self.btn_coordinates):

            if self.button_hover(coord,self.size) and index == 0:

                pg.draw.rect(surface,self.selection_color[index],(coord[0],coord[1],self.size[0],self.size[1]),1,10)
                text_surface = self.font.render(str(self.btn_string[index]),False,self.selection_color[index])

            elif self.button_hover(coord,self.size) and index == 1:

                pg.draw.rect(surface,self.selection_color[index],(coord[0],coord[1],self.size[0],self.size[1]),1,10)
                text_surface = self.font.render(str(self.btn_string[index]),False,self.selection_color[index])
            
            elif self.button_hover(coord,self.size) and index == 2:
                
                pg.draw.rect(surface,self.selection_color[index],(coord[0],coord[1],self.size[0],self.size[1]),1,10)
                text_surface = self.font.render(str(self.btn_string[index]),False,self.selection_color[index])

            else:

                pg.draw.rect(surface,self.color,(coord[0],coord[1],self.size[0],self.size[1]),1,10)
                text_surface = self.font.render(str(self.btn_string[index]),False,self.color)

            offset = self.get_offset(text_surface,self.size)

            surface.blit(text_surface,(coord[0]+offset[0], coord[1]+offset[1]))




        