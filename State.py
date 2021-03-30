# coding=utf-8
class State:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.policy = [[0.0, '↑'], [0.0, '↓'], [0.0, '→'], [0.0, '←']]

    def set_policy(self, newPolicy):
        self.policy = newPolicy
