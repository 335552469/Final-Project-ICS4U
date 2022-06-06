import pygame
from Modules.Character_Modules.Player import Player

class Map(object):

    def __init__(self, camera):
        self.main_character = Player("Hero", 0, 0, 25, camera)
        self.game_surface = pygame.Surface((1500, 700))


    def draw_character(self, surface, dt):
        self.game_surface.fill((0, 0, 255))
        self.main_character.walk(self.game_surface, dt)
        surface.blit(self.game_surface, (0, 0))
        