import pygame
pygame.init()

#game icon
gameIcon = pygame.image.load("/csc_141/assignments/code_jam/media/ball.png")
pygame.display.set_icon(gameIcon)

#window
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Bouncing Basketball")

#class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        #load ball image
        self.image = pygame.image.load("/csc_141/assignments/code_jam/media/ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.speed = 10
        self.vel_x = 1
        self.vel_y = 1

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def bounce(self):
        #bounce off top and bottom
        if self.y <= 0 or self.y >= 500:
            self.vel_y = -self.vel_y

        #bounce off left and right
        if self.x <= 0 or self.x >= 920:
            self.vel_x = -self.vel_x

        #move ball
        self.y += self.speed * self.vel_y
        self.x += self.speed * self.vel_x


#object
ball = Ball(480, 270)

#clock
clock = pygame.time.Clock()

#event handler
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    ball.bounce()
    ball.draw()

    pygame.display.flip()

pygame.quit()