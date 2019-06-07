import pygame

pygame.init()

red = (255,150,100)
black = (0,0,0)

screen = pygame.display.set_mode((900,600))

rect_x = 0
rect_y = 0

clock = pygame.time.Clock()
FPS = 50

while True:
    for event in pygame.event.get():
        # Print event
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(red)
    pygame.draw.rect(screen, black, [rect_x, rect_y, 50, 50])

    rect_x += 5
    rect_y += 5
    pygame.display.update()
    clock.tick(FPS)