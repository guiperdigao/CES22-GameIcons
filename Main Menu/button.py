import math, random, sys
import pygame
from stup_screen import *
from pygame.locals import *

class button:
    #Creates the buttons to start the game, go to section 'How to Play' and to close this section
    def call_sheet(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows
		
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw, hh = self.cellCenter = (int(w / 2), int(h / 2))
        
        self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([
			(0, 0), (-hw, 0), (-w, 0),
			(0, -hh), (-hw, -hh), (-w, -hh),
			(0, -h), (-hw, -h), (-w, -h),])
            
    def draw(self, surface, cellIndex, x, y, handle = 0):
	    surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

    def start_button(self,x,y):
        s = self.call_sheet("start_button.png", 2, 1)
        DS = pygame.display.set_mode((800, 450))
        #Button to initialize game
        CENTER_HANDLE = 4
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+160 > mouse[0] > x and y+61 > mouse[1] > y:
            s.draw(DS, 1 % s.totalCellCount, x, y, CENTER_HANDLE)

            if click[0] == 1: #Colocar and != action
                print("OK!") #ALTERAR        
        else:
            s.draw(DS, 0 % s.totalCellCount, x,y, CENTER_HANDLE)
