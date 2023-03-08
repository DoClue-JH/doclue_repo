# Player Module
import pygame

class Player:    

    def __init__(self, name):
        self.player_name = name
        self.player_status = 0 # 0 = active, 1 = lost, and 2 = inactive
        self.first_turn = True # Set to false after first turn
        # self.cards = 
        
        # Use a dictionary to map name to location, how are we defining locations?
        # self.player_location = 
       
    # Return player status (0 = active, 1 = lost, and 2 = inactive)
    def get_status(self):
        return self.player_status
    
    # Update player status (0 = active, 1 = lost, and 2 = inactive)
    def set_status(self, status):
        self.player_status = status