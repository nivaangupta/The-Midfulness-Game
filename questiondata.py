from .constants import *


class QuestionBrain:

    def __init__(self, data):
        self.question_data = data
        self.no_of_questions_red = len(data['red'])
        self.no_of_questions_green = len(data['green'])
        self.no_of_questions_blue = len(data['blue'])
        self.red_question = [item['Question'] for item in data['red']]
        self.green_question = [item['Question'] for item in data['green']]
        self.blue_question = [item['Question'] for item in data['blue']]
        self.red_options = [item['Options'] for item in data['red']]
        self.blue_options = [item['Options'] for item in data['blue']]
        self.green_options = [item['Options'] for item in data['green']]
        self.green_points = [item['Points'] for item in data['green']]
        self.blue_points = [item['Points'] for item in data['blue']]
        self.red_points = [item['Points'] for item in data['red']]
        self.question_to_be_asked = None
        self.options_to_be_displayed = None
        self.points_to_be_given = None
        self.red_questions_asked = 0
        self.green_questions_asked = 0
        self.blue_questions_asked = 0

    def ask_question(self, pos):
        if pos in RED_BLOCKS_POS:
            if self.red_questions_asked >= self.no_of_questions_red:
                self.red_questions_asked = self.red_questions_asked - self.no_of_questions_red
            self.question_to_be_asked = self.red_question[self.red_questions_asked]
            self.options_to_be_displayed = self.red_options[self.red_questions_asked]
            self.points_to_be_given = self.red_points[self.red_questions_asked]
            self.red_questions_asked += 1
        elif pos in GREEN_BLOCKS_POS:
            if self.green_questions_asked >= self.no_of_questions_green:
                self.green_questions_asked = self.green_questions_asked - self.no_of_questions_green
            self.question_to_be_asked = self.green_question[self.green_questions_asked]
            self.options_to_be_displayed = self.green_options[self.green_questions_asked]
            self.points_to_be_given = self.green_points[self.green_questions_asked]
            self.green_questions_asked += 1
        elif pos in BLUE_BLOCKS_POS:
            if self.blue_questions_asked >= self.no_of_questions_blue:
                self.blue_questions_asked -= self.no_of_questions_blue
            self.question_to_be_asked = self.blue_question[self.blue_questions_asked]
            self.options_to_be_displayed = self.blue_options[self.blue_questions_asked]
            self.points_to_be_given = self.blue_points[self.blue_questions_asked]
            self.blue_questions_asked += 1

