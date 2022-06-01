from xml.etree.ElementTree import TreeBuilder
import pygame, sys, time, os
from Modules.Character_Modules.Player import Player
from Modules.System_Modules.TypeWriter import TypeWriter
from Modules.System_Modules.SpriteHandler import SpriteHandler
from Modules.System_Modules.SoundHandler import SoundHandler

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

# Opening Scene Variables --> WILL BE MOVED TO A MODULE IN THE SCENE MODULE FOLDER. THIS IS ONLY HERE FOR TESTING
#surface2 = pygame.Surface((screenX, screenY))

title_music = SoundHandler("Assets\\Audio\\title.wav", 0, False)
introduction_sound = SoundHandler("Assets\\Audio\\Introduction_Audio\\Introduction_1.wav", 1, False)

ominous_text = TypeWriter("You are not supposed to be here... \nThis place is not meant for you... \n             Please... \n        Turn back now...", 32, "Assets\\Fonts\\Volter__28Goldfish_29.ttf", (255, 255, 255), 400, (screenY//2)-50)
ominous_text_bool = True
Opening_Glitch_Surface = pygame.Surface((screenX, screenY))
glitch = SpriteHandler(f"Assets\\Animations\\Glitch_Sprite\\", 10, "png")
opening_glitch_bool = True
opening_glitch_sound = SoundHandler("Assets\\Audio\\Opening_Cinematic_Glitch.wav", 1, False)

opening_cinematic_bool = False
opening_cinematic = pygame.Surface((screenX, screenY))
castle_background = SpriteHandler(f"Assets\\Animations\\Castle_Background\\", 22, "png")
castleX, castleY = 0, -300

while run:
    dt = time.time() - last_time
    dt *= frames_per_second
    last_time = time.time()

    surface.fill(background_color)
    Opening_Glitch_Surface.fill((0, 0, 0))


    opening_cinematic.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit() 

    if ominous_text_bool:
        ominous_text.type(Opening_Glitch_Surface, 30)

    if ominous_text.finish == True:
        ominous_text_bool = False
        glitch.animate(Opening_Glitch_Surface, 0, 0, 100, 10, False)
        opening_glitch_sound.play()
        if glitch.isBlit == False:
            opening_glitch_bool = False
            opening_cinematic_bool = True

    if opening_glitch_bool == True:
        surface.blit(Opening_Glitch_Surface, (0, 0))
    elif opening_cinematic_bool == True:
        castle_background.animate(opening_cinematic, castleX, castleY, 1000, 35)
        surface.blit(opening_cinematic, (0, 0))
        castleX -= 0.07
        castleY += 0.04
        title_music.play(0.3)
        introduction_sound.play()

    pygame.display.update()
