from player import Player
from ai import AI

class Game:
    def __init__(self):
        self.display_welcome()
        self.display_rules()
        self.run_game()
        self.ai = True
        self.rounds = int


    def run_game(self):

        self.display_winner()
    def display_welcome(self):
        print('Welcome to Rock Paper Scissor Lizard Spock!')

    def display_winner(self):
        pass

    def display_rules(self):
        print('The game RPSLS is just like Rock Paper Scissors, however there are now five options to choose from!\nRules:\nRock beats Scissor and Lizard\nPaper beats Rock and Spock\nScissor beats Paper and Lizard\nLizard beats Spock and Paper\nSpock beats Scissors and Rock')

    def get_mode(self):
        ai_on_off = input('Please select you game mode:\n1: Play versus an AI\n2: Play against a friend')
        if ai_on_off == 2:
            self.ai = False

    def round_count(self):
        return input('How many rounds would you like to play?')

