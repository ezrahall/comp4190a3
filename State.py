import random
# coding=utf-8
class State:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.policy = [[0.0, '↑'], [0.0, '↓'], [0.0, '→'], [0.0, '←']]
        self.terminal = False
        self.boulder = False

    def set_policy(self, newPolicy):
        self.policy = newPolicy

    def set_terminal(self, terminal):
        self.terminal = terminal

    def set_boulder(self, boulder):
        self.boulder = boulder

    def get_max(self):
        max = -10
        for i in self.policy:
            if i[0] > max:
                max = i[0]
        return max

    def getPolicy(self):

        #no uncertanty yet
        max = self.get_max()
        if max == 0:
            values = []
            for v in self.policy:
                if v[0] == 0:
                    values.append(v)

            return random.choice(values)

        for v in self.policy:
            if v[0] == max:
                return v

