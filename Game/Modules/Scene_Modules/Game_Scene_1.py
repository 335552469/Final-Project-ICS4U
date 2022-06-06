import pygame, os
from Modules.Character_Modules.Player import Player
from Modules.System_Modules.SpriteHandler import SpriteHandler

class Map(object):

    def __init__(self, camera, map_path, file_type):
        self.camera = camera
        self.map_path = map_path
        self.main_character = Player("Hero", 1500//2, 700//2, 25, camera)
        self.game_surface = pygame.Surface((1500, 700))
        path = os.getcwd()

    def draw_character(self, surface, dt):
        self.game_surface.fill((0, 0, 255))