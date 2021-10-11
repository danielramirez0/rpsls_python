from gesture import Gesture

class Player:
    def __init__(self):
        self.gestures = [
            Gesture('rock', ['scissors', 'lizard'], ['paper', 'spock']), 
            Gesture('paper', ['rock', 'spock'], ['scissors', 'lizard']), 
            Gesture('scissors', ['paper', 'lizard'], ['rock', 'spock']), 
            Gesture('lizard', ['paper', 'spock'], ['scissors', 'rock']), 
            Gesture('spock', ['scissors', 'rock'], ['lizard', 'paper']), 
            ]
        self.score = 0

    def increase_score(self):
        self.score += 1

