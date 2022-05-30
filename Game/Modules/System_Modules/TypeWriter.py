import pygame
from pygame import gfxdraw

class TypeWriter(object):
    def __init__(self, text, size, font, colour, x, y):
        
        self.text = text
        self.lines = self.text.split('\n')

        self.empty_text = ["" for i in range(len(self.lines))]

        self.x = x
        self.y = [y for i in range(len(self.lines))]

        self.size = size
        self.space = self.size + 10

        self.colour = colour

        self.font = pygame.font.Font(font, self.size)
        self.text_written = False
        self.count = 0
        self.count_speed = 1
        self.finish = False

        self.line_index = 0
        self.index = 0
        self.count = 0


    def createTextbox(self, surface, color, boarder_color,  rect, width=1):
        x, y, w, h = rect
        width = max(width, 1)  # Draw at least one rect
        width = min(min(width, w // 2), h // 2)  # Don't overdraw

        pygame.draw.rect(surface, color, rect)

        for i in range(width):
            gfxdraw.rectangle(surface, (x + i, y + i, w - i * 2, h - i * 2), boarder_color)
    
    def type_init(self, rate):
        self.text_surface = [self.font.render(i, True, self.colour) for i in self.empty_text]
        if self.finish == False:
            if self.index > len(self.lines[self.line_index])-1:
                self.text_written = True
            
            if self.text_written == False:
                self.count += self.count_speed
                if self.count > rate:
                    self.empty_text[self.line_index] += self.lines[self.line_index][self.index]
                    self.index += 1
                    self.count = 0
            else:
                self.index = 0
                self.count = 0 
                self.line_index += 1
                self.y[self.line_index] += self.space
                self.space += (self.size + 10)
                self.text_written = False

        print(self.space)

        if self.line_index == len(self.lines)-1 and len(self.empty_text[self.line_index]) == len(self.lines[-1]):
            self.finish = True

    def type(self, surface, rate=10):
        self.type_init(rate)
        for i in range(len(self.lines)):
            surface.blit(self.text_surface[i], (self.x, self.y[i]))
        
            


