import numpy as np 

class Cube:

    def __init__(self):
        
        self.valid_states = np.loadtxt('2x2states.txt', dtype=str)
        self.terminal_s = len(self.valid_states) - 1 # terminal state
        self.current_s = None # current state
        self.current_r = 0 # current reward 
    
    def shuffle_state(self):
        """
        Shuffles cube to a random state and sets reward sum to 0 to signify new episode start

        returns: random starting state (integer)
        """
        self.current_s = np.random.randint(len(self.valid_states) - 1)
        self.current_r = 0

    def rotate(self, str_list, ind_list, clockwise):
        """
        Rotates rotates the indeces in the string representation of the state
        
        parameters
        -----------
        str_list: list representation of the state's string representation
        ind_list: 3x4 list where each sublist is the list of indeces to rotate
        clockwise: boolean, direction to rotate given indeces
        
        returns
        --------
        str_list: new list representation with rotated indeces
        """
        if clockwise:
            for inds in ind_list:
                l = str_list[inds[-1]]
                for i in range(3, 0, -1):
                    str_list[inds[i]] = str_list[inds[i-1]]
                str_list[inds[0]] = l
        else:
            for inds in ind_list:
                l = str_list[inds[0]]
                for i in range(3):
                    str_list[inds[i]] = str_list[inds[i+1]]
                str_list[inds[-1]] = l
                
        return str_list

    def step(self, state, action):
        """
        Given a state and action, executes that action and returns the new state and reward
        
        parameters
        -----------
        state: integer representation of current state (index of string representation in valid_states)
        action: integer representation of action to take
            action indeces: [0/F, 1/F', 2/U, 3/U', 4/R, 5/R', 6/B, 7/B', 8/D, 9/D', 10/L, 11/L']
            
        returns
        -------
        state_new: integer representation of next state
        reward
        """
        
        state_str = self.valid_states[state]
        
        if action in [0,1,6,7]:
            inds = [[5,3,16,20],[13,2,8,21],[6,7,15,14]]
            clockwise = True if action in [0,7] else False
        elif action in [2,3,8,9]:
            inds = [[0,1,3,2],[6,4,10,8],[7,5,11,9]]
            clockwise = True if action in [2,9] else False
        elif action in [4,5,10,11]:
            inds = [[8,9,17,16],[7,1,18,21],[15,3,10,23]]
            clockwise = True if action in [4,10] else False
        
        str_list = rotate(list(state_str), inds, clockwise=clockwise)
        new_str = ''.join([i for i in str_list])
        state_new = np.where(self.valid_states == new_str)[0][0]
        
        self.current_s = state_new
        self.current_r -= 1