class Player:

    def __init__(self):
        self.score = 0

    def get_input(self, current_round_score, rolls_so_far, max_score):
        return True

    def add_score(self, score):
        self.score += score


class Score_Stop_Player(Player):

    def __init__(self, round_score_hold):
        super().__init__()
        self.score_hold = round_score_hold

    def get_input(self, current_round_score, rolls_so_far, max_score):
        return current_round_score >= self.score_hold

    def __str__(self):
        return "Score Stop {}".format(self.score_hold)


class Roll_Stop_Player(Player):

    def __init__(self, number_rolls_hold):
        super().__init__()
        self.rolls_hold = number_rolls_hold

    def get_input(self, current_round_score, rolls_so_far, max_score):
        return rolls_so_far >= self.rolls_hold

    def __str__(self):
        return "Roll Stop {}".format(self.rolls_hold)

class Strategic_Player(Score_Stop_Player):

    def get_input(self, current_round_score, rolls_so_far, max_score):
        potential_score = self.score + current_round_score
        if potential_score >= 100:
            return True
        if 100 - potential_score <= 2:
            return False
        return current_round_score >= self.score_hold

    def __str__(self):
        return "Strategic Score Stop {}".format(self.score_hold)