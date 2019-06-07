import pygame

pygame.init()

red = (255,150,100)
black = (0,0,0)

screen = pygame.display.set_mode((900,600))

screen.fill(red)

while True:
    # Drawing Object - Rectangle
    pygame.draw.rect(screen, black, [20, 20, 50, 50])

    # Drawing Circle
    pygame.draw.circle(screen, black, [150, 150], 50)

    pygame.display.update()