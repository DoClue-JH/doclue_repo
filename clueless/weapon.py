import pygame
from pathlib import Path

class Weapon:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name
