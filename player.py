class Player:

    def __init__(self):
        self.score = 0

    def get_input(self, current_round_score, rolls_so_far):
        return True


class Score_Stop_Player(Player):

    def __init__(self, round_score_hold):
        super(Score_Stop_Player, self).__init__()
        self.round_hold = round_score_hold

    def get_input(self, current_round_score, rolls_so_far):
        return current_round_score >= self.round_hold


class Roll_Stop_Player(Player):

    def __init__(self, number_rolls_hold):
        super(Roll_Stop_Player, self).__init__()
        self.rolls_hold = number_rolls_hold

    def get_input(self, current_round_score, rolls_so_far):
        return rolls_so_far >= self.rolls_hold