#run this code in console
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


with np.load("tree_simulation.npz") as f:
    cells = f["state"]
    
print("Trees,Fires, Fire Chance")
time = 0
for x in range(len(cells)):
    state = cells[x]
    trees = 0
    fires = 0
    for i in range(len(state)):
            for j in range(len(state[i])):
                
                if state[i,j] == 1:
                    trees = trees + 1
                if state[i,j] == 2:
                    fires = fires +1
    time = time + 1        
    print(f"{trees/100},{fires/100},5")
    
#I took these printed numbers and inserted them into a text file to create my dataset, named tree_data.txt
    
######################
#creating figures

data=pd.read_csv("C:/Users/yq19555/Desktop/tree_data.txt")

graph = data.plot(title = "Percentage Distribution of Cells Per Timestep",
       xlabel = "Timestep",

       ylabel = "Amount of cells\n(%)")

fig = graph.get_figure()

fig.savefig("steady_state_graph")

##################################
