import pygame
from life import Life

pygame.init()
screen = pygame.display.set_mode((200, 200))

board = Life(5, 5)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        board.event_handler(event)

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
