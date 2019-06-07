import pygame
import random

pygame.init()

red = (255,150,100)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
black = (0,0,0)

col_list = [green,blue,yellow,black]
color= random.choice(col_list)

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

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
    screen.fill(red)

    pygame.draw.circle(screen, color, [circle_x, circle_y], 60)

    circle_x += speed[0]
    circle_y += speed[1]

    if circle_x > width - 60 or circle_x < 60:
        speed[0] = -speed[0]
        color = random.choice(col_list)

    elif circle_y > height - 60 or circle_y < 60:
        speed[1] = -speed[1]
        color = random.choice(col_list)

    pygame.display.update()
    clock.tick(FPS)