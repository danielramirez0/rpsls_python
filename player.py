from gesture import Gesture

class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = [
            Gesture('rock', ['scissors', 'lizard'], ['paper', 'spock']), 
            Gesture('paper', ['rock', 'spock'], ['scissors', 'lizard']), 
            Gesture('scissors', ['paper', 'lizard'], ['rock', 'spock']), 
            Gesture('lizard', ['paper', 'spock'], ['scissors', 'rock']), 
            Gesture('spock', ['scissors', 'rock'], ['lizard', 'paper']), 
            ]
    