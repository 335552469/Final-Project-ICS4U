import pygame
from math import gcd
from Modules.System_Modules.CameraClass import Camera

pygame.init()

class Image(object):
    def __init__(self, x, y, scale, fileDestination, fileType, camera):
        self.x = x
        self.y = y
        self.fileDestination = fileDestination
        self.scale = scale
        self.fileType = fileType
        self.camera = camera

class ImageHandler(Image):
    
    def __init__(self, x, y, scale, fileDestination, fileType, camera):
        super().__init__(x, y, scale, fileDestination, fileType, camera)
        self.coords = [self.x, self.y]
        self.camera.obj.append(self.coords)

        self.image = pygame.image.load(f"{fileDestination}.{fileType}")
        self.bigger = pygame.transform.scale(self.image, (self.scale*(self.image.get_width()//gcd(self.image.get_width(), 
                                        self.image.get_height())), self.scale*(self.image.get_height()//gcd(self.image.get_width(), 
                                        self.image.get_height()))))

    def blit(self, surface):
        surface.blit(self.bigger, (self.coords[0], self.coords[1]))
        

# This class will be used to handle all in game sprites and animations
class SpriteHandler(Image):

    def __init__(self, x, y, scale, fileDestination, frames, fileType, camera=None):
        super().__init__(x, y, scale, fileDestination, fileType, camera)
        # File Variables
        self.frames = frames # How many frames does that animation have
        self.image_names = [f"{self.fileDestination}{i}.{self.fileType}" for i in range(self.frames)] # Stores the file locations of each frame
        self.images = [pygame.image.load(i) for i in self.image_names] # Stores the loaded frames

        # Update Variables
        self.count = 0 # counter for type speed
        self.index = 0 # Sprite index
        self.isBlit = True # isBlit

        self.coords = [self.x, self.y]
        self.camera.obj.append(self.coords)

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

    # Draws the animation to the screenc
    def animate(self, surface, rate=10, show=True):
        self.update(rate, show) # runs the update function

        # Rescales the image
        bigger = pygame.transform.scale(self.image, (self.scale*(self.image.get_width()//gcd(self.image.get_width(), 
                                        self.image.get_height())), self.scale*(self.image.get_height()//gcd(self.image.get_width(), 
                                        self.image.get_height()))))
        # Draws the animation
        if self.isBlit == True:
            surface.blit(bigger, (self.coords[0], self.coords[1]))


