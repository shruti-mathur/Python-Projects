import pygame


pygame.init()

red = (255,150,100)
black = (0,0,0)

screen = pygame.display.set_mode((900,600))
screen.fill(red)

while True:
    # Draw object - Rectangle

    for event in pygame.event.get():

        # Print Event
        if event.type ==pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.rect(screen, black, [20, 20, 50, 50])

    # Drawing Circle
    pygame.draw.circle(screen, black, [150, 150], 50)

    pygame.display.update()