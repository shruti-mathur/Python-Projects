import pygame
pygame.init()

red = (255,150,100)
black = (0,0,0)

width = 900
height = 600
screen = pygame.display.set_mode((width, height))
rect_x = 0
rect_y = 0

move_x = 0
move_y = 0

clock = pygame.time.Clock()
FPS = 100
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 5
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -5
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 5
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -5
                move_x = 0

    screen.fill(red)
    pygame.draw.rect(screen, black, [rect_x,rect_y, 50, 50])

    rect_x += move_x
    rect_y += move_y

    if rect_x > width:
        rect_x = -50
    elif rect_x < -50:
        rect_x = width
    elif rect_y > height:
        rect_y = -50
    elif rect_y < -50:
        rect_y = height

    pygame.display.update()
    clock.tick(FPS)