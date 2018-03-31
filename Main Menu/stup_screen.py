import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

def init_screen():
    # define display surface			
    W, H = 800, 450
    HW, HH = W / 2, H / 2
    AREA = W * H

    # initialise display
    pygame.init()
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W, H))
    FPS = 4
    # define some colors
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)