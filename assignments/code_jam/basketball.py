""" the start of my basketball pygame
"""
import pygame


pygame.init()
screen = pygame.display.set_mode((960,540))
pygame.display.set_caption("Blake's Basketball")

my_image = pygame.image.load("assignments/code_jam/media/ball.png")


image_rect = my_image.get_rect()
image_rect.topleft = (480, 260)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(my_image, image_rect)
    pygame.display.flip()


