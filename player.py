import pygame.draw
from .constants import *


class Player:
    BORDER = 2
    PADDING = 10

    def __init__(self, color):
        self.pos = 0
        self.row = 6
        self.col = 0
        self.color = color
        self.direction = 'N'
        self.x = 75
        self.y = 700

    def draw_player(self, win):
        radius = RECTANGLE_WIDTH//4 - self.PADDING
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        if 0 <= self.pos <= 5:
            self.direction = 'N'
        elif 11 >= self.pos >= 6:
            self.direction = 'E'
        elif 17 >= self.pos >= 12:
            self.direction = 'S'
        elif 23 >= self.pos >= 18:
            self.direction = 'W'
        self.col = col
        self.row = row
        self.cal_pos()

    def cal_pos(self):
        if self.direction == 'N':
            self.y = 100 + (self.row*RECTANGLE_WIDTH)
            self.x = 75
        elif self.direction == 'E':
            self.x = 100 + (self.col * RECTANGLE_WIDTH)
            self.y = 100
        elif self.direction == 'S':
            self.y = 100 + (self.row*RECTANGLE_WIDTH)
            self.x = 725
        elif self.direction == 'W':
            self.x = 100 + (self.col * RECTANGLE_WIDTH)
            self.y = 700

    def __repr__(self):
        return str(self.color)


