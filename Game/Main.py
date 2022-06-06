import pygame, sys, time, os
from Modules.Character_Modules.Player import Player
from Modules.Scene_Modules.Opening_Sequence import Scene_1
from Modules.System_Modules.CameraClass import Camera
from Modules.Scene_Modules.Game_Scene_1 import Map

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

# Cameras
scene_cam = Camera(0, 0)
game_cam = Camera(0, 0)

# Scenes
scene_1 = Scene_1(scene_cam)

mc = Player("Hero", 0, 0, 25, game_cam)
#scene_1.scene_finished = True

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
    scene_1.draw(surface, dt)
    if scene_1.scene_finished == True:
        print("IS HAPPENING")
        mc.walk(surface, dt)
    pygame.display.update()
