import pygame, sys, time
from Modules.Character_Modules.Player import Player

pygame.init()
run = True

# Window Name
caption = "Indie.exe"

info = pygame.display.Info() # finds info about the CURRENT DISPLAY BEING USED
# Note: We must make EVERY value in the game proportional to the display size NOT!!! the screen size
screenX = 1500
screenY = 800

pygame.display.set_caption(caption)
surface = pygame.display.set_mode((screenX, screenY))
main_clock = pygame.time.Clock()
frames_per_second = 60
last_time = time.time()

# Background Colour 
white = (255, 255, 255)

# Main Character Class
mc = Player("Test Player", screenX//2, screenY//2, 25)

while run:

    dt = time.time() - last_time
    dt*=frames_per_second
    last_time = time.time()


    surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 

    pygame.display.update()
