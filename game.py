from human import Human
from ai import AI
from prompt import prompt_input
import validation as validator


class Game:
    def __init__(self):
        self.use_ai = True
        self.rounds = int
        self.winner = str
        self.player1 = object
        self.player2 = object

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
        print(f'{self.winner} wins the set!!!')

    def display_rules(self):
        print('The game RPSLS is just like Rock Paper Scissors, however there are now five options to choose from!\nRules:\nRock beats Scissor and Lizard\nPaper beats Rock and Spock\nScissor beats Paper and Lizard\nLizard beats Spock and Paper\nSpock beats Scissors and Rock')

    def get_mode(self):
        msg = 'Please select you game mode:\n1: Play versus an AI\n2: Play against a friend\n'
        game_mode = prompt_input(msg, validator.number_between, 1, 2)
        if game_mode == "2":
            self.use_ai = False

    def round_count(self):
        self.rounds = int(prompt_input(
            'How many rounds would you like to play?\n', validator.is_odd))

    def start(self):
        self.player1 = Human(prompt_input(
            'Player 1, enter your name: ', validator.auto_valid))
        if self.use_ai == True:
            self.player2 = AI("BOT")
        else:
            self.player2 = Human(prompt_input(
                'Player 2, enter your name: ', validator.auto_valid))

        while True:
            player1_gesture = self.player1.select_gesture()
            player2_gesture = self.player2.select_gesture()
            print(f"{self.player1.name} chose {player1_gesture.name}")
            print(f'{self.player2.name} chose {player2_gesture.name}')
            if player1_gesture.name == player2_gesture.name:
                print('Tie!')
            elif player1_gesture.name in player2_gesture.weaknesses:
                print(f'{self.player1.name} wins this round')
                self.player1.increase_score()
            elif player1_gesture.name in player2_gesture.strengths:
                print(f'{self.player2.name} wins this round')
                self.player2.increase_score()
            if self.player1.score / self.rounds > .5:
                self.winner = self.player1.name
                break
            elif self.player2.score / self.rounds > .5:
                self.winner = self.player2.name
                break
