import random
from player import Player


class Game:

    def __init__(self, player):
        self.player = player

    def turn(self):
        round_score = 0
        while True:
            current_roll = self.roll()
            if current_roll == 1:
                round_score = 0
                break
            round_score += current_roll
            hold = self.player.get_input(round_score)
            if hold:
                break
        return round_score


    def roll(self):
        return random.randint(1, 6)

    def run(self):
        for _ in range(7):
            self.player.add_score(self.turn())

    @property
    def report(self):
        return self.player.score
