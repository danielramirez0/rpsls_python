from player import Player
from validation import number_between
from prompt import prompt_input


class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def select_gesture(self):
        print(f'{self.name}, select your gesture')
        i = 1
        for gesture in self.gestures:
            print(f'{i}: {gesture.name}')
            i += 1
        selection = int(prompt_input("", number_between, 1, 5, secret=True)) - 1
        return self.gestures[selection]
