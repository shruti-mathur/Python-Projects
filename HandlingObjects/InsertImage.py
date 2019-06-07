import pygame
import random

pygame.init()

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

img_1 = pygame.image.load("Ball.png")

#circle_x = 60
#circle_y = 60

circle_x = random.randint(60,width-60)
circle_y = random.randint(60,height-60)

clock = pygame.time.Clock()
FPS = 50

speed = [2,2]
while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))

    screen.blit(img_1, (circle_x, circle_y))

    circle_x += speed[0]
    circle_y += speed[1]

    if circle_x > width - 200 or circle_x < 0:
        speed[0] = -speed[0]

    elif circle_y > height - 200 or circle_y < 0:
        speed[1] = -speed[1]

    pygame.display.update()
    clock.tick(FPS)