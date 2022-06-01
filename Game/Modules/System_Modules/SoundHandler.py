import pygame, os
pygame.mixer.pre_init(44100, -16, 20, 512)

pygame.init()
pygame.mixer.init()

class SoundHandler(object):
    
    def __init__(self, file_location, channel_number, loop):
        path = os.getcwd()
        self.sound = pygame.mixer.Sound(f"{path}\\{file_location}")
        self.channel = pygame.mixer.Channel(channel_number)
        self.play_bool = True
        self.loop = loop


    
    def play(self, volume=1):
        self.channel.set_volume(volume)
        if self.play_bool == True:
            self.channel.play(self.sound)
            self.play_bool = False

        if self.loop == True:
            if self.channel.get_busy() == False:
                self.play_bool = True

    def stop(self):
        self.channel.stop()

    def pause(self):
        self.channel.pause()