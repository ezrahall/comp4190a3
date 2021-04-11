import random


class QValueLearning:
	
	def __init__(self, grid):

		self.grid = grid

	def runQValueLearning(self):

		startState = self.grid.robotStartState
		reward = 0

		for i in range(0, 3500):#self.grid.episodes):

			currentState = self.grid.gridStates[startState[0]][startState[1]]
			alive = True
			reward = 0

			while alive:

				#choose the next state to go to 
				policy = currentState.getPolicy(self.grid.noise)
				#reward -= self.grid.transactionCost

				#'↑' '↓' '→' '←' 
				if policy[1] == '*':
					alive = False
					reward = policy[0]

				elif policy[1] == '↑':
					#check if we can move here
					if currentState.Y < self.grid.vertical - 1:
						if not self.grid.gridStates[currentState.Y + 1][currentState.X].boulder:
							#reward = 0

							#update policy:
							currentState.policy[0][0] = ((1-self.grid.alpha) * currentState.policy[0][0]) + (self.grid.alpha * (reward + (self.grid.discount * self.grid.gridStates[currentState.Y + 1][currentState.X].get_max())))
							currentState = self.grid.gridStates[currentState.Y + 1][currentState.X]
				
				elif policy[1] == '↓':
					#check if we can move here
					if currentState.Y > 0:
						if not self.grid.gridStates[currentState.Y - 1][currentState.X].boulder:
							#reward = 0

							#update policy:
							currentState.policy[1][0] = ((1-self.grid.alpha) * currentState.policy[1][0]) + (self.grid.alpha * (reward + (self.grid.discount * self.grid.gridStates[currentState.Y - 1][currentState.X].get_max())))
							currentState = self.grid.gridStates[currentState.Y - 1][currentState.X]
			
				elif policy[1] == '→':
					#check if we can move here
					if currentState.X < self.grid.horizontal - 1:
						if not self.grid.gridStates[currentState.Y][currentState.X + 1].boulder:
							#reward = 0

							#update policy:
							currentState.policy[2][0] = ((1-self.grid.alpha) * currentState.policy[2][0]) + (self.grid.alpha * (reward + (self.grid.discount * self.grid.gridStates[currentState.Y][currentState.X + 1].get_max())))
							currentState = self.grid.gridStates[currentState.Y][currentState.X + 1]
				
				elif policy[1] == '←':
					#check if we can move here
					if currentState.X > 0:
						if not self.grid.gridStates[currentState.Y][currentState.X - 1].boulder:
							#reward = 0

							#update policy:
							currentState.policy[3][0] = ((1-self.grid.alpha) * currentState.policy[3][0]) + (self.grid.alpha * (reward + (self.grid.discount * self.grid.gridStates[currentState.Y][currentState.X - 1].get_max())))
							currentState = self.grid.gridStates[currentState.Y][currentState.X - 1]
			

		return self.grid


	def update(self):
		pass

	def getValue(self):
		pass

	def getQValue(self):
		pass



