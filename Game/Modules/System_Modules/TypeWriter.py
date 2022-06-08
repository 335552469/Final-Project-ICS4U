import pygame
from pygame import gfxdraw
from Game.Modules.System_Modules.SoundHandler import SoundHandler


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
        self.text_written = False
        self.finish = False

        # Dispersion variables
        self.count = 0
        self.line_index = 0
        self.index = 0
        self.count = 0


    # Draws a textbox to the screen
    def createTextbox(self, surface, color, boarder_color,  rect, width=1):
        x, y, w, h = rect # Isolates rect values
        width = max(width, 1)  # Draw at least one rect
        width = min(min(width, w // 2), h // 2)  # Don't overdraw

        # Draws a basic rectangle
        pygame.draw.rect(surface, color, rect)

        # Draws a rectangle but only the boarder and then expands it increasingly to mimic a boarder
        for i in range(width):
            gfxdraw.rectangle(surface, (x + i, y + i, w - i * 2, h - i * 2), boarder_color)
    
    # Initializes the typing
    def type_init(self, rate, delay=0):
        self.text_surface = [self.font.render(i, True, self.colour) for i in self.empty_text] # Renders multiple text lines
        if self.finish == False: # Used to check if everything is written to the screen
            if self.index > len(self.lines[self.line_index])-1:
                self.text_written = True
            
            if self.text_written == False: # Used to check if a line is written
                self.count += 1 # Counter starts
                if self.count > rate: # uses the count rate to time the letters being placed
                    self.empty_text[self.line_index] += self.lines[self.line_index][self.index] # adds the letter to the empty
                    self.index += 1 # Goes to the next letter
                    self.count = 0 # Resets counter
            else: # When a line is finished 
                #pygame.time.delay(delay) # Optional delay

                # Resets the values for the next line
                self.index = 0 
                self.count = 0 
                self.line_index += 1
                self.text_written = False

                # Spaces out the next line
                self.y[self.line_index] += self.space
                self.space += (self.size + 10)

        # Checks if the sentance is finished
        if self.line_index == len(self.lines)-1 and len(self.empty_text[self.line_index]) == len(self.lines[-1]):
            self.finish = True

    def type(self, surface, rate=10, delay=1000):

        # Runs the init
        self.type_init(rate, delay)

        # Blits our lines
        for i in range(len(self.lines)):
            surface.blit(self.text_surface[i], (self.x, self.y[i]))
        
            


