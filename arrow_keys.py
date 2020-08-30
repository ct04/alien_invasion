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
still = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if not ghostrect.top <= 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ghostrect.move_ip(up)
        if not ghostrect.bottom >= height:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ghostrect.move_ip(down)
        if not ghostrect.left <= 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ghostrect.move_ip(left)
        if not ghostrect.right >= width:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ghostrect.move_ip(right)
    firerect.move_ip([random.randint(-300, 300), random.randint(-200, 200)])

    # EVENT1 = firerect.move_ip([random.randint(0, 600), random.randint(0, 400)])
    #
    # pygame.time.set_timer(EVENT1, 1000)







    screen.fill(colour)
    screen.blit(ghost, ghostrect)
    screen.blit(fire, firerect)
    screen.blit(heart, [570, 15])
    screen.blit(heart, [550, 15])
    screen.blit(heart, [530, 15])
    pygame.display.flip()