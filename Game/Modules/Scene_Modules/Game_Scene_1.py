import pygame, os
from Modules.Character_Modules.Player import Player
from Modules.System_Modules.SpriteHandler import SpriteHandler

class Map(object):

    def __init__(self, camera, map_path, file_type):
        self.camera = camera
        self.main_character = Player("Hero", 1500//2, 700//2, 25, camera)
        self.game_surface = pygame.Surface((1500, 700))
        path = os.getcwd()
        self.map = SpriteHandler(0, 0, map_path, 1, file_type, camera)

    def draw_character(self, surface, dt):
        print(self.camera.x, self.camera.y)
        self.game_surface.fill((0, 0, 255))
        self.map.draw(self.game_surface, 300)
        self.main_character.walk(self.game_surface, dt)
        surface.blit(self.game_surface, (0, 0))
        