import pygame, os
pygame.mixer.pre_init(44100, -16, 20, 512) # Basic preinit for sounds

pygame.init()
pygame.mixer.init()

# The SoundHandler class will organize the mixer library so we can have easy to use sounds in our game
class SoundHandler(object):
    
    def __init__(self, file_location, channel_number, loop=0):
        path = os.getcwd() # path variable to make life easier
        self.sound = pygame.mixer.Sound(f"{path}\\{file_location}") # Initializes our sound
        self.channel = pygame.mixer.Channel(channel_number) # sets our sound to a channel
        self.play_bool = True # Is the sound playing
        self.loop = loop # do we want our sound to loop and how many times if it does loop


    # Plays our sound
    def play(self, volume=1):
        self.channel.set_volume(volume) # set volume

        # Makes sure that the sound plays once even in the main loop
        if self.play_bool == True:
            self.channel.play(self.sound, loops=self.loop)
            self.play_bool = False

    # stops the sound
    def stop(self):
        self.channel.stop()
    # Pauses the sound
    def pause(self):
        self.channel.pause()