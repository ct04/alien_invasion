import sys, pygame
import random
pygame.init()

size = width, height = 600, 400
speed = [2, 2]
colour = [0, 0, 0]

screen = pygame.display.set_mode(size)

ghost = pygame.image.load("ghost.png")
ghostrect = ghost.get_rect()

def recolour(list):
    for a in range(len(list)):
        list[a] = random.randint(0,255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ghostrect.move_ip(speed)
    if ghostrect.left < 0 or ghostrect.right > width:
        speed[0] = -speed[0]
        recolour(colour)
    if ghostrect.top < 0 or ghostrect.bottom > height:
        speed[1] = -speed[1]
        recolour(colour)



    screen.fill(colour)
    screen.blit(ghost, ghostrect)
    pygame.display.flip()