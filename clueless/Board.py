# Board Module
import pygame

class Board:
    WIDTH = 550
    HEIGHT = 550
    
    def __init__(self):
        self.boardSurface = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.boardSurface.fill('bisque3')

        self.cornerRoomSurface = pygame.image.load('clueless\data\graphics\corner.PNG')
        self.cornerRoomSurface = pygame.transform.scale(self.cornerRoomSurface, (100, 100))

        self.normalRoomSurface = pygame.image.load('clueless\data\graphics\window.PNG')
        self.normalRoomSurface = pygame.transform.scale(self.normalRoomSurface, (100, 100))

        self.hallway = pygame.image.load('clueless\data\graphics\hallway.PNG')
        self.hallway = pygame.transform.scale(self.hallway, (100, 50))

        self.hallwayVertical = pygame.transform.scale(self.hallway, (50, 100))

