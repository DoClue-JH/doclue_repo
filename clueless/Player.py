# Player Module
import pygame
from pathlib import Path

class Player:    
    WIDTH = 100
    HEIGHT = 100
    
    def __init__(self, name):
        self.player_surface = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.player_surface.fill('bisque3')
        data_folder = Path("clueless/data/graphics/")
        
        self.player_name = name
        # Initialize player to active
        self.player_status = 0 # 0 = active, 1 = lost, and 2 = inactive
        self.first_turn = True # Set to false after first turn
        
        name_image_dict = {'Professor Plum':'prof_plum',
                           'Mrs Peacock':'mrs_peacock',
                           'Mr Green':'mr_green',
                           'Mrs Wine':'mrs_wine',
                           'Miss Scarlet':'miss_scarlet',
                           'Colonel Mustard':'col_mustard'}
        self.player_image = pygame.image.load(f'{data_folder / name_image_dict[name]}.PNG')
        self.player_image = pygame.transform.scale(self.player_image, (80, 80))

        # Use a dictionary to map name to location, how are we defining locations?
        # self.player_location = 
       
    # Return player status (0 = active, 1 = lost, and 2 = inactive)
    def get_status(self):
        return self.player_status
    
    # Update player status (0 = active, 1 = lost, and 2 = inactive)
    def set_status(self, status):
        self.player_status = status
    