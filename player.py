class Player:
    def __init__(self, name, gestures):
        self.name = name
        self.gestures = gestures
    
    def select_gesture(self):
        for gesture in self.gestures:
            #TODO
            print(f"{gesture}")
