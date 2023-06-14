import pygame
import requests
from themindfulnessgame.constants import *
from themindfulnessgame.board import Board
from themindfulnessgame.player import Player
from themindfulnessgame.scoreboard import ScoreBoard
from themindfulnessgame.questiondata import QuestionBrain

FPS = 60        # GLOBAL VARIABLE for game simulation
WIN = pygame.display.set_mode((WIDTH, HEIGHT))      # GLOBAL VARIABLES for game design
pygame.display.set_caption('THE MINDFULNESS GAME')
DATA = requests.get("https://api.npoint.io/ee001056f289895ebb05").json()


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    score = ScoreBoard(SCOREBOARD_COLOR)
    player1 = Player(PLAYER_BLUE)
    brain = QuestionBrain(DATA)
    pygame.draw.rect(WIN, BOARD_COLOR, (800, 400, 400, 400))
    roll_enable = True

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if board.button_rect.collidepoint(pos):
                    board.role_dice(WIN, player1, score, brain, roll_enable)
                    roll_enable = False
                if score.option1.is_over(pos):
                    option_no = 0
                    score.calc_points(option_no, WIN)
                    roll_enable = True
                if score.option2.is_over(pos):
                    option_no = 1
                    score.calc_points(option_no, WIN)
                    roll_enable = True
                if score.option3.is_over(pos):
                    option_no = 2
                    score.calc_points(option_no, WIN)
                    roll_enable = True

        board.draw(WIN, player1)
        score.update_on_scoreboard(WIN)
        pygame.display.update()

    pygame.quit()


main()


