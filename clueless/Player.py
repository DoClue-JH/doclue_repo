# Player Module
import pygame

class Player:    

    def __init__(self, name):
        self.player_name = name
        self.player_status = 0 # 0 = active, 1 = lost, and 2 = inactive
        # self.cards = 
        
        # self.player_location = # use a dict to map name to location
        

    # Update player status (0 = active, 1 = lost, and 2 = inactive)
    def set_status(self, status):
        self.player_status = status