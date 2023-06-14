import pygame
from .constants import *


class Options:

    def __init__(self, option_no, text=''):
        self.color = OPTION_COLOR
        self.x = 820
        if option_no == 1:
            self.y = 550
        elif option_no == 2:
            self.y = 640
        elif option_no == 3:
            self.y = 730
        self.width = 350
        self.height = 40
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width+10, self.height+30))
        if self.text != '':
            font = pygame.font.SysFont('monospace', 15)
            list_of_strings = self.text.split()
            y_cord = self.y + 10
            text = ''
            for word in list_of_strings:
                if list_of_strings.index(word) % 4 == 0 and list_of_strings.index(word) != 0:
                    text_tbd = font.render(f'{text}', 1, BLACK)
                    win.blit(text_tbd, (self.x+10, y_cord))
                    y_cord += 20
                    text = ''
                    text += f' {word}'
                else:
                    text += f' {word}'
            text_tbd = font.render(f'{text}', 1, BLACK)
            win.blit(text_tbd, (self.x + 10, y_cord))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

