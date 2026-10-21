""" the start of my basketball pygame
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Blake's Basketball")

my_image = pygame.image.load("assignments/code_jam/media/ball.png")


image_rect = my_image.get_rect()
image_rect.topleft = (480, 260)

dragging = False
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Start moving when right-clicking the basketball
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and image_rect.collidepoint(event.pos):
                dragging = True

        # Stop moving when right-click is released
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                dragging = False

    # Move the basketball while holding right-click
    if dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        image_rect.center = (mouse_x, mouse_y)

    screen.fill((0, 0, 100))
    screen.blit(my_image, image_rect)

    pygame.display.flip()

pygame.quit()