import pygame

pygame.init()

class Player(object):

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.index = 0

    def load_sprite_images(self, frames, file_location):
        self.frames = frames
        self.sprite_names = [f"{file_location}{i}.png" for i in range(frames)]
        self.images = [pygame.image.load(i) for i in self.sprite_names]

    def handle_animation(self, rate=10):
        if self.index > self.frames-1:
            self.index = 0
        self.count += 1
        if self.count >= rate:
            self.index += 1
            self.count = 0

    def draw_animation(self, surface, x, y, frames, file_location, rate=10):
        self.load_sprite_images(frames, file_location)
        self.handle_animation()
        surface.blit(self.images[self.index], (x, y))