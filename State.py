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
        max = 0
        for i in self.policy:
            if i[0] > max:
                max = i[0]
        return max
