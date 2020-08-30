import sys, pygame
import random
pygame.init()

size = width, height = 600, 490
speed = [2, 2]
colour = [0, 0, 0]

screen = pygame.display.set_mode(size)

ghost = pygame.image.load("ghost.png")
fire = pygame.image.load('fire.png')
heart = pygame.image.load('heart.png')
ghostrect = ghost.get_rect()
firerect = fire.get_rect()
heartrect = heart.get_rect()


def recolour(list):
    for a in range(len(list)):
        list[a] = random.randint(0,255)
# def relocate()

up = [0,-10]
down = [0,10]
left = [-10,0]
right = [10,0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ghostrect.move_ip(up)
            elif event.key == pygame.K_DOWN:
                ghostrect.move_ip(down)
            elif event.key == pygame.K_LEFT:
                ghostrect.move_ip(left)
            elif event.key == pygame.K_RIGHT:
                ghostrect.move_ip(right)




    if ghostrect.contains(firerect) == True:


    # ballrect.move_ip(speed)
    # if ballrect.left < 5:
    #     if event.key == pygame.K_LEFT:
    #         ballrect.move_ip([0,0])
    # if ballrect.right < 5:
    #     if event.key == pygame.K_RIGHT:
    #         ballrect.move_ip([0, 0])
    # if ballrect.top < 5:
    #     if event.key == pygame.K_UP:
    #         ballrect.move_ip([0, 0])
    # if ballrect.bottom < 5:
    #     if event.key == pygame.K_DOWN:
    #         ballrect.move_ip([0, 0])

    screen.fill(colour)
    screen.blit(ghost, ghostrect)
    screen.blit(heart, heartrect)
    pygame.display.flip()