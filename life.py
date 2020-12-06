import pygame

from board import Board


class Life(Board):
    def __init__(self, width, height, debug=False):
        super().__init__(width, height)
        self.debug = debug

        self.started = False

        self.to_retrospective = []
        self.my_event_type = pygame.USEREVENT + 1
        self.speed = 1000

    def next_color(self, x, y):
        super().next_color(x, y)
        self.to_retrospective.append((x, y))

    def timer_exceed_event(self):
        self.next_move()

    def clicked_event(self, button, x, y):
        pos = self.get_pos(x, y)

        if self.debug:
            self.debug_print(pos)

        if button == 1 and not self.started:
            if pos is not None:
                self.next_color(*pos)
        elif button == 3:
            self.started = True
            pygame.time.set_timer(self.my_event_type, self.speed)

    def pressed_event(self, key):
        if key == pygame.K_SPACE:
            self.started = not self.started
            if not self.started:
                pygame.time.set_timer(self.my_event_type, 0)
            else:
                pygame.time.set_timer(self.my_event_type, self.speed)

    def scroll_event_up(self):
        self.speed = max(10, self.speed - 10)
        if self.started:
            pygame.time.set_timer(self.my_event_type, self.speed)

    def scroll_event_down(self):
        self.speed = self.speed + 10
        if self.started:
            pygame.time.set_timer(self.my_event_type, self.speed)

    def next_move(self):
        to_change = []
        buffer = []

        for ch_el in self.to_retrospective:
            x, y = ch_el
            around = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    cur_x = x + dx
                    cur_y = y + dy
                    if 0 <= cur_x < self.width and 0 <= cur_y < self.height:
                        around += self.board[cur_y][cur_x]

            if self.board[y][x] == 0:
                if around == 3:
                    buffer.append((x, y))
                    to_change.append((y, x, 1))
            elif self.board[y][x] == 1:
                if around != 2 and around != 3:
                    buffer.append((x, y))
                    to_change.append((y, x, 0))

        for e in to_change:
            self.board[e[0]][e[1]] = e[2]
        self.to_retrospective = buffer