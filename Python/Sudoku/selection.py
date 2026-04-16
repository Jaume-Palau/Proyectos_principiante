import pygame as pg

class NumberSelection:

    def __init__(self,font):

        self.font = font
        self.off_setx = 20
        self.off_sety = 10
        self.btn_w = 80
        self.btn_h = 80
        self.normal_color = pg.Color('white')
        self.selected_color = pg.Color('green')
        self.btn_coordinates = [(950, 50), (1050, 50),
                                (950, 150), (1050, 150),
                                (950, 250), (1050, 250),
                                (950, 350), (1050, 350),
                                (1050, 450)]
        self.number_list = list(range(1,10))


    def draw(self,surface) -> None:
        """Dibuja los botones de seleccion"""

        for index, pos in enumerate(self.btn_coordinates):

            pg.draw.rect(surface,self.normal_color,(pos[0],pos[1],self.btn_w,self.btn_h)
                        , width=1, border_radius=1)
            
            text_surface = self.font.render(str(self.number_list[index]),False,self.normal_color)
            surface.blit(text_surface,(pos[0]+self.off_setx,pos[1]+self.off_sety))

    
    def get_clicked_number(self,mouse_x: int, mouse_y: int):
        """Obtener numero del boton"""

        for index, (x,y) in enumerate(self.btn_coordinates):

            if x <= mouse_x <= x + self.btn_w and  y <= mouse_y <= y + self.btn_h:
                return index + 1
        
        return None


    




