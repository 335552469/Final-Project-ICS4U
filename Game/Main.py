import pygame, sys, time, os
from Modules.Character_Modules.Player import Player
from Modules.Scene_Modules.Opening_Sequence import Scene_1

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

run = True

path = os.getcwd()
print(path)

# Window Name
caption = "Indie.exe"

info = pygame.display.Info() # finds info about the CURRENT DISPLAY BEING USED
# Note: We will edit the code so we can have the game work for any screen size

screenX = 1500
screenY = 700

pygame.display.set_caption(caption)
surface = pygame.display.set_mode((screenX, screenY))
main_clock = pygame.time.Clock()
frames_per_second = 144
last_time = time.time()
# Background Colour 
background_color = (0, 0, 0)

# Main Character Classa
mc = Player("Test Player", screenX//2, screenY//2, 25)

# Scenes
scene_1 = Scene_1()

while run:

    # Framerate independance 
    dt = time.time() - last_time
    dt *= frames_per_second
    last_time = time.time()

    surface.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 
    scene_1.draw(surface)
    pygame.display.update()
