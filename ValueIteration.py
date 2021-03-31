import copy


class ValueIteration:

    def __init__(self, grid):
        self.grid = grid

    def runValueIteration(self):
        for i in range(0, self.grid.K):
            previous_grid = copy.deepcopy(self.grid)
            for j in range(0, len(self.grid.gridStates)):
                for idx, state in enumerate(self.grid.gridStates[j]):
                    if not state.boulder and not state.terminal:
                        state.policy[0][0] = self._get_upwards_reward_(previous_grid.gridStates[j][idx], previous_grid)
                        state.policy[1][0] = self._get_downwards_reward_(previous_grid.gridStates[j][idx], previous_grid)
        return self.grid

    def _get_upwards_reward_(self, previous_state, previous_grid):
        if previous_state.Y == 0:
            reward = (1-self.grid.noise)*previous_state.get_max()
        else:
            reward = (1-self.grid.noise)*(previous_grid.gridStates[previous_state.Y-1][previous_state.X].get_max())
            print reward
        return reward

    def _get_downwards_reward_(self, previous_state, previous_grid):
        if previous_state.Y == self.grid.vertical - 1:
            reward = (1-self.grid.noise)*previous_state.get_max()
            print reward
        else:
            reward = (1-self.grid.noise)*(previous_grid.gridStates[previous_state.Y+1][previous_state.X].get_max())
            print reward
        return reward
