import pygame, sys
from Modules.Character_Modules.Player import Player

pygame.init()
run = True

caption = "Indie.exe"

info = pygame.display.Info() # finds info about the CURRENT DISPLAY BEING USED
# Note: We must make EVERY value in the game proportional to the display size NOT!!! the screen size
screenX = info.current_w - 100
screenY = info.current_h - 100

pygame.display.set_caption(caption)
surface = pygame.display.set_mode((screenX, screenY))

white = (255, 255, 255)

mainCharacer = Player("Joshua Zive")
mainCharacer.load_sprite_images(3, "Assets\\Characters\\Character_1\\Down\\")


while run:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 
    mainCharacer.draw_animation(surface, screenX//2, screenY//2, 50, 20)
    pygame.display.update()
