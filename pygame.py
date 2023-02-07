import pygame

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update game state

    # render
    screen.fill((255, 255, 255))
    pygame.display.update()

    # limit frame rate
    clock.tick(60)

# quit pygame
pygame.quit()