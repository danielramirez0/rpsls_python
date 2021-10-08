from player import Player
from validation import Validator

class Human(Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        print('Select your gesture')
        i = 1
        for gesture in self.gestures:
            print(f'{i}: {gesture.name}')
            i += 1
    