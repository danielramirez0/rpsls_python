from human import Human
from ai import AI
from prompt import prompt_input
import validation as validator


class Game:
    def __init__(self):
        self.use_ai = True
        self.rounds = int
        self.winner = str
        self.player_one_score = int
        self.player_two_score = int

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
        print(f'{self.winner} won!!!')

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
        player_one = Human(prompt_input(
            'Player 1, enter your name: ', validator.auto_valid))
        if self.use_ai == True:
            player_two = AI("BOT")
        else:
            player_two = Human(prompt_input(
                'Player 2, enter your name: ', validator.auto_valid))

        while True:
            player_one_choice = player_one.select_gesture()
            player_two_choice = player_two.select_gesture()
            print(f"{player_one.name} chose {player_one_choice.name}")
            print(f'{player_two.name} chose {player_two_choice.name}')
            if player_one_choice.name == player_two_choice.name:
                print('Tie!')
            elif player_one_choice.name in player_two_choice.weaknesses:
                print(f'{player_one.name} wins this round')
                self.player_one_score += 1
            elif player_one_choice.name in player_two_choice.strengths:
                print(f'{player_two.name} wins this round')
                self.player_two_score += 1
            if self.player_one_score / self.rounds > .5:
                self.winner = player_one.name
                break
            elif self.player_two_score / self.rounds > .5:
                self.winner = player_two.name
                break
