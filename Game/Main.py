from xml.etree.ElementTree import TreeBuilder
import pygame, sys, time, os
from Modules.Character_Modules.Player import Player
from Modules.System_Modules.TypeWriter import TypeWriter

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

run = True
path = os.getcwd()

pygame.mixer.init()

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

# Opening Scene Variables --> WILL BE MOVED TO A MODULE IN THE SCENE MODULE FOLDER. THIS IS ONLY HERE FOR TESTING
#surface2 = pygame.Surface((screenX, screenY))
ominous_text = TypeWriter("You are not supposed to be here... \nThis place is not meant for you... \n             Please... \n        Turn back now...", 32, "Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 400, (screenY//2)-50)
surface2 = pygame.Surface((screenX, screenY))
while run:


    dt = time.time() - last_time
    dt*=frames_per_second
    last_time = time.time()

    surface.fill(background_color)
    surface2.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 

    ominous_text.type(surface2, 30)
    surface.blit(surface2, (0, 0))
    pygame.display.update()