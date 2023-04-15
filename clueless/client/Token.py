# Player Module
import pygame

class Token(pygame.sprite.Sprite):    
    
    def __init__(self, name, pos_x, pos_y, width, height, color):
        super().__init__()

        self.player_name = name
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.vel = 3
    
    # def draw(self, window):
    #     pygame.draw.rect(window, self.color, self.rect)

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)