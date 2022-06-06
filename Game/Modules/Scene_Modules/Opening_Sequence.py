from Modules.System_Modules.SoundHandler import SoundHandler
from Modules.System_Modules.TypeWriter import TypeWriter
from Modules.System_Modules.SpriteHandler import SpriteHandler

import pygame

class Scene_1(object):


    def __init__(self, camera):
        self.camera = camera
        self.screenX = 1500
        self.screenY = 700

        self.title_music = SoundHandler("Assets\\Audio\\title.wav", 0)
        self.introduction_sound = SoundHandler("Assets\\Audio\\Introduction_Audio\\Introduction_1.wav", 1)

        self.ominous_text = TypeWriter("You are not supposed to be here... \nThis place is not meant for you... \n             Please... \n        Turn back now...", 32, "Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 400, (self.screenY//2)-50)
        self.ominous_text_bool = True
        self.ominious_text_surface = pygame.Surface((self.screenX, self.screenY))
        self.Opening_Glitch_Surface = pygame.Surface((self.screenX, self.screenY))
        self.gx = 0
        self.gy = 0
        self.glitch = SpriteHandler(self.gx, self.gy, "Assets\\Animations\\Glitch_Sprite\\", 10, "png", camera)
        self.opening_glitch_bool = False
        self.opening_glitch_sound = SoundHandler("Assets\\Audio\\Opening_Cinematic_Glitch.wav", 3)

        self.opening_cinematic_bool = False
        self.opening_cinematic = pygame.Surface((self.screenX, self.screenY))
        self.castle_background = SpriteHandler(0, -300, "Assets\\Animations\\Castle_Background\\", 22, "png", camera)
        self.speedX, self.speedY = 0.075, 0.04
        self.desert_backgroud = SpriteHandler(1900, -400, "Assets\\Animations\\Caped_Hero_Background\\", 20, "png", camera)
        self.glitch2 = SpriteHandler(1900, -400, "Assets\\Animations\\Glitch_Sprite\\", 10, "png", camera)

        self.introduction2_sound = SoundHandler("Assets\\Audio\\Introduction_Audio\\Introduction_2.wav", 2)
        self.intro_counter = 0

        self.scene_finished = False
    def draw(self, surface, dt):
        self.Opening_Glitch_Surface.fill((0, 0, 255))
        self.opening_cinematic.fill((255, 0, 0))
        self.ominious_text_surface.fill((0, 0, 0))
        if self.scene_finished == False:
            if self.ominous_text_bool == True:
                self.ominous_text.type(self.ominious_text_surface, 30)
                surface.blit(self.ominious_text_surface, (0, 0))
                if self.ominous_text.finish == True:
                    self.ominous_text_bool = False
                    self.opening_glitch_bool = True
                    
            if self.opening_glitch_bool == True:
                self.glitch.animate(self.Opening_Glitch_Surface, 100, 10, False)
                surface.blit(self.Opening_Glitch_Surface, (0, 0))
                self.opening_glitch_sound.play()
                if self.glitch.isBlit == False:
                    self.opening_glitch_bool = False
                    self.opening_cinematic_bool = True

            elif self.opening_cinematic_bool == True:
                self.title_music.play(0.2)
                self.introduction_sound.play(0.5)
                self.desert_backgroud.animate(self.opening_cinematic, 200, 20)
                self.castle_background.animate(self.opening_cinematic, 1000,  20)
                self.camera.moveX(self.speedX, dt)
                self.camera.moveY(-self.speedY, dt)
                if self.introduction_sound.channel.get_busy() == False:
                    self.intro_counter += 1
                    self.speedY = 0
                    self.speedX = 0.45
                    self.introduction2_sound.play(2)
                    if self.intro_counter == 760:
                        self.title_music.channel.fadeout(8000)

                    if self.introduction2_sound.channel.get_busy() == False:
                        self.speedX = 0
                        self.speedY = 0
                        self.glitch2.animate(self.opening_cinematic, 100, 10, False)
                        self.opening_glitch_sound.play()
                        if self.glitch2.isBlit == False:
                            self.scene_finished = True
                
                surface.blit(self.opening_cinematic, (0, 0))