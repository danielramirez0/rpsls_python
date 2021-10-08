from player import Player
from random import choice


class AI(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def select_gesture(self):
        return choice(self.gestures)
