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
        self.speedX = 3
        self.speedY = 3

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
            self.camera.moveY(-self.speedY, dt)
            for i in self.sprite_directions:
                i.coords[1] -= self.speedX*dt
            self.index = 0 # Up Sprite
        elif keys[pygame.K_s]: # S key
            self.camera.moveY(self.speedY, dt)
            for i in self.sprite_directions:
                i.coords[1] += self.speedX*dt
            self.index = 1 # Down Sprite
        elif keys[pygame.K_a]: # A key
            self.camera.moveX(-self.speedX, dt)
            for i in self.sprite_directions:
                i.coords[0] -= self.speedX*dt
            self.index = 3 # Left Sprite
        elif keys[pygame.K_d]: # D key
            self.camera.moveX(self.speedX, dt)
            for i in self.sprite_directions:
                i.coords[0] += self.speedX*dt
            self.index = 2 # Right Sprite
        else: # Key up
            self.sprite_directions[self.index].count_speed = 0 # Player Stops
            self.sprite_directions[self.index].index = 1 # The sprite animation stops at the static sprite

        self.sprite_directions[self.index].animate(surface, 20) # Blits the walk -- dependant on index
        pygame.draw.rect(surface, (255, 0, 0), (self.sprite_directions[self.index].coords[0], self.sprite_directions[self.index].coords[1], self.sprite_directions[self.index].image.get_width()*self.scale//16, self.sprite_directions[self.index].image.get_height()*self.scale//16), 2) # draws the hitbox

    # Function will be used to create the collisions
    def collision_mask(self, other):
        pass
