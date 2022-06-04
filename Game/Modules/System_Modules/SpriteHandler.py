import pygame
from math import gcd
from Modules.System_Modules.CameraClass import Camera

pygame.init()

# This class will be used to handle all in game sprites and animations
class SpriteHandler(object):

    def __init__(self, x, y, fileDestination, frames, fileType, camera=None):
    
        # File Variables
        self.fileDestination = fileDestination # where the sprite is in your computer
        self.frames = frames # How many frames does that animation have
        self.fileType = fileType # png/jpg etc...
        self.image_names = [f"{fileDestination}{i}.{fileType}" for i in range(frames)] # Stores the file locations of each frame
        self.images = [pygame.image.load(i) for i in self.image_names] # Stores the loaded frames

        # Update Variables
        self.count = 0 # counter for type speed
        self.index = 0 # Sprite index
        self.isBlit = True # isBlit

        self.camera = camera
        self.coords = [x, y]
        camera.obj.append(self.coords)

    
    # Method to update the sprite
    def update(self, rate, show): # rate is how fast does the animation move to the next frame
        self.count += 1 # counter starts 
        
        # keeps the index looping
        if self.index > len(self.images)-1:
            self.index = 0
            if show == False: # unless the show is equal to False in which the program only blits once
                self.isBlit = False
        self.image = self.images[self.index] # sets the correct image to a variable called image
        if self.count > rate: # Resets the counter based on the rate
            self.index += 1
            self.count = 0

    # Draws the animation to the screen
    def animate(self, surface, scale, rate=10, show=True):
        self.update(rate, show) # runs the update function

        # Rescales the image
        bigger = pygame.transform.scale(self.image, (scale*(self.image.get_width()//gcd(self.image.get_width(), 
                                        self.image.get_height())), scale*(self.image.get_height()//gcd(self.image.get_width(), 
                                        self.image.get_height()))))
        
        # Draws the animation
        if self.isBlit == True:
            surface.blit(bigger, (self.coords[0], self.coords[1]))

    # draws static images
    def draw(self):
        pass

