import math, random, sys
from stup_screen import *
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

	def start(self):
		CENTER_HANDLE = 4
		index = 0
		s = self.__init__("Tela_inicial.png", 4, 3)
		# main loop
		while True:
			events()

			s.self.draw(DS, index % s.totalCellCount, HW, HH, CENTER_HANDLE)
			if index<=9:
				index += 1

			pygame.display.update()
			CLOCK.tick(FPS)
			DS.fill(BLACK)	

	def draw(self, surface, cellIndex, x, y, handle = 0):
		surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
	
