import pygame

WIDTH, HEIGHT = 1200, 800
ROWS, COLS = 7, 7
RECTANGLE_WIDTH = 100
RECTANGLE_HEIGHT = 150

BOARD_COLOR = (255, 251, 235)
SCOREBOARD_COLOR = (191, 206, 226)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (170, 86, 86)
GREEN = (171, 194, 112)
BLUE = (181, 213, 197)
PLAYER_RED = (255, 0, 0)
PLAYER_BLUE = (0, 0, 255)
PLAYER_GREEN = (0, 255, 0)
OPTION_COLOR = (227, 132, 255)
HOVER_COLOR = (134, 93, 255)

DICE1 = pygame.transform.scale(pygame.image.load('assets/1.png'), (75, 75))
DICE2 = pygame.transform.scale(pygame.image.load('assets/2.png'), (75, 75))
DICE3 = pygame.transform.scale(pygame.image.load('assets/3.png'), (75, 75))
DICE4 = pygame.transform.scale(pygame.image.load('assets/4.png'), (75, 75))
DICE5 = pygame.transform.scale(pygame.image.load('assets/5.png'), (75, 75))
DICE6 = pygame.transform.scale(pygame.image.load('assets/6.png'), (75, 75))
ROLL = pygame.transform.scale(pygame.image.load('assets/roll.png'), (200, 75))

DATA = {
    'red':
        [
            {
                'Question': "You just lost a running race with your friend Harry in your school's sports day event, what will you do?",
                'Options': ['Train harder to beat harry next year', 'Seek inspiration from harry & get better', 'Fight with harry as he defeated you'],
                'Points': [0, 10, -10]
            },
            {
                'Question': "Your friend scored more marks on a test, later revealing that he cheated on that test to obtain a higher score than you",
                'Options': ['Complain the professor for wrong-doings', 'Never talk to that friend', "Don't compare your scores & move on"],
                'Points': [0, -10, 10]
            },
            {
                'Question': "Your friends dont want to talk to you because you dont drink alcohol and smoke cigarettes",
                'Options': ['Try alcohol & smoking to fit in', 'Accept that they were never your friends', 'Request them to include you inspite'],
                'Points': [0, 10, -10]
            },
        ],
    'green':
        [
            {
                'Question': "You won the quiz despite a lot of your classmates believing that you cant",
                'Options': ['Let them know they were wrong', 'self-affirm that nobody can define your capabilities', 'Sledge your classmates as they were wrong'],
                'Points': [0, 10, -10]
            },
            {
                'Question': "Your exams got cancelled and you have plenty of time to do things that you want, what would you do?",
                'Options': ['Make a routine for slef-development and follow', 'Watch informational documentaries on Netflix', 'Scroll through social media and tiktok'],
                'Points': [10, 0, -10]
            },
            {
                'Question': "You are living in a hotel for a month, what will you prefer having in the breakfast buffet regularly?",
                'Options': ['Chocolate Pancakes with Mapel Syrup', 'Breakfast cereals like cornflakes', 'Oatmeal along with eggs, veggies and fruit'],
                'Points': [-10, 0, 10]
            },
        ],
    'blue':
        [
            {
                'Question': "Do any one of the below activities for 10 minutes for a positive mental health :)",
                'Options': ['Meditate while focusing on a thought', 'practice breath regulation yoga', "Show gratitude towards things you're thankful for"],
                'Points': [10, 10, 10]
            },
            {
                'Question': "Do any one of the below activities for 10 minutes for a positive mental health :)",
                'Options': ['Think of 5 positive things in life', 'Reach out & appreciate a close friend', 'Perform light excercise'],
                'Points': [10, 10, 10]
            },
            {
                'Question': "Do any one of the below activities for 10 minutes for a positive mental health :)",
                'Options': ['Schedule a time for relaxation today', 'Pay attention to present moment & thoughts', 'Eat a healthy meal'],
                'Points': [10, 10, 10]
            },
        ],
}

WELCOME_MESSAGE = "Welcome to the mindfulness game"
RED_MESSAGE = "Red Tile - Negative experience"
GREEN_MESSAGE = "Green Tile - Positive experience"
BLUE_MESSAGE = "Blue Tile - Positive Actions"
CONST_MESSAGE = "please choose an appropriate action"
CONST_MESSAGE_ = "for your mental health below:"

BLUE_BLOCKS_POS = [0, 3, 6, 9, 12, 15, 18, 21]
RED_BLOCKS_POS = [1, 4, 7, 10, 13, 16, 19, 22]
GREEN_BLOCKS_POS = [2, 5, 8, 11, 14, 17, 20, 23]

MESSAGE1 = "Amazing! your mental health is positively affected by your actions :)"
MESSAGE2 = "This action doesn't improve your mental health :|"
MESSAGE3 = "This action affects your mental health negatively :("
VICTORY_MESSAGE = "Congratulations! You are now out of the rat race and have become a Ninja"
