# rubiks-cube-RL
COGS 182 Final Project

Implementing RL methods to solve a 2x2 Rubik's Cube

states file taken from: https://tim.id.au/limejuice/generating-the-full-list-of-valid-states-of-a-2x2-rubiks-cube/ 

## Instructions for running

**CUBE** The 2x2 Rubik's Cube is implemented in the Cube class in cube2x2.py. It initializes a cube with a current_s (state), terminal_s (terminal state), and valid_states, which is the list of string representation of the state space. Methods include shuffle_state, which shuffles to a random state, and step, which takes in an action and changes the current_s to the next state. Note that this function does not explicitly return the next state.

All Sarsa(0) and n-step Sarsa code is contained in Jupyter notebooks and can be run there, parameters such as number of episodes, alpha, epsilon, gamma can all be tweaked.

Initializing Q values is in the Q_init notebook, which updates Q values by following paths startin from the goal state.

**all Q values are in Q.zip file** This is because the raw files were too large to upload to github
