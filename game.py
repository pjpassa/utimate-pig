import random
from player import Player, Roll_Stop_Player, Score_Stop_Player


class Game:

    def __init__(self, players):
        self.players = players
        self.solitaire = type(players) != type(list())
        self.winner = ""

    @property
    def max_score(self):
        if self.solitaire:
            return self.players.score
        return max([player.score for player in self.players])

    def turn(self, player):
        round_score = 0
        number_of_rolls = 0
        while True:
            current_roll = self.roll()
            number_of_rolls += 1
            if current_roll == 1:
                round_score = 0
                break
            round_score += current_roll
            hold = player.get_input(round_score, number_of_rolls, self.max_score)
            if hold:
                break
        return round_score

    def roll(self):
        return random.randint(1, 6)

    def run(self):
        if self.solitaire:
            for _ in range(7):
                self.players.add_score(self.turn(self.players))
            return self.report
        while True:
            for index, player in enumerate(self.players):
                player.add_score(self.turn(player))
                if player.score >= 100:
                    self.winner = str(player)
                    break
            if self.winner:
                break
        return self.report

    @property
    def report(self):
        if self.solitaire:
            return self.players.score
        return self.winner