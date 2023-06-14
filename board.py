import pygame
from .player import Player
from .constants import *
from random import randint
from .scoreboard import ScoreBoard


class Board:

    def __init__(self):
        self.moves = {'N': {'y': [6, 5, 4, 3, 2, 1, 0]},
                      'E': {'x': [1, 2, 3, 4, 5, 6]},
                      'S': {'y': [1, 2, 3, 4, 5, 6]},
                      'W': {'x': [5, 4, 3, 2, 1]}}
        self.board = []
        self.dice1 = 6
        self.dice2 = 6
        self.dice_list = [DICE1, DICE2, DICE3, DICE4, DICE5, DICE6]
        self.button_rect = ROLL.get_rect()
        self.button_rect.topleft = (285, 400)
        self.create_board_map()
        self.rolling_enabled = True

    def create_board_map(self):
        for y_cord in self.moves['N']['y']:
            coord = (0, y_cord)
            self.board.append(coord)
        for x_cord in self.moves['E']['x']:
            coord = (x_cord, 0)
            self.board.append(coord)
        for y_cord in self.moves['S']['y']:
            coord = (6, y_cord)
            self.board.append(coord)
        for x_cord in self.moves['W']['x']:
            coord = (x_cord, 6)
            self.board.append(coord)

    def draw_rectangles(self, win):

        pygame.draw.rect(win, BOARD_COLOR, (150, 150, 500, 500))

        for row in range(ROWS):
            for col in range(COLS):

                # Colouring BLUE
                if row == 0 or row == 6 and col == 0 or col == 6:
                    pygame.draw.rect(win, BLUE,
                                     (0, 0, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT))
                    pygame.draw.rect(win, BLACK,
                                     (0, 0, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT), 1)
                    pygame.draw.rect(win, BLUE,
                                     (650, 0, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT))
                    pygame.draw.rect(win, BLACK,
                                     (650, 0, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT), 1)
                    pygame.draw.rect(win, BLUE,
                                     (0, 650, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT))
                    pygame.draw.rect(win, BLACK,
                                     (0, 650, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT), 1)
                    pygame.draw.rect(win, BLUE,
                                     (650, 650, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT))
                    pygame.draw.rect(win, BLACK,
                                     (650, 650, RECTANGLE_HEIGHT, RECTANGLE_HEIGHT), 1)
                if col == 3 and row == 0:
                    pygame.draw.rect(win, BLUE,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, 0,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, 0,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT), 1)
                if col == 3 and row == 6:
                    pygame.draw.rect(win, BLUE,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, WIDTH - 400 - RECTANGLE_HEIGHT,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, WIDTH - 400 - RECTANGLE_HEIGHT,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT), 1)
                if row == 3 and col == 0:
                    pygame.draw.rect(win, BLUE,
                                     (col, RECTANGLE_HEIGHT + (row-1)*RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH))
                    pygame.draw.rect(win, BLACK,
                                     (col, RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH), 1)
                if row == 3 and col == 6:
                    pygame.draw.rect(win, BLUE,
                                     (RECTANGLE_HEIGHT + (col-1)*RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH))
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH),1)

                # Colouring RED
                if row == 0 and col == 1 or row == 0 and col == 4:
                    pygame.draw.rect(win, RED,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, 0,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
                                     )
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, 0,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT), 1
                                     )
                if row == 6 and col == 2 or row == 6 and col == 5:
                    pygame.draw.rect(win, RED,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
                                     )
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT), 1
                                     )
                if col == 0 and row == 2 or col == 0 and row == 5:
                    pygame.draw.rect(win, RED,
                                     (col, RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH))
                    pygame.draw.rect(win, BLACK,
                                     (col, RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH), 1)
                if col == 6 and row == 1 or col == 6 and row == 4:
                    pygame.draw.rect(win, RED,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH)
                                     )
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH), 1
                                     )

                # Colouring Green
                if row == 0 and col == 2 or row == 0 and col == 5:
                    pygame.draw.rect(win, GREEN,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, 0,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
                                     )
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH, 0,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT), 1
                                     )
                if row == 6 and col == 1 or row == 6 and col == 4:
                    pygame.draw.rect(win, GREEN,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
                                     )
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_WIDTH, RECTANGLE_HEIGHT), 1
                                     )
                if col == 0 and row == 1 or col == 0 and row == 4:
                    pygame.draw.rect(win, GREEN,
                                     (col, RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH))
                    pygame.draw.rect(win, BLACK,
                                     (col, RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH), 1)
                if col == 6 and row == 2 or col == 6 and row == 5:
                    pygame.draw.rect(win, GREEN,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH)
                                     )
                    pygame.draw.rect(win, BLACK,
                                     (RECTANGLE_HEIGHT + (col - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT + (row - 1) * RECTANGLE_WIDTH,
                                      RECTANGLE_HEIGHT, RECTANGLE_WIDTH), 1
                                     )

    def draw(self, win, player):
        self.draw_rectangles(win)
        self.draw_dice(win)         # THIS NEEDS REPLACEMENT
        win.blit(ROLL, (285, 400))
        player.draw_player(win)

    def draw_dice(self, win):
        image1 = None
        image2 = None
        for i in range(6):
            if self.dice1 == i+1:
                image1 = self.dice_list[i]
            if self.dice2 == i+1:
                image2 = self.dice_list[i]
        win.blit(image1, (400, 300))
        win.blit(image2, (300, 300))

    def role_dice(self, win, player, scoreboard, brain, rolling_enabled):
        if rolling_enabled:
            self.dice1 = randint(1, 6)
            self.dice2 = randint(1, 6)
            self.draw_dice(win)
            player.pos += self.dice1 + self.dice2
            if player.pos >= 24:
                player.pos = player.pos-24
            self.move_player(player)
            player.draw_player(win)
            self.rolling_enabled = False
            scoreboard.scoreboard_question_update(win, brain, player)

    def move_player(self, player):
        position_of_player = self.board[player.pos]
        row = position_of_player[1]
        col = position_of_player[0]
        player.move(row, col)
