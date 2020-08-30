import sys, pygame
import random
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
colour = [255, 17, 0]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
# ballrect = ballrect.move(200, 20)


def recolour(list):
    for a in range(len(list)):
        list[a] = random.randint(0,255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    ballrect.move_ip(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]



    screen.fill(colour)
    screen.blit(ball, ballrect)
    pygame.display.flip()