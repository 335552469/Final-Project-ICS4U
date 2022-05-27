import pygame, sys

pygame.init()
run = True

caption = "Indie.exe"
info = pygame.display.Info()
screenX = info.current_w - 100
screenY = info.current_h - 100

pygame.display.set_caption(caption)
surface = pygame.display.set_mode((screenX, screenY))

white = (255, 255, 255)

while run:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 

    pygame.display.update()
