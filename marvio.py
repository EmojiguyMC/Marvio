import pygame
import random
from time import sleep as s

pygame.init()
font = pygame.font.SysFont("Minecraft", 25, bold=True)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Marvio Bros")

clock = pygame.time.Clock()
running = True
dirtLight = (128, 69, 19)
dirtDark = (82, 43, 10)
sky = (191, 229, 239)
grassLight = (125, 238, 109)
grassDark = (115, 206, 102)
white = (255, 255, 255)
black = (0, 0, 0)
pC = [375, 275]
pVel = [0, .01]
ground = pygame.image.load('ground.png').convert()
ground = pygame.transform.scale(ground, (80, 80))
bricks = pygame.image.load('bricks.png').convert()
bricks = pygame.transform.scale(bricks, (80, 80))

def closecode():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()


while running:
    closecode()
    # level
    pygame.draw.rect(screen, sky, (0, 0, 800, 600))

    # player
    if pygame.key.get_pressed()[pygame.K_d]:
        pVel[0] += .4
    if pygame.key.get_pressed()[pygame.K_a]:
        pVel[0] -= .4
    if not pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]:
        if pVel[0] < 0:
            pVel[0] += .6
        elif pVel[0] > 0:
            pVel[0] -= .6
        elif pVel[0] > 0:
            pVel[0] = 0
        elif pVel[0] > .4:
            pVel[0] = .4
    if pC[0] <= 0:
        pVel[0] = 0
        pC[0] = 1
    if pC[0] >= 720:
        pVel[0] = 0
        pC[0] = 719
    else:
        pC[0] += pVel[0]
    if pygame.key.get_pressed()[pygame.K_w] and pC[1] == 390:
        pVel[1] -= 30
    if pC[1] != 390:
        pVel[1] += 2
    if pC[1] > 390:
        pC[1] = 390
        pVel[1] = 0

    pC[1] += pVel[1]
    pygame.draw.rect(screen, white, (pC[0], pC[1], 50, 50))
    pygame.draw.rect(screen, black, (pC[0], pC[1], 50, 50), 5)
    screen.blit(ground, (0, 520))
    screen.blit(ground, (0, 440))
    screen.blit(ground, (80, 520))
    screen.blit(ground, (80, 440))
    screen.blit(ground, (160, 520))
    screen.blit(ground, (160, 440))
    screen.blit(ground, (240, 520))
    screen.blit(ground, (240, 440))
    screen.blit(ground, (320, 520))
    screen.blit(ground, (320, 440))
    screen.blit(ground, (400, 520))
    screen.blit(ground, (400, 440))
    screen.blit(ground, (480, 520))
    screen.blit(ground, (480, 440))
    screen.blit(ground, (560, 520))
    screen.blit(ground, (560, 440))
    screen.blit(ground, (640, 520))
    screen.blit(ground, (640, 440))
    screen.blit(ground, (720, 520))
    screen.blit(ground, (720, 440))
    # screen.blit(bricks, (0, 240))
    pygame.display.update()
    clock.tick(60)
