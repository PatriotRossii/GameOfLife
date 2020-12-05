import math

import pygame

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

        self.colors = [(0, 0, 0), (0, 255, 0)]
        self.white = (255, 255, 255)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def draw_styled_rect(self, surface, color, pos, border_width=0, border_color=(255, 255, 255)):
        pygame.draw.rect(surface, color, pos)
        if border_width:
            pygame.draw.rect(surface, border_color, pos, border_width)

    def render(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                x = self.left + j * self.cell_size  # i = (x - self.left) / self.cell_size
                y = self.top + i * self.cell_size   # j = (y - self.top) / self.cell_size

                color = self.colors[self.board[i][j]]
                self.draw_styled_rect(surface, color, (x, y, self.cell_size, self.cell_size), border_width=1)

    def get_pos(self, x, y):
        i = math.ceil((x - self.left) / self.cell_size)
        j = math.ceil((y - self.top) / self.cell_size)

        return (i - 1, j - 1) if 0 < i <= self.width and 0 < j <= self.height else None

    def debug_print(self, pos):
        print(pos)

    def reverse_row_color(self, row):
        for i in range(len(self.board[row])):
            self.reverse_color(i, row)

    def reverse_column_color(self, column):
        for i in range(len(self.board)):
            self.reverse_color(column, i)

    def reverse_color(self, x, y):
        self.board[y][x] = not self.board[y][x]

    def next_color(self, x, y):
        self.board[y][x] = not self.board[y][x]

    def clicked_event(self, x, y):
        pass

    def pressed_event(self, key):
        pass

    def scroll_event_up(self):
        pass

    def scroll_event_down(self):
        pass

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 4:
                self.scroll_event_up()
            if event.button == 5:
                self.scroll_event_down()
            else:
                self.clicked_event(event.button, *event.pos)
        if event.type == pygame.KEYDOWN:
            self.pressed_event(event.key)
        if event.type == pygame.USEREVENT + 1:
            self.timer_exceed_event()