from axelrod import Player


class Retaliate(Player):
    """
    A player starts by cooperating but will retaliate once the opponent
    has won more than 10 percent times the number of defections the player has.
    """
    retaliation_threshold = 0.1

    def __init__(self):
        Player.__init__(self)
        self.name = (
            'Retaliate (' +
            str(self.retaliation_threshold) + ')')

    def strategy(self, opponent):
        history = zip(self.history, opponent.history)
        if history.count(('C', 'D')) > (
           history.count(('D', 'C')) * self.retaliation_threshold):
            return 'D'
        return 'C'


class Retaliate2(Retaliate):
    retaliation_threshold = 0.08


class Retaliate3(Retaliate):
    retaliation_threshold = 0.12


class LimitedRetaliate(Player):
    """
    A player that co-operates unless the opponent defects and wins.
    It will then retaliate by defecting. It stops when either, it has beaten
    the opponent 10 times more often that it has lost or it reaches the
    retaliation limit (20 defections).
    """
    retaliation_limit = 20
    retaliation_threshold = 0.1
    retaliating = False
    retaliation_count = 0

    def __init__(self):
        Player.__init__(self)
        self.name = (
            'Limited Retaliate (' +
            str(self.retaliation_threshold) +
            '/' + str(self.retaliation_limit) + ')')

    def strategy(self, opponent):
        history = zip(self.history, opponent.history)
        if history.count(('C', 'D')) > (
           history.count(('D', 'C')) * self.retaliation_threshold):
            self.retaliating = True
        else:
            self.retaliating = False
            self.retaliation_count = 0

        if self.retaliating:
            if self.retaliation_count < self.retaliation_limit:
                self.retaliation_count += 1
                return 'D'
            else:
                self.retaliation_count = 0
                self.retaliating = False

        return 'C'

    def reset(self):
        Player.reset(self)
        self.retaliating = False
        self.retaliation_count = 0


class LimitedRetaliate2(LimitedRetaliate):
    retaliation_limit = 25
    retaliation_threshold = 0.1


class LimitedRetaliate3(LimitedRetaliate):
    retaliation_limit = 20
    retaliation_threshold = 0.08
