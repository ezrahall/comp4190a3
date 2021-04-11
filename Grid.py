from State import State

def _get_robot_start_state_(inputState):
    values = inputState.split('RobotStartState={')[1].split('}')[0].split(',')
    return [int(values[0]), int(values[1])]


class Grid:

    def __init__(self, filename):
        file = open(filename, "r")
        gridString = file.read()
        file.close()
        lines = gridString.split("\n")
        self.horizontal = int(lines[0].split('=')[1])
        self.vertical = int(lines[1].split('=')[1])
        self.gridStates = []
        self._init_grid()
        self.terminal = self._get_terminal_states_(lines[2])
        self.boulder = self._get_boulder_states_(lines[3])
        self.robotStartState = _get_robot_start_state_(lines[4])
        self.K = int(lines[5].split('=')[1])
        self.episodes = int(lines[6].split('=')[1])
        self.alpha = float(lines[7].split('=')[1])
        self.discount = float(lines[8].split('=')[1])
        self.noise = float(lines[9].split('=')[1])
        self.transactionCost = float(lines[10].split('=')[1])

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
            self.gridStates[int(i[1])][int(i[0])].set_terminal(True)
        return result

    def _get_boulder_states_(self, inputStates):
        result = []
        values = inputStates.split('Boulder=')[1]
        values = values.split('=')
        values.pop(0)
        for i in values:
            i = i.split('{')
            i = i[1].split('}')[0]
            i = i.split(',')
            result.append([int(i[1]), int(i[0])])
            self.gridStates[int(i[1])][int(i[0])].set_boulder(True)
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
