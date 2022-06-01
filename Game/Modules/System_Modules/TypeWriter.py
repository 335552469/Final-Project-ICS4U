import pygame
from pygame import gfxdraw
from Modules.System_Modules.SoundHandler import SoundHandler


# This class writes lines of text in order depending on where the \n values exist within the text

class TypeWriter(object):
    def __init__(self, text, size, font, colour, x, y):
        
        # Attributes 
        self.text = text
        self.size = size
        self.colour = colour
        self.x = x

        # line variables
        self.lines = self.text.split('\n') # splits the sentance into a list of lines
        self.empty_text = ["" for i in range(len(self.lines))] # different lines require different empty strings
        self.space = self.size + 10 # Space in between each line
        self.y = [y for i in range(len(self.lines))] # Multiple lines have different y values

        # font variables
        self.font = pygame.font.Font(font, self.size)

        self.type_sound = SoundHandler("Assets\\Audio\\type_sound.wav", 2, False)

        # Text Bools
        self.text_written = False # Checks if a line is written
        self.finish = False # Checks if the sentance is written

        # Dispersion variables
        self.count = 0
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
    
    def type_init(self, rate, delay):
        self.text_surface = [self.font.render(i, True, self.colour) for i in self.empty_text]
        if self.finish == False:
            if self.index > len(self.lines[self.line_index])-1:
                self.text_written = True
            
            if self.text_written == False:
                self.count += 1
                if self.count > rate:
                    self.empty_text[self.line_index] += self.lines[self.line_index][self.index]
                    self.index += 1
                    self.count = 0
            else:
                pygame.time.delay(delay)
                self.index = 0
                self.count = 0 
                self.line_index += 1
                self.y[self.line_index] += self.space
                self.space += (self.size + 10)
                self.text_written = False

        if self.line_index == len(self.lines)-1 and len(self.empty_text[self.line_index]) == len(self.lines[-1]):
            self.finish = True

    def type(self, surface, rate=10, delay=1000):
        self.type_init(rate, delay)
        for i in range(len(self.lines)):
            surface.blit(self.text_surface[i], (self.x, self.y[i]))
        
            


