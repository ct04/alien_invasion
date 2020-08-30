import sys, pygame
import random
pygame.init()

size = width, height = 600, 400
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

up = [0,-10]
down = [0,10]
left = [-10,0]
right = [10,0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ghostrect.move_ip(up)
            elif event.key == pygame.K_DOWN:
                ghostrect.move_ip(down)
            elif event.key == pygame.K_LEFT:
                ghostrect.move_ip(left)
            elif event.key == pygame.K_RIGHT:
                ghostrect.move_ip(right)

    # EVENT1 = firerect.move_ip([random.randint(-300, 300), random.randint(-200, 200)])
    #
    # pygame.time.set_timer(EVENT1, 100)

    if ghostrect.left < 0 or ghostrect.right > width:
        recolour(colour)
    if ghostrect.top < 0 or ghostrect.bottom > height:
        recolour(colour)

    # if ghostrect.left < 0:
    #     if event.key == pygame.K_LEFT:
    #         pygame.event.set_blocked(pygame.K_LEFT)
    #         event.type == pygame.key
    # if ghostrect.right > width:
    #     if event.key == pygame.K_RIGHT:
    #         ghostrect.move_ip([0, 0])
    # if ghostrect.top < 0:
    #     if event.key == pygame.K_UP:
    #         ghostrect.move_ip([0, 0])
    # if ghostrect.bottom > height:
    #     if event.key == pygame.K_DOWN:
    #         ghostrect.move_ip([0, 0])

    screen.fill(colour)
    screen.blit(ghost, ghostrect)
    screen.blit(fire, firerect)
    screen.blit(heart, [570, 15])
    screen.blit(heart, [550, 15])
    screen.blit(heart, [530, 15])
    pygame.display.flip()