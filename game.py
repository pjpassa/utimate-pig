import random


class Game:

    def __init__(self, player):
        self.player = player

    def turn(self):
        round_score = 0
        number_of_rolls = 0
        while True:
            current_roll = self.roll()
            number_of_rolls += 1
            if current_roll == 1:
                round_score = 0
                break
            round_score += current_roll
            hold = self.player.get_input(round_score, number_of_rolls)
            if hold:
                break
        return round_score

    def roll(self):
        return random.randint(1, 6)

    def run(self):
        for _ in range(7):
            self.player.add_score(self.turn())
        return self.report

    @property
    def report(self):
        return self.player.score
