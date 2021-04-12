# coding=utf-8
from Grid import Grid
from ValueIteration import ValueIteration
from QValueLearning import QValueLearning
import tkinter as tk


def main():
    '''
    window = tk.Tk()
    window2 = tk.Tk()

    #Grid for Value iteration
    valueIterationGrid = Grid('gridConf.txt')

    #Grid for Q-learning
    qLearningGrid = Grid('gridConf.txt')

    valueIteration = ValueIteration(valueIterationGrid)
    valueIterationGrid = valueIteration.runValueIteration()

    qValueLearning = QValueLearning(qLearningGrid)
    qLearningGrid = qValueLearning.runQValueLearning()

    VIGridPolicies = valueIterationGrid.get_policies_()
    QLGPolicies = qLearningGrid.get_policies_()


    terminal_states_VI = valueIterationGrid.terminal
    terminal_states_QL = qLearningGrid.terminal

    boulder_states_VI = valueIterationGrid.boulder
    boulder_states_QL = qLearningGrid.boulder

    draw_board(window, VIGridPolicies, [row[:-1] for row in terminal_states_VI], boulder_states_VI,
               max_reward(terminal_states_VI), max_punishment(terminal_states_VI), valueIterationGrid.K, 'value-iteration')

    draw_board(window2, QLGPolicies, [row[:-1] for row in terminal_states_QL], boulder_states_QL,
               max_reward(terminal_states_QL), max_punishment(terminal_states_QL), qLearningGrid.episodes, 'q-learning')

    window.mainloop()
    window2.mainloop()
    '''
    #read in results file
    results = open("results.txt","r")
    questions = []
    for line in results:
        line = line.replace("\n","")
        line = line.replace("\r","")
        questions.append(line.split(","))

    windows = []
    for q in questions:
        window = tk.Tk()
        grid = Grid('gridConf.txt')

        if(q[3] == "MDP"):
            valueIteration = ValueIteration(grid)
            grid = valueIteration.runValueIteration()
        elif(q[3] == "RL"):
            qValueLearning = QValueLearning(grid)
            grid = qValueLearning.runQValueLearning()

        gridPolicies = grid.get_policies_()
        terminal_states = grid.terminal
        boulder_states = grid.boulder

        answer = ""

        if(q[4] == "stateValue"):
            answer = grid.gridStates[int(q[1])][int(q[0])].get_max()
        elif(q[4] == "bestPolicy"):
            answer = grid.gridStates[int(q[1])][int(q[0])].getPolicy(0.0)[1]
        elif(q[4] == "bestQValue" and q[3] == "RL"):
            answer = grid.gridStates[int(q[1])][int(q[0])].getPolicy(0.0)[0]

        index = questions.index(q) + 1
        answer = "Question " + str(index) + ": " + ",".join(q) + ": " + str(answer)

        if(q[3] == "MDP"):
            draw_board(window, gridPolicies, [row[:-1] for row in terminal_states], boulder_states,
                max_reward(terminal_states), max_punishment(terminal_states), q[2], 'value-iteration', answer)
        elif(q[3] == "RL"):
            draw_board(window, gridPolicies, [row[:-1] for row in terminal_states], boulder_states,
               max_reward(terminal_states), max_punishment(terminal_states),  q[2], 'q-learning', answer)

        windows.append(window)

    for window in windows:
        window.mainloop()


def max_reward(terminal_states):
    max_reward = float('-inf')

    for state in terminal_states:
        if state[2] > max_reward:
            max_reward = state[2]

    return max_reward
        

def max_punishment(terminal_states):
    max_punishment = float('inf')

    for state in terminal_states:
        if state[2] < max_punishment:
            max_punishment = state[2]

    return max_punishment


def draw_board(window, grid, terminal, boulders, max_reward, max_punishment, iterations, learningType, answer):

    canvas_width = 1000  # Width of the window
    canvas_height = 600  # Length of the window

    edge_dist = 10  # Distance of the board to the edge of the window
    bottom_space = 100  # Distance from the bottom of the board to the bottom of the window
    small_rect_diff = 5  # For terminal states, distance from outside rectangle to inside rectangle

    rows = len(grid)  # Number of rows in the grid
    cols = len(grid[0])  # Number of columns in the grid

    edge_dist_triangle = 5  # Distance from tip of the triangle to the edge of the rectangle
    triangle_height = int(0.1 * min(((canvas_width - 2 * edge_dist) / cols), ((canvas_height - edge_dist - bottom_space) / rows)))  # Height of the triangles
    triangle_width = 2 * triangle_height  # Width of the triangles

    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, background='black')  # Create a black background

    for row in range(rows - 1, -1, -1):  # Loop through the rows of the grid
        for col in range(cols):  # Loop through the columns of the grid
            #print(row, col)
            if [row, col] not in boulders:  # If it's not a boulder state
                x1 = edge_dist + col * ((canvas_width - 2 * edge_dist) / cols)  # Top left x coordinate of the rectangle
                y1 = edge_dist + (rows - row - 1) * ((canvas_height - edge_dist - bottom_space) / rows)  # Top left y coordinate of the rectangle
                #print(x1, y1)
                x2 = x1 + ((canvas_width - 2 * edge_dist) / cols)  # Bottom right x coordinate of the rectangle
                y2 = y1 + ((canvas_height - edge_dist - bottom_space) / rows)  # Bottom right y coordinate of the rectangle

                best_move = get_best_move(grid[row][col])  # Get the index of the maximum q-value for this cell
                best_value = grid[row][col][best_move][0]  # Get the best q-value for this cell
                best_direction = grid[row][col][best_move][1]  # Get the best direction out of this cell

                if best_value >= 0:  # Best value is positive, so draw the rectangle in green
                    canvas.create_rectangle(x1, y1, x2, y2, outline='white',
                                            fill='#%02x%02x%02x' % (0, int(200 * min(best_value / max_reward, max_reward)), 0))  # Draw the rectangle of this cell
                else:  # Best value is negative, so draw the rectangle in red
                    canvas.create_rectangle(x1, y1, x2, y2, outline='white',
                                            fill='#%02x%02x%02x' % (int(200 * min(best_value / max_punishment, -1 * max_punishment)), 0, 0))  # Draw the rectangle of this cell

                canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(round(best_value, 2)),
                                   font=('TkDefaultFont', int(0.25 * ((canvas_width - 2 * edge_dist) / cols))), fill='white')  # Print the best value in the middle of the cell

                if [row, col] in terminal:  # If this cell is a terminal state
                    #print("TERMINAL: ", row, col)
                    x1 = x1 + small_rect_diff
                    y1 = y1 + small_rect_diff
                    x2 = x2 - small_rect_diff
                    y2 = y2 - small_rect_diff
                    canvas.create_rectangle(x1, y1, x2, y2, outline='white')  # Draw a smaller rectangle inside
                else:  # Not a terminal state, so draw an arrow in the direction of the highest q-value
                    if best_direction == '↑':  # Draw an up arrow
                        mid = (x1 + x2) / 2
                        top = y1 + edge_dist_triangle
                        triange_points = [mid, top, mid - triangle_width / 2, top + triangle_height, mid + triangle_width / 2, top + triangle_height]
                        canvas.create_polygon(triange_points, fill='white')
                    elif best_direction == '↓':  # Draw a down arrow
                        mid = (x1 + x2) / 2
                        top = y2 - edge_dist_triangle
                        triange_points = [mid, top, mid - triangle_width / 2, top - triangle_height,
                                          mid + triangle_width / 2, top - triangle_height]
                        canvas.create_polygon(triange_points, fill='white')
                    elif best_direction == '←':  # Draw a left arrow
                        mid = (y1 + y2) / 2
                        top = x1 + edge_dist_triangle
                        triange_points = [top, mid, top + triangle_height, mid - triangle_width / 2,
                                          top + triangle_height, mid + triangle_width / 2]
                        canvas.create_polygon(triange_points, fill='white')
                    elif best_direction == '→':  # Draw a right arrow
                        mid = (y1 + y2) / 2
                        top = x2 - edge_dist_triangle
                        triange_points = [top, mid, top - triangle_height, mid - triangle_width / 2,
                                          top - triangle_height, mid + triangle_width / 2]
                        canvas.create_polygon(triange_points, fill='white')

            else:  # This is a boulder state
                x1 = edge_dist + col * ((canvas_width - 2 * edge_dist) / cols)
                y1 = edge_dist + (rows - row - 1) * ((canvas_height - edge_dist - bottom_space) / rows)
                x2 = x1 + ((canvas_width - 2 * edge_dist) / cols)
                y2 = y1 + ((canvas_height - edge_dist - bottom_space) / rows)
                canvas.create_rectangle(x1, y1, x2, y2, fill='grey', outline='white')

    if(learningType == 'value-iteration'):
        canvas.create_text(int(canvas_width / 2), (canvas_height - bottom_space / 2) - 10, font=('TkDefaultFont', int(bottom_space / 4)),
                        text=('Values after ' + str(iterations) + ' iterations (Value Iteration)'), fill='white')  # Write text at the bottom of the canvas

    elif(learningType == 'q-learning'):
        canvas.create_text(int(canvas_width / 2), (canvas_height - bottom_space / 2) - 10, font=('TkDefaultFont', int(bottom_space / 4)),
                        text=('Values after ' + str(iterations) + ' episodes (Q-Learning)'), fill='white')  # Write text at the bottom of the canvas

    canvas.create_text(int(canvas_width / 2), canvas_height - bottom_space / 5, font=('TkDefaultFont', int(bottom_space / 6)),
                    text=(answer), fill='white')  # Write text at the bottom of the canvas
    print(answer)

    canvas.pack()


def get_best_move(state):
    max_value = float('-inf')
    max_index = -1

    for move in range(len(state)):
        if state[move][0] > max_value:
            max_index = move
            max_value = state[move][0]
    return max_index


main()