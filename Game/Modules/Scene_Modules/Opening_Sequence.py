import imp
from Modules.System_Modules.SoundHandler import SoundHandler
from Modules.System_Modules.TypeWriter import TypeWriter
from Modules.System_Modules.SpriteHandler import SpriteHandler

import pygame

class Scene_1(object):

    def __init__(self):
        self.screenX = 1500
        self.screenY = 700

        self.title_music = SoundHandler("Assets\\Audio\\title.wav", 0)
        self.introduction_sound = SoundHandler("Assets\\Audio\\Introduction_Audio\\Introduction_1.wav", 1)

        self.ominous_text = TypeWriter("You are not supposed to be here... \nThis place is not meant for you... \n             Please... \n        Turn back now...", 32, "Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 400, (self.screenY//2)-50)
        self.ominous_text_bool = True
        self.Opening_Glitch_Surface = pygame.Surface((self.screenX, self.screenY))
        self.glitch = SpriteHandler(f"Assets\\Animations\\Glitch_Sprite\\", 10, "png")
        self.opening_glitch_bool = True
        self.opening_glitch_sound = SoundHandler("Assets\\Audio\\Opening_Cinematic_Glitch.wav", 1)

        self.opening_cinematic_bool = False
        self.opening_cinematic = pygame.Surface((self.screenX, self.screenY))
        self.castle_background = SpriteHandler("Assets\\Animations\\Castle_Background\\", 22, "png")
        self.castleX, self.castleY = 0, -300
        self.castleSpeedX, self.castleSpeedY = 0.7, 0.4

        self.hero_sillouhette = SpriteHandler("Assets\\Animations\\Caped_Hero_Sillouhette\\", 4, "png")

    def draw(self, surface):

        self.Opening_Glitch_Surface.fill((0, 0, 0))
        self.opening_cinematic.fill((255, 0, 0))

        if self.ominous_text_bool:
            self.ominous_text.type(self.Opening_Glitch_Surface, 30)

        if self.ominous_text.finish == True:
            self.ominous_text_bool = False
            self.glitch.animate(self.Opening_Glitch_Surface, 0, 0, 100, 10, False)
            self.opening_glitch_sound.play()
            if self.glitch.isBlit == False:
                self.opening_glitch_bool = False
                self.opening_cinematic_bool = True

        if self.opening_glitch_bool == True:
            surface.blit(self.Opening_Glitch_Surface, (0, 0))
        elif self.opening_cinematic_bool == True:
            self.castle_background.animate(self.opening_cinematic, self.castleX, self.castleY, 1000, 35)
            # self.hero_sillouhette.animate(self.opening_cinematic, 0, 0, 500, 20)
            surface.blit(self.opening_cinematic, (0, 0))
            self.castleX -= 0.07
            self.castleY += 0.04
            self.title_music.play(0.3)
            self.introduction_sound.play()
            if self.introduction_sound.channel.get_busy() == False:
                pass