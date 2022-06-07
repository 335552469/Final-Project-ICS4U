import pygame, sys, keyboard, time
from math import gcd
from Game.Modules.Character_Modules.Player import Player
from Game.Modules.System_Modules.CameraClass import Camera
from Game.Modules.System_Modules.TypeWriter import TypeWriter

class NPC(object):
    def __init__(self, npcNum, x, y, scale, camera, file):
        self.text = open("npc" + str(npcNum) + "Lines.txt")
        self.x = x
        self.y = y
        self.scale = scale
        self.camera = camera
        self.file = file

        self.hit_boxW = 50
        self.hit_boxH = 75

        self.count = 0
        self.delay = 15000000

        self.image = pygame.image.load(self.file)
        self.npc = pygame.transform.scale(self.image, (scale*(self.image.get_width()//gcd(self.image.get_width(), 
                                        self.image.get_height())), scale*(self.image.get_height()//gcd(self.image.get_width(), 
                                        self.image.get_height()))))
        
        self.words = TypeWriter(self.text.readline(), 15, f"Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 25, 325)

    def draw(self, surface):
        surface.blit(self.npc, (self.x, self.y))
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 50, 75), 2)
    
    def counter(self):
        self.counts = 0
        for i in range(self.delay):
            self.counts += 1
        return self.counts
    
    def interaction(self, surface, answers, whenQ):
        player.speedX = 0
        player.speedY = 0
        player.sprite_directions[player.index].count_speed = 0 # Player Stops
        player.sprite_directions[player.index].index = 1 # The sprite animation stops at the static sprite
        self.words.createTextbox(surface, (0, 0, 0), (0, 0, 255), (0, 300, 600, 150))
        self.words.type(surface, rate=20)
        if self.count == whenQ:
            self.ans = TypeWriter(answers[0] + "\n" + answers[1], 15, f"Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 25, 300)
            self.ans.type(surface, rate=1)
        if self.words.finish is True:
            if self.counter() == self.delay:
                self.words = TypeWriter(self.text.readline(), 15, f"Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 25, 325)
                self.count += 1


gameCam = Camera(0, 0)
run = True
npcTalk = False
player = Player("Hero", 0, 0, 25, gameCam)
npc = NPC(1, 300, 225, 25, gameCam, f"Assets\\Characters\\Character_2\\tile016.png")
surface = pygame.display.set_mode((600, 450))
whenQ = 6

while run:
    surface.fill((255, 255, 255))
    if keyboard.is_pressed("space"):
        npcTalk = True
    if npc.count == whenQ:
        npcTalk = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    
    player.walk(surface, 0.05)
    npc.draw(surface)
    if npcTalk is True:
        npc.interaction(surface, ["Yes", "No"], whenQ)
    pygame.display.update()
