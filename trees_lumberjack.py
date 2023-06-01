import numpy as np
from numpy.random import default_rng 
rng = default_rng()

def initialise_state(num_steps, size, initial_state):
    '''
    initialises the system, creating the 'blank' arrays to be updated for each iteration of states.
    
    Arguments:
        num_steps (int) : the number of steps the simulation will run for
        size : the size of the array, as - (num_steps, len(intial_array), len(initial_array[0]))
        initial_state (np.ndarray): the starting state of the simulation, as a 2D array.
        
    Returns:
    A 3D array of length num_steps, with the initial state as the first iteration. all other numbers in the array are zero.
                
    
    '''
  # create an array of zeroes ( num_steps, len(initial_array), len(initial_array[0]))
    cells = np.zeros(size, dtype=int)  
    # set initial state as the first item in the array
    cells[0] = initial_state
    return cells

def update_state(previous_array):
    """
    The rules upon the simulation. Takes the initial state, and creates the next state by imposing its rules upon it, and recording the changes to the state these rules make.
    
    Where 0 = empty cell, 1 = tree, 2 = burning tree.
    
    Rule 1: A burning tree in the previous timestep will be an empty cell in the next timestep.
    Rule 2: A tree with at least one burning neighbour(Von Neumann Neighbourhood) will be burning in the next timestep.
    Rule 3: A tree with no burning neighbours starts burning with probability f. Lightning strike.
    Rule 4: A previously empty cell may become a tree with probability p. Tree growth.
    
    Args:
        previous_array (np.ndarray): the 2-dimensional previous state of the system

    Returns:
        new_array (np.ndarray): the 2-dimensional new state of the system
    """
    new_array = np.zeros_like(previous_array)
    
    for i in range(len(previous_array)):
        for j in range(len(previous_array[i])):
            #set positions of trees around tree being inspected
            index_of_tree_to_left = ((i - 1),j)
            index_of_tree_to_right = ((i + 1),j)
            index_of_tree_above = (i,(j-1))
            index_of_tree_below = (i,(j+1))
           
            # set edges of boundry
            # cells over the boundry should be 0, to avoid confusing the simulation
            if index_of_tree_to_left < (0,j):
                tree_to_left = 0
            else:
                tree_to_left = previous_array[index_of_tree_to_left]
            if index_of_tree_above < (i,0):
                tree_above = 0
            else:
                tree_above = previous_array[index_of_tree_above]
            if index_of_tree_to_right > (len(previous_array[i])-1,j):
                tree_to_right = 0
            else:
                tree_to_right = previous_array[index_of_tree_to_right]
            if index_of_tree_below > (i,len(previous_array[i])-1):
                tree_below = 0
            else:
                tree_below = previous_array[index_of_tree_above]            

       
            if previous_array[i,j] == 2:
                new_array[i,j] = 0 # Rule 1 - a burning tree turns into an empty cell
                 
            if previous_array[i,j] == 1:
                x = rng.integers(101)
                z = rng.integers(101)
                if z >= 90 :
                    new_array[i,j] = 0 # rule 5 - random lumberjack
                elif tree_to_left == 2:
                    new_array[i,j] =2 # Rule 2 - a tree starts burning if at least one neighbour is burning
                elif tree_to_right == 2:
                    new_array[i,j] =2
                elif tree_above == 2:
                    new_array[i,j] =2
                elif tree_below == 2:
                    new_array[i,j] =2 
                elif x >= 95 :
                    new_array[i,j] =2 # Rule 3 - a tree may randomly start burning, even with no burning neighbours - lightning strike
                else:
                    new_array[i,j] = 1
                        
            if previous_array[i,j] == 0:
                y = rng.integers(101)
                if y >= 80:
                    new_array[i,j] = 1 # Rule 4 - a empty cell has a chance of growing a tree
                else:
                    new_array[i,j] = 0
            
    return new_array

def run_simulation(num_steps, size, initial_state):
    '''
    
    '''
    state = initialise_state(num_steps, size, initial_state)

    for t in range(1, num_steps):
        state[t] = update_state(state[t-1])

    return state


########### Testing arrays

# a small testing array - 
small_array_with_fire = np.array([[0, 1, 0, 2, 1],
       [2, 2, 1, 2, 1],
       [0, 2, 2, 1, 2],
       [2, 1, 1, 1, 1],
       [1, 2, 2, 1, 2]]) 
#a medium testing array
medium_testing_array = np.array([[1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
       [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
       [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
       [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
       [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
       [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
       [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
       [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
       [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
       [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
       [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
       [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
       [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0]])
#large testing array
large_seeded_array_setup = default_rng(seed=1)
large_seeded_array =large_seeded_array_setup.integers(low = 0, high = 1, size = (100,100), endpoint= True, dtype = int)

#gives a random array
random_array = rng.integers(low = 0, high = 1, size = (100,100), endpoint= True, dtype = int)

#############

#number of steps the simulation should take
number_of_steps = 200

# the starting array/state
initial_state = large_seeded_array

#size 
size = (number_of_steps, len(initial_state), len(initial_state[0]))


#### running, printing and saving
cells = run_simulation(number_of_steps, size , initial_state)

print(cells)

np.savez_compressed("tree_xtra_feature_simulation.npz", state=cells)

