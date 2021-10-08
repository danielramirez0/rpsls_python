from player import Player
from validation import Validator

class Human(Player):
    def __init__(self, name):
        self.name = name
        self.validator = Validator()
        self.prompt = self.validator.prompt_input
        super().__init__()

    def select_gesture(self):
        print('Select your gesture')
        i = 1
        for gesture in self.gestures:
            print(f'{i}: {gesture.name}')
            i += 1
        selection = int(self.prompt("", self.validator.number_between, True, 1, 5)) - 1
        return self.gestures[selection]