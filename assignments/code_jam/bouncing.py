import pygame
import sys
import random

pygame.init()
screensize = (800,600)
screen = pygame.display.set_mode(screensize,0)
pygame.display.set_caption("Animation Test")
clock = pygame.time.Clock()

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

radius = 25
color_list = [WHITE]

def createball():
    x = random.randint(radius, screensize[0]-radius)
    y = random.randint(radius, screensize[1]-radius)
    color = random.choice(color_list)
    return x, y, 2, 2, color

def moveball(x, y, dx, dy, color):
    x, y = x + dx, y + dy
    if not radius < x < screensize[0]-radius:
        dx = -dx
        color = random.choice(color_list)
    if not radius < y < screensize[1]-radius:
        dy = -dy
        color = random.choice(color_list)
    return x, y, dx, dy, color

x, y, dx, dy, color = createball()

go = True
while go:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False

    x, y, dx, dy, color = moveball(x, y, dx, dy, color)
   

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (x, y), radius)
    
    pygame.display.flip()