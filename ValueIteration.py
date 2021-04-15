import copy

'''
ValueIteration.py

Class file for the Value Iteration algorithm

'''
class ValueIteration:

    def __init__(self, grid):
        self.grid = grid

    # Run Value iteration
    def runValueIteration(self):
        # Iterate through the number of iteration specified in the input
        for i in range(0, self.grid.K):
            previous_grid = copy.deepcopy(self.grid)
            # Update All States
            for j in range(0, len(self.grid.gridStates)):
                for idx, state in enumerate(self.grid.gridStates[j]):
                    # If it is a updateable state update the values for all moves
                    if not state.boulder and not state.terminal:
                        state.policy[0][0] = self._get_upwards_move_(previous_grid.gridStates[j][idx], previous_grid)
                        state.policy[1][0] = self._get_downwards_move_(previous_grid.gridStates[j][idx], previous_grid)
                        state.policy[2][0] = self._get_right_move_(previous_grid.gridStates[j][idx], previous_grid)
                        state.policy[3][0] = self._get_left_move_(previous_grid.gridStates[j][idx], previous_grid)
        return self.grid

    # Get the value of trying to move up taking into account transaction cost, noise and previous rewards
    def _get_upwards_move_(self, previous_state, previous_grid):
        reward = (1-self.grid.noise)*self._get_upwards_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2) * self._get_right_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2) * self._get_left_reward_(previous_state, previous_grid)
        reward = self.grid.discount*reward - self.grid.transactionCost
        return reward

    # Get the value of trying to move down taking into account transaction cost, noise and previous rewards
    def _get_downwards_move_(self, previous_state, previous_grid):
        reward = (1-self.grid.noise)*self._get_downwards_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2) * self._get_right_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2) * self._get_left_reward_(previous_state, previous_grid)
        reward = self.grid.discount*reward - self.grid.transactionCost
        return reward

    # Get the value of trying to move right taking into account transaction cost, noise and previous rewards
    def _get_right_move_(self, previous_state, previous_grid):
        reward = (1-self.grid.noise)*self._get_right_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2) * self._get_upwards_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2) * self._get_downwards_reward_(previous_state, previous_grid)
        reward = self.grid.discount*reward - self.grid.transactionCost
        return reward

    # Get the value of trying to move left taking into account transaction cost, noise and previous rewards
    def _get_left_move_(self, previous_state, previous_grid):
        reward = (1-self.grid.noise)*self._get_left_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2)*self._get_downwards_reward_(previous_state, previous_grid)
        reward = reward + (self.grid.noise / 2)*self._get_upwards_reward_(previous_state, previous_grid)
        reward = self.grid.discount*reward - self.grid.transactionCost
        return reward

    # Get the reward of the square above from the previous iteration, if it cant make this move keep previous states max
    def _get_upwards_reward_(self, previous_state, previous_grid):
        if previous_state.Y == 0 or previous_grid.gridStates[previous_state.Y-1][previous_state.X].boulder:
            reward = previous_state.get_max()
        else:
            reward = (previous_grid.gridStates[previous_state.Y-1][previous_state.X].get_max())
        return reward

    # Get the reward of the square below from the previous iteration, if it cant make this move keep previous states max
    def _get_downwards_reward_(self, previous_state, previous_grid):
        if previous_state.Y == self.grid.vertical - 1 or previous_grid.gridStates[previous_state.Y+1][previous_state.X].boulder:
            reward = previous_state.get_max()
        else:
            reward = (previous_grid.gridStates[previous_state.Y+1][previous_state.X].get_max())
        return reward

    # Get the reward of the square to the right from the previous iteration, if it cant make this move keep previous states max
    def _get_right_reward_(self, previous_state, previous_grid):
        if previous_state.X == self.grid.horizontal - 1 or previous_grid.gridStates[previous_state.Y][previous_state.X + 1].boulder:
            reward = previous_state.get_max()
        else:
            reward = (previous_grid.gridStates[previous_state.Y][previous_state.X + 1].get_max())
        return reward

    # Get the reward of the square to the left from the previous iteration, if it cant make this move keep previous states max
    def _get_left_reward_(self, previous_state, previous_grid):
        if previous_state.X == 0 or previous_grid.gridStates[previous_state.Y][previous_state.X - 1].boulder:
            reward = previous_state.get_max()
        else:
            reward = (previous_grid.gridStates[previous_state.Y][previous_state.X - 1].get_max())
        return reward
