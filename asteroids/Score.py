import pygame

class Score:
    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.value = 0
    
    def add(self):
        self.value += 1