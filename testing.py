import pygame, os
pygame.init() 


run = True
surface = pygame.display.set_mode((500, 500))

path = os.getcwd()
img = pygame.image.load(f"{path}\\Assets\\Animations\\Caped_Hero_Background\\Caped_Hero_Background_0000_Layer-20.png")
resize = pygame.transform.scale(img, (img.get_width(), img.get_height()))

class Camera(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.origin = (x - x, y - y)

        self.width = width
        self.height = height
        
        self.differentiate_bool = True

        self.objects = []
    
    def differentiate(self):
        print(self.objects)
        for i in self.objects:
            if event.type == pygame.KEYDOWN:
                print(self.x, self.y)
                if event.key == pygame.K_w:
                    self.y -= 10
                    i[1] += self.y
                elif event.key == pygame.K_a:
                    self.x -= 10
                    i[0] -= self.x
                elif event.key == pygame.K_s:
                    self.y += 10
                    i[1] += self.y
                elif event.key == pygame.K_d:
                    self.x += 10
                    i[0] -= self.x

        
        
square_coords = [250, 100]
x = 0
y = 0
cam = Camera(x, y, 500, 500)
cam.objects.append(square_coords)
while run:
    surface.fill((255, 255, 255))
    pygame.draw.rect(surface, (255, 0, 0), (square_coords[0], square_coords[1], 25, 25))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        cam.differentiate()


    pygame.display.update()
