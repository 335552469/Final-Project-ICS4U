import pygame
from Modules.System_Modules.SpriteHandler import SpriteHandler

class Player(object):

    def __init__(self, name, x, y, scale):
        self.name = name
        self.x = x
        self.y = y

        self.hit_boxW = 50
        self.hit_boxH = 75
        self.scale = scale

        self.speedX = 3
        self.speedY = 3

        self.index = 0

        directions = ["Up", "Down", "Right", "Left"]
        self.sprite_directions = [SpriteHandler(f"Assets\\Characters\\Character_1\\{i}\\", 3) for i in directions]

    def walk(self, surface, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speedY*dt
            self.index = 0
        elif keys[pygame.K_s]:
            self.y += self.speedY*dt
            self.index = 1
        elif keys[pygame.K_a]:
            self.x -= self.speedX*dt
            self.index = 3
        elif keys[pygame.K_d]:
            self.x += self.speedX*dt
            self.index = 2
        else:
            self.sprite_directions[self.index].count_speed = 0
            self.sprite_directions[self.index].index = 1

        self.sprite_directions[self.index].animate(surface, self.x, self.y, self.scale, 70)
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.hit_boxW, self.hit_boxH), 2)

    def collision_mask(self, other):
        pass


        
