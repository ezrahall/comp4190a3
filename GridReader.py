from State import State


def _get_boulder_states_(inputStates):
    result = []
    values = inputStates.split('Boulder=')[1]
    values = values.split('=')
    values.pop(0)
    for i in values:
        i = i.split('{')
        i = i[1].split('}')[0]
        i = i.split(',')
        result.append([int(i[1]), int(i[0])])
    return result


class GridReader:

    def __init__(self, filename):
        file = open(filename, "r")
        gridString = file.read()
        file.close()
        lines = gridString.split("\r\n")
        self.horizontal = int(lines[0].split('=')[1])
        self.vertical = int(lines[1].split('=')[1])
        self.gridStates = []
        self._init_grid()
        self.terminal = self._get_terminal_states_(lines[2])
        self.boulder = _get_boulder_states_(lines[3])
        self.robotStartState = lines[4]
        self.K = lines[5]
        self.episodes = lines[6]
        self.discount = lines[7]
        self.noise = lines[8]
        self.transactionCost = lines[9]

    def _get_terminal_states_(self, inputStates):
        result = []
        values = inputStates.split('Terminal=')[1]
        values = values.split('=')
        values.pop(0)
        for i in values:
            i = i.split('{')
            i = i[1].split('}')[0]
            i = i.split(',')
            result.append([int(i[1]), int(i[0]), int(i[2])])
            self.gridStates[int(i[1])][int(i[0])].set_policy([[int(i[2]), '*']])
        return result

    def _init_grid(self):
        for i in range(0, self.vertical):
            row = []
            for j in range(0, self.horizontal):
                row.append(State(j, i))
            self.gridStates.append(row)

    def get_policies_(self):
        result = []
        for i in range(0, len(self.gridStates)):
            row = []
            for j in self.gridStates[i]:
                row.append(j.policy)
            result.append(row)
        return result
