import pygame
from math import gcd

pygame.init()

class SpriteHandler(object):

    def __init__(self, fileDestination, frames):

        # File Variables
        self.fileDestination = fileDestination
        self.frames = frames
        self.image_names = [f"{fileDestination}{i}.png" for i in range(frames)]
        self.images = [pygame.image.load(i) for i in self.image_names]

        # Update Variables
        self.count = 0
        self.count_speed = 1
        self.index = 0
    
    def update(self, rate):
        self.count += self.count_speed
        if self.index > len(self.images)-1:
            self.index = 0
        self.image = self.images[self.index]
        if self.count > rate:
            self.index += 1
            self.count = 0

    def animate(self, surface, x, y, scale, rate=10):
        self.update(rate)
        self.count_speed = 1
        bigger = pygame.transform.scale(self.image, (scale*(self.image.get_width()//gcd(self.image.get_width(), 
                                        self.image.get_height())), scale*(self.image.get_height()//gcd(self.image.get_width(), 
                                        self.image.get_height()))))
        surface.blit(bigger, (x, y))

