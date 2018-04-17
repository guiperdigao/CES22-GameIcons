
import math, random, sys
import pygame
from pygame.locals import *


# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface			
W, H = 800, 450
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("Fase_1.png").convert_alpha()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth
stagePosX = 0
stageHeight = bgHeight
stagePosY = 0

startScrollingPosX = int(round(W/2))
startScrollingPosY = 50

playerPosX = 16
tamaPosX = playerPosX
playerPosY = HH
tamaPosY = playerPosY
playerVelocityX = 0
playerVelocityY = 0

#Define soil
soil = pygame.image.load("soil.png").convert_alpha()
soil_mask = pygame.mask.from_surface(soil)
soil_rect = soil.get_rect()
ox = HW - soil_rect.center[0]
oy = HH - soil_rect.center[1]

tama = pygame.image.load("tama.png").convert_alpha()
tamaWidth, tamaHeight = tama.get_rect().size
tamac = pygame.image.load("tamac.png").convert_alpha()
tama_mask = pygame.mask.from_surface(tama)
tama_rect = tama.get_rect()
tama_col = tama

# main loop
while True:
    events()
    k = pygame.key.get_pressed()
    playerVelocityX = 0
    playerVelocityY = 0
    if k[K_RIGHT]:
        playerVelocityX = 1
        if k[K_LEFT]:
            playerVelocityX = -1
        elif k[K_UP]:
            playerVelocityY = -1
            playerVelocityX = 0
        elif k[K_DOWN]:
            playerVelocityY = 1
            playerVelocityX = 0
    elif k[K_LEFT]:
        playerVelocityX = -1
        if k[K_RIGHT]:
            playerVelocityX = 1
        elif k[K_UP]:
            playerVelocityY = -1
            playerVelocityX = 0
        elif k[K_DOWN]:
            playerVelocityY = 1
            playerVelocityX = 0
    elif k[K_UP]:
        playerVelocityY = -1
        if k[K_DOWN]:
            playerVelocityY = 1
    elif k[K_DOWN]:
        playerVelocityY = 1
        if k[K_UP]:
            playerVelocityY = -1

    offset = (int(playerPosX), int(playerPosY - (tamaHeight / 2)))
    result = soil_mask.overlap(tama_mask, offset)
    if result:
        tama_col = tamac
        if playerVelocityX == 1:
            playerPosX -= playerVelocityX
            playerVelocityX = 0
        elif playerVelocityX == -1:
            playerPosX -= playerVelocityX
            playerVelocityX = 0
        elif playerVelocityY == -1:
            playerPosY -= playerVelocityY
            playerVelocityY = 0
        elif playerVelocityY == 1:
            playerPosY -= playerVelocityY
            playerVelocityY = 0
    else:
        playerPosX += playerVelocityX
        playerPosY += playerVelocityY

    if playerPosX > stageWidth - (tamaWidth/2):
        playerPosX = stageWidth - (tamaWidth/2)
    if playerPosX < (tamaWidth/2):
        playerPosX = (tamaWidth/2)
    if playerPosX < startScrollingPosX:
        tamaPosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX:
        tamaPosX = playerPosX - stageWidth + W
    else:
        tamaPosX = startScrollingPosX
        stagePosX += -playerVelocityX

    if playerPosY < (tamaHeight/2):
        playerPosY = tamaHeight
    elif playerPosY > 450:
        playerPosY = 450
    else:
        tamaPosY = startScrollingPosY
        stagePosY += -playerVelocityY
    rel_y = stagePosY % bgHeight
    DS.blit(bg, (rel_y - bgHeight, 0))
    DS.blit(soil, (rel_y - bgHeight, 0))
    if rel_y > H:
        DS.blit(bg, (rel_y, 0))
    rel_x = stagePosX % bgWidth
    DS.blit(bg, (rel_x - bgWidth, 0))
    DS.blit(soil, (rel_x - bgWidth, 0))
    if rel_x < W:
        DS.blit(bg, (rel_x, 0))
        DS.blit(soil, (rel_x, 0))

    tama_col = tama
    DS.blit(tama_col, (tamaPosX, playerPosY - (tamaHeight / 2)))
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)