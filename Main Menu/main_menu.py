import math, random, sys
import pygame
from pygame.locals import *

class main_menu_animation:
	def __init__(self, filename = "Tela_inicial.png", cols = 4, rows = 3):
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

class button:
    #Creates the buttons to start the game, go to section 'How to Play' and to close this section
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw, hh = self.cellCenter = (int(w / 2), int(h / 2))
        
        self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([(0, 0), (-hw, 0), (-w, 0),(0, -hh), (-hw, -hh), (-w, -hh),(0, -h), (-hw, -h), (-w, -h),])
            
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

   
# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

def menu():
    intro = True
    global CLOCK
    CLOCK = pygame.time.Clock()
    global DS
    DS = pygame.display.set_mode((W, H))
    global FPS
    FPS = 4
    # define some colors
    global BLACK
    BLACK = (0, 0, 0, 255)
    global WHITE
    WHITE = (255, 255, 255, 255)
    global CENTER_HANDLE
    CENTER_HANDLE = 4
    global index
    index = 0
    global s
    s = main_menu_animation("Tela_inicial.png", 4, 3)
    while intro:
        events()
        s.draw(DS, index % s.totalCellCount, HW, HH, CENTER_HANDLE)
        if index<=9:
            index += 1
            CLOCK.tick(FPS)

        start_but = button("start_button.png", 2, 1)
        howto_but = button("howto_button.png",2,1)
        exit_but = button("exit_button.png",2,1)
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        x=HW-200
        y=HH+100
        if index==10:
            if 280 > mouse[0] > 120 and 360 > mouse[1] > 300:
                start_but.draw(DS, 1 % s.totalCellCount, x, y, CENTER_HANDLE)
                if click[0] == 1:
                    print("OK!") #ALTERAR        
            else:
                start_but.draw(DS, 0 % s.totalCellCount, x,y, CENTER_HANDLE)
            if 480 > mouse[0] > 320 and 360 > mouse[1] > 300:
                howto_but.draw(DS, 1 % s.totalCellCount, 200+x, y, CENTER_HANDLE)
                if click[0] == 1:
                    index = 11
            else:
                howto_but.draw(DS, 0 % s.totalCellCount,200+ x,y, CENTER_HANDLE)
        if index==11:
            if 777 > mouse[0] > 752 and 43 > mouse[1] > 18:
                exit_but.draw(DS, 1 % s.totalCellCount, 764, 31, CENTER_HANDLE)
                if click[0] == 1:
                    index = 10
            else:
                exit_but.draw(DS, 0 % s.totalCellCount,  764, 31, CENTER_HANDLE)
        pygame.display.update()


# define display surface
W, H = 800, 450
HW, HH = W / 2, H / 2
AREA = W * H

pygame.init()
menu()