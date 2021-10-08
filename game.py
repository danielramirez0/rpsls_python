from player import Player
from ai import AI
from validation import Validator

class Game:
    def __init__(self):
        self.ai = True
        self.rounds = int
        self.validator = Validator()
        self.prompt = self.validator.prompt_input
        self.winner = str
        self.player_one_score = 0
        self.player_two_score = 0

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.get_mode()
        self.round_count()
        self.start()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Rock Paper Scissor Lizard Spock!')

    def display_winner(self):
        pass

    def display_rules(self):
        print('The game RPSLS is just like Rock Paper Scissors, however there are now five options to choose from!\nRules:\nRock beats Scissor and Lizard\nPaper beats Rock and Spock\nScissor beats Paper and Lizard\nLizard beats Spock and Paper\nSpock beats Scissors and Rock')

    def get_mode(self):
        ai_on_off = self.prompt('Please select you game mode:\n1: Play versus an AI\n2: Play against a friend', self.validator.number_between, 1 , 2)
        if ai_on_off == 2:
            self.ai = False

    def round_count(self):
        self.rounds = self.prompt('How many rounds would you like to play?', self.validator.is_odd)

    def start(self):
        player_one = Player(self.prompt('Player 1, enter your name: ', self.validator.auto_valid))
        if self.ai == True:
            player_two = AI()
        else:
            player_two = Player('Player 2, enter your name: ', self.validator.auto_valid))
        