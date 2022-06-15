import pygame
from Modules.System_Modules.SpriteHandler import SpriteHandler

# This class is specifically used to modify the abilities of the player/main character
class Player(object):

    def __init__(self, name, x, y, scale, camera):

        # characteristics
        self.name = name # character name
        self.x = x # x position
        self.y = y # y position
        self.scale = scale # size
        self.camera = camera

        # Hit box values
        self.hit_boxW = 50
        self.hit_boxH = 75

        # Speeds
        self.speedU = 3
        self.speedD = 3
        self.speedL = 3
        self.speedR = 3

        # Index of sprite
        self.index = 0

        # Movement 
        directions = ["Up", "Down", "Right", "Left"]
        
        # different sprite animations for different directions placed into a list
        self.sprite_directions = [SpriteHandler(self.x, self.y, self.scale, f"Assets\\Characters\\Character_1\\{i}\\", 3, "png", camera) for i in directions]
    # Method used to handle whether the player is walking
    def walk(self, surface, dt): # takes in surface and delta time so we can have walking movement be independant of the framerate

        keys = pygame.key.get_pressed()
        # Key Input
        if keys[pygame.K_w]: # W key
            self.speedD = 3
            self.speedL = 3
            self.speedR = 3
            self.camera.moveY(-self.speedU, dt)
            for i in self.sprite_directions:
                i.coords[1] -= self.speedU*dt
            self.index = 0 # Up Sprite
        elif keys[pygame.K_s]: # S key
            self.speedU = 3
            self.speedL = 3
            self.speedR = 3
            self.camera.moveY(self.speedD, dt)
            for i in self.sprite_directions:
                i.coords[1] += self.speedD*dt
            self.index = 1 # Down Sprite
        elif keys[pygame.K_a]: # A key
            self.speedU = 3
            self.speedD = 3
            self.speedR = 3
            self.camera.moveX(-self.speedL, dt)
            for i in self.sprite_directions:
                i.coords[0] -= self.speedL*dt
            self.index = 3 # Left Sprite
        elif keys[pygame.K_d]: # D key
            self.speedU = 3
            self.speedD = 3
            self.speedL = 3
            self.camera.moveX(self.speedR, dt)
            for i in self.sprite_directions:
                i.coords[0] += self.speedR*dt
            self.index = 2 # Right Sprite
        else: # Key up
            self.sprite_directions[self.index].count_speed = 0 # Player Stops
            self.sprite_directions[self.index].index = 1 # The sprite animation stops at the static sprite

        self.sprite_directions[self.index].animate(surface, dt, 20) # Blits the walk -- dependant on index
        self.width = self.sprite_directions[self.index].bigger.get_width()
        self.height = self.sprite_directions[self.index].bigger.get_height()
        pygame.draw.rect(surface, (255, 0, 0), (self.sprite_directions[self.index].coords[0], self.sprite_directions[self.index].coords[1], self.width, self.height), 2) # draws the hitbox

    # Function will be used to create the collisions
    def collision_mask(self, other):
        pass
