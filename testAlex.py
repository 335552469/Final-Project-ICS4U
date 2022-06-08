from calendar import c
import pygame, sys, keyboard, time
from math import gcd
from Game.Modules.Character_Modules.Player import Player
from Game.Modules.System_Modules.CameraClass import Camera
from Game.Modules.System_Modules.TypeWriter import TypeWriter

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

class NPC(object):
    def __init__(self, text, x, y, scale, camera, filename, filetype, interactNum):
        self.text = text
        self.x = x
        self.y = y
        self.scale = scale
        self.camera = camera
        self.filename = filename
        self.filetype = filetype
        self.interactNum = interactNum

        self.npcImage = ImageHandler(300, 250, 25, f"Assets\\Characters\\Character_2\\{filename}", filetype, camera)

        self.hit_boxW = 50
        self.hit_boxH = 75

        self.callBool = False
        self.responceBool = False
        self.check = False
        
        self.respond = list(text.keys())[0]
        self.words = TypeWriter(text[self.respond], 15, f"Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 25, 315)
        self.ans = TypeWriter(list(text.keys())[1] + "\n" + list(text.keys())[2], 15, f"Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 25, 315)

    def draw(self, surface):
        self.npcImage.blit(surface)

    def call(self, surface):
        self.words.createTextbox(surface, (0, 0, 0), (0, 0, 255), (0, 300, 600, 150))
        self.words.type(surface, rate=15)

    def responce(self, surface):
        self.ans.createTextbox(surface, (0, 0, 0), (0, 0, 255), (0, 300, 600, 150))
        self.ans.type(surface, rate=15)
    
    def interaction(self, surface):
        player.speedX = 0
        player.speedY = 0
        player.sprite_directions[player.index].count_speed = 0 # Player Stops
        player.sprite_directions[player.index].index = 1 # The sprite animation stops at the static sprite
        if keyboard.is_pressed("Enter"):
            self.check = True
        if self.callBool is True:
            self.call(surface)
        if self.responceBool is True:
            self.responce(surface)
        
        for i in range(self.interactNum):
            self.call(surface)
            if self.check:
                self.responce(surface)
            

gameCam = Camera(0, 0)
run = True
npcTalk = False
player = Player("Hero", 250, 210, 25, gameCam)
npc = NPC({"None": "Hey… I know you. You’re that new hero who’s come to town.\nBig whoop, I’m stronger anyway I’ve been heroing in Zandril\nfor as long as I can remember.\nSo… you planning on retrieving the princess\nand bringing her back to her former glory?", "Yes": "Hm… I could do that, but… \nif you’re going anyway, I probably shouldn’t interfere, \nfor… yknow… \nsafety reasons…", "No": "HA how predictable, \nI knew you were a wimp anyway…."}, 300, 225, 25, gameCam, "tile016", "png", 2)
surface = pygame.display.set_mode((600, 450))

while run:
    surface.fill((255, 255, 255))
    if keyboard.is_pressed("space"):
        npcTalk = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    
    player.walk(surface, 0.05)
    npc.draw(surface)
    if npcTalk is True:
        npc.interaction(surface)
    pygame.display.update()
