import pygame, time
pygame.init() 

run = True
surface = pygame.display.set_mode((500, 500))

main_clock = pygame.time.Clock()
frames_per_second = 144
last_time = time.time()

class Box(object):
    
    def __init__(self, rect):
        self.x, self.y, self.w, self.h = rect

    def draw_rect(self, surface, color):
        self.rectValue = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(surface, color, self.rectValue)

class HitBox(Box):

    def __init__(self, rect):
        super().__init__(rect)
    
    def isHit(self, other):
        if other.x + other.w >= self.x and other.y + other.h >= self.y:
            if other.x <= self.x + self.w and other.y <= self.y + self.h:
                return True
        return False

player1 = Box((0, 0, 50, 50))
hitbox1 = HitBox((250, 250, 50, 50))

while run:
    print(player1.x, player1.y)
    dt = time.time() - last_time
    dt *= frames_per_second
    last_time = time.time()

    surface.fill((255, 255, 255))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    player1.draw_rect(surface, (255, 0, 0))
    hitbox1.draw_rect(surface, (0, 0, 255))
    hitbox1.isHit(player1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= 1*dt
    elif keys[pygame.K_s]:
        player1.y += 1*dt
    elif keys[pygame.K_d]:
        player1.x += 1*dt
    elif keys[pygame.K_a]:
        player1.x -= 1*dt

    pygame.display.update()