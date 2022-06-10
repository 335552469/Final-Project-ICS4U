import pygame 

class HitBox(object):
    def __init__(self, rect, camera):
        self.x, self.y, self.width, self.height = rect
        self.rect = rect
        self.camera = camera
        self.coords = [self.x, self.y]
        self.camera.obj.append(self.coords)
    
    def createBox(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.coords[0], self.coords[1], self.width+2, self.height+2))

    def isHit(self, other):
        self.side_coords = [other.y, other.y+other.height//2, other.y + other.height]
        self.topdown_coords = [other.x, other.x+other.width//2, other.x + other.width]

        print([other.x, other.y], [self.coords[0], self.coords[1]])
        if other.x+2 + other.width >= self.coords[0] and other.x+2 + other.width <= self.coords[0] + self.width: # Left Side
            for i in self.side_coords:
                if i >= self.coords[1] and i <= self.coords[1] + self.height:
                    return "Left Hit"
        elif other.x-2 <= self.coords[0] + self.width and other.x-2 >= self.coords[0]:
            for i in self.side_coords:
                if i >= self.coords[1] and i <= self.coords[1] + self.height:
                    return "Right Hit"
        if other.y+2 + other.height >= self.coords[1] and other.y+2 + other.height <= self.coords[1] + self.height:
            for i in self.topdown_coords:
                if i >= self.coords[0] and i <= self.coords[0] + self.width:
                    return "Top Hit"
        elif other.y-2 <= self.coords[1] + self.height and other.y-2 >= self.coords[1]:
            for i in self.topdown_coords:
                if i >= self.coords[0] and i <= self.coords[0] + self.width:
                    return "Bottom Hit"