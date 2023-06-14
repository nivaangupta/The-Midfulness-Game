import pygame
from .constants import *
from .questiondata import QuestionBrain
from .options import Options


class ScoreBoard:

    def __init__(self, color):
        self.score = 0
        self.points_list = []
        self.messages = [MESSAGE1, MESSAGE2, MESSAGE3]
        self.color = color
        self.option1 = None
        self.option2 = None
        self.option3 = None

    def update_on_scoreboard(self, win):
        pygame.draw.rect(win, self.color, (800, 0, 400, 400))
        pygame.font.init()
        textfont = pygame.font.SysFont('monospace', 30)
        textfont1 = pygame.font.SysFont('monospace', 15)
        textTBD1 = textfont.render(f"MINDFULNESS: {self.score}%", 1, BLACK)
        textTBD2 = textfont.render(f"GOAL       : 100%", 1, BLACK)
        textTBD3 = textfont1.render(f'{WELCOME_MESSAGE}', 1, BLACK)
        textTBD4 = textfont1.render(f'{RED_MESSAGE}', 1, BLACK)
        textTBD5 = textfont1.render(f'{GREEN_MESSAGE}', 1, BLACK)
        textTBD6 = textfont1.render(f'{BLUE_MESSAGE}', 1, BLACK)
        textTBD7 = textfont1.render(f'{CONST_MESSAGE}', 1, BLACK)
        textTBD8 = textfont1.render(f'{CONST_MESSAGE_}', 1, BLACK)
        win.blit(textTBD1, (850, 100))
        win.blit(textTBD2, (850, 130))
        win.blit(textTBD3, (850, 200))
        win.blit(textTBD4, (850, 230))
        win.blit(textTBD5, (850, 260))
        win.blit(textTBD6, (850, 290))
        win.blit(textTBD7, (820, 350))
        win.blit(textTBD8, (820, 370))

    def scoreboard_question_update(self, win, brain, player):
        pygame.draw.rect(win, BOARD_COLOR, (800, 400, 400, 400))
        brain.ask_question(player.pos)
        pygame.font.init()
        textfont1 = pygame.font.SysFont('monospace', 15)
        list_of_question_string = brain.question_to_be_asked.split()
        y_cord = 420
        text = ''
        for word in list_of_question_string:
            if list_of_question_string.index(word) % 6 == 0 and list_of_question_string.index(word) != 0:
                question_tbd = textfont1.render(f'{text}', 1, BLACK)
                win.blit(question_tbd, (820, y_cord))
                y_cord += 30
                text = ''
                text += f' {word}'
            else:
                text += f' {word}'
        question_tbd = textfont1.render(f'{text}', 1, BLACK)
        win.blit(question_tbd, (820, y_cord))
        i = 0
        self.option1 = Options(i+1, brain.options_to_be_displayed[i])
        self.option1.draw(win)
        i += 1
        self.option2 = Options(i + 1, brain.options_to_be_displayed[i])
        self.option2.draw(win)
        i += 1
        self.option3 = Options(i + 1, brain.options_to_be_displayed[i])
        self.option3.draw(win)
        self.points_list = brain.points_to_be_given
        pygame.display.update()

    def calc_points(self, option_chosen, win):
        pygame.font.init()
        textfont1 = pygame.font.SysFont('monospace', 15)
        points_to_be_added = self.points_list[option_chosen]
        self.score += points_to_be_added
        pygame.draw.rect(win, BOARD_COLOR, (800, 400, 400, 400))
        if points_to_be_added == 10:
            index = 0
        elif points_to_be_added == 0:
            index = 1
        else:
            index = 2
        if self.score >= 100:
            self.out_of_rat_race(win)
        else:
            list_of_message_string = self.messages[index].split()
            text = ''
            y_cord = 420
            for word in list_of_message_string:
                if list_of_message_string.index(word) % 6 == 0 and list_of_message_string.index(word) != 0:
                    message_tbd = textfont1.render(f'{text}', 1, BLACK)
                    win.blit(message_tbd, (820, y_cord))
                    y_cord += 30
                    text = ''
                    text += f' {word}'
                else:
                    text += f' {word}'
            question_tbd = textfont1.render(f'{text}', 1, BLACK)
            win.blit(question_tbd, (820, y_cord))

    def out_of_rat_race(self, win):
        pygame.draw.rect(win, BOARD_COLOR, (800, 400, 400, 400))
        pygame.font.init()
        textfont1 = pygame.font.SysFont('monospace', 20)
        list_of_words = VICTORY_MESSAGE.split()
        text = ''
        y_cord = 420
        for word in list_of_words:
            if list_of_words.index(word) % 4 == 0 and list_of_words.index(word) != 0:
                vic_masseage = textfont1.render(f'{text}', 1, BLACK)
                win.blit(vic_masseage, (820, y_cord))
                y_cord += 30
                text = ''
                text += f' {word}'
            else:
                text += f' {word}'
        vic_masseage = textfont1.render(f'{text}', 1, BLACK)
        win.blit(vic_masseage, (820, y_cord))



