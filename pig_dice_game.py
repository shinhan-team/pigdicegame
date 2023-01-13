from random import randint


class Player:

    def __init__(self):
        self.now_score = 0
        self.total_score = 0

    def roll(self):
        dice_number = randint(1,6)
        if dice_number == 1:
            return
        else:
            self.now_score += dice_number

class Com:

    def __init__(self):
        self.now_score = 0
        self.total_score = 0
