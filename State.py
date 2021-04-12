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

    def getPolicy(self, noise):

        max = self.get_max()
        retVal = None

        #if the max is 0, check if any other are also 0, if they are choose one randomly 
        if max == 0:
            values = []
            for v in self.policy:
                if v[0] == 0:
                    values.append(v)

            retVal = random.choice(values)
        else:
            for v in self.policy:
                if v[0] == max:
                    retVal = v


        doUnexpectedMove = False
        unexpectedMove2 = False
        #Test if we take an unexpected move
        if random.random() < noise:
            doUnexpectedMove = True
            if random.random() <= .5:
                #of the two remaining options, which one do we take (50/50)
                unexpectedMove2 = True

        if(retVal[1] == '↑'):
            if doUnexpectedMove:
                if unexpectedMove2:
                    return self.policy[2]    #right
                else:
                    return self.policy[3]   #left
            else:
                return retVal

        elif(retVal[1] == '↓'):
            if doUnexpectedMove:
                if unexpectedMove2:
                    return self.policy[2]    #right
                else:
                    return self.policy[3]   #left
            else:
                return retVal

        elif(retVal[1] == '→'):
            if doUnexpectedMove:
                if unexpectedMove2:
                    return self.policy[0]    #up
                else:
                    return self.policy[1]   #down
            else:
                return retVal

        elif(retVal[1] == '←'):
            if doUnexpectedMove:
                if unexpectedMove2:
                    return self.policy[0]    #up
                else:
                    return self.policy[1]   #down
            else:
                return retVal

        return retVal

            


















