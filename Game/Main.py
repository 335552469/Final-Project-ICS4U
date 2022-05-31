import pygame, sys, time
from Modules.Character_Modules.Player import Player
from Modules.System_Modules.TypeWriter import TypeWriter

pygame.init()
run = True

pygame.mixer.init()
sound = pygame.mixer.Sound("Assets\\Audio\\Menue_Theme.wav")

# Window Name
caption = "Indie.exe"

info = pygame.display.Info() # finds info about the CURRENT DISPLAY BEING USED
# Note: We must make EVERY value in the game proportional to the display size NOT!!! the screen size
screenX = 1500
screenY = 700

pygame.display.set_caption(caption)
surface = pygame.display.set_mode((screenX, screenY))
main_clock = pygame.time.Clock()
frames_per_second = 60
last_time = time.time()
# Background Colour 
background_color = (0, 0, 0)

# Main Character Class
mc = Player("Test Player", screenX//2, screenY//2, 25)

text = TypeWriter("Hello My name is Josh nice to meet you. \nThis is the game called indie.exe. \nThis game will be my final Game. \nThis is a test to see if the typewriter class works:) \nHere is one last test to check if the typewriter class works", 
                  24, 'Assets\\Fonts\\Volter__28Goldfish_29.ttf', (255, 255, 255), 0, 0)


while run:

    dt = time.time() - last_time
    dt*=frames_per_second
    last_time = time.time()


    surface.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 
    # text.createTextbox(surface, (0, 0, 0), (255, 255, 255), (50, screenY//2, 1400, 200), 5)
    text.type(surface)
    pygame.display.update()