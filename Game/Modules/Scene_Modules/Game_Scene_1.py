import pygame, os
from Modules.Character_Modules.Player import Player
from Modules.System_Modules.SpriteHandler import SpriteHandler, ImageHandler
from Modules.System_Modules.SoundHandler import SoundHandler

class Map(object):

    def __init__(self, camera, map_assets, file_type, main_character):
        self.camera = camera
        self.map_assets = map_assets
        self.main_character = main_character
        self.game_surface = pygame.Surface((1500, 700))
        path = os.getcwd()
        self.map = ImageHandler(-350, -1900, 300, self.map_assets[0], file_type, self.camera)
        self.background_music = SoundHandler("Assets\\Audio\\First_Level.wav", 1, -1)

    def draw(self, surface, dt):
        self.game_surface.fill((0, 0, 255))
        self.background_music.play()

        self.map.blit(self.game_surface)
        surface.blit(self.game_surface, (0, 0))
        self.main_character.walk(surface, dt)

        if self.camera.obj[-1][0] < -600:
            self.main_character.speedX = 0
            print(True)