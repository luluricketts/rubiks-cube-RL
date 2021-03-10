import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import colors 

def visualize_cube(state_str):
    """
    Function to visualize rubik's cube
    parameter: 
        state_str - string representation of sate as it exists in valid_states
    """

    maps = {'W':1, 'G':2, 'R':3, 'O':4, 'B':5, 'Y':6}

    viz = np.zeros((6,8))
    cube = [maps[i] for i in state_str]

    viz[:2,2:4] = np.array(cube[:4]).reshape(2,2)
    viz[2:4,:] = np.array(cube[4:20]).reshape(2,8)
    viz[4:,2:4] = np.array(cube[20:]).reshape(2,2)

    cmap = colors.ListedColormap(['black', 'white', 'green', 'red', 'orange', 'blue', 'yellow'])
    bounds = np.arange(-.5, 7, 1)
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(viz, cmap=cmap, norm=norm)
    plt.vlines(x=np.arange(0.5, 7, 1), ymin=-.5, ymax=5.5)
    plt.hlines(y=np.arange(0.5, 5, 1), xmin=-.5, xmax=7.5)
    plt.xticks([])
    plt.yticks([])
    plt.show()