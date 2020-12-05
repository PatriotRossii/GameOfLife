import pygame
from board import Board

pygame.init()
screen = pygame.display.set_mode((500, 500))

board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        board.event_handler(event)

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
