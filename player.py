class Player:

    def __init__(self, round_score_hold):
        self.score = 0
        self.hold = round_score_hold

    def get_input(self, current_round_score):
        return current_round_score >= self.hold

