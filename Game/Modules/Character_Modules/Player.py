import pygame
from math import gcd

pygame.init()

class Player(object):

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.index = 0
        self.count_speed = 1
        
        self.images = []

    def load_sprite_images(self, frames, file_location):
        image_list = [f"{file_location}{i}.png" for i in range(frames)]
        print(image_list)
        for i in image_list:
            self.images.append(pygame.image.load(i))

    def update(self, rate):
        self.count += self.count_speed
        if self.index > len(self.images)-1:
            self.index = 0
        self.image = self.images[self.index]
        if self.count > rate:
            self.index += 1
            self.count = 0

    def draw_animation(self, surface, x, y, scale, rate=10):
        self.update(rate)
        self.count_speed = 1
        #print(self.image.get_width(), self.image.get_height())
        bigger = pygame.transform.scale(self.image, (scale*(self.image.get_width()//gcd(self.image.get_width(), self.image.get_height())), scale*(self.image.get_height()//gcd(self.image.get_width(), self.image.get_height()))))
        surface.blit(bigger, (x, y))