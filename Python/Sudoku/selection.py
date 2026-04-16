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
        self.selected_number = None

        self.btn_resolution_coordinates = (950,800)
        self.font_resolution = pg.font.SysFont('Arial',40)


    def draw(self,surface) -> None:
        """Dibuja los botones de seleccion"""

        for index, pos in enumerate(self.btn_coordinates):

            if self.button_hover(pos,self.btn_w,self.btn_h):

                pg.draw.rect(surface,self.selected_color,(pos[0],pos[1],self.btn_w,self.btn_h)
                            , width=1, border_radius=10)
                
                text_surface = self.font.render(str(self.number_list[index]),False,self.selected_color)   
            
            else:

                pg.draw.rect(surface,self.normal_color,(pos[0],pos[1],self.btn_w,self.btn_h)
                            , width=1, border_radius=10)
                
                text_surface = self.font.render(str(self.number_list[index]),False,self.normal_color)
            
            if self.selected_number is not None:
                if self.selected_number -1 == index:
                    pg.draw.rect(surface,self.selected_color,(pos[0],pos[1],self.btn_w,self.btn_h)
                                , width=1, border_radius=10)
                    
                    text_surface = self.font.render(str(self.number_list[index]),False,self.selected_color)    

            surface.blit(text_surface,(pos[0]+self.off_setx,pos[1]+self.off_sety))
        
        self.resolution_button(surface)

    
    def get_clicked_number(self, mouse_x: int, mouse_y: int):
        """Obtener numero del boton"""

        for index, pos in enumerate(self.btn_coordinates):

            if self.on_button(mouse_x,mouse_y,pos,self.btn_w,self.btn_h):
                self.selected_number = index + 1
        

    def on_button(self, mouse_x: int, mouse_y: int, pos: tuple,width: int, height)-> bool:
        """Returns True if the given coordinates are inside the button"""

        return pos[0] < mouse_x < pos[0]+width and pos[1] < mouse_y < pos[1]+height
    

    def button_hover(self, pos: tuple,width,height)-> bool:
        """Returns True if the mouse is currently hovering over the button"""

        mouse_pos = pg.mouse.get_pos()

        return self.on_button(mouse_pos[0],mouse_pos[1],pos,width,height)
    

    def resolution_button(self,surface) -> None:

        if self.button_hover(self.btn_resolution_coordinates,200,80):
            pg.draw.rect(surface,self.selected_color,
                (self.btn_resolution_coordinates[0],self.btn_resolution_coordinates[1],200,80),10,10)
        
            text_surface = self.font_resolution.render('Resolver',False,self.selected_color)
        #surface.blit(text_surface,(self.btn_resolution_coordinates[0]+22,self.btn_resolution_coordinates[1]+20))           
        
        else:
            pg.draw.rect(surface,self.normal_color,
                (self.btn_resolution_coordinates[0],self.btn_resolution_coordinates[1],200,80),10,10)
        
            text_surface = self.font_resolution.render('Resolver',False,self.normal_color)

        surface.blit(text_surface,(self.btn_resolution_coordinates[0]+22,self.btn_resolution_coordinates[1]+20))
