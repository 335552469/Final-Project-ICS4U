import pygame
from pygame import gfxdraw

class TypeWriter(object):
    def __init__(self, text, size, font, colour):
        
        self.text = text
        self.lines = self.text.split('\n')

        self.empty_text = ""

        self.size = size

        self.colour = colour

        self.font = pygame.font.SysFont(font, self.size)

        self.index = 0
        self.text_written = False
        self.count = 0


        self.index = 0


    def createTextbox(self, surface, color, boarder_color,  rect, width=1):
        x, y, w, h = rect
        width = max(width, 1)  # Draw at least one rect
        width = min(min(width, w // 2), h // 2)  # Don't overdraw

        pygame.draw.rect(surface, color, rect)

        for i in range(width):
            gfxdraw.rectangle(surface, (x + i, y + i, w - i * 2, h - i * 2), boarder_color)
