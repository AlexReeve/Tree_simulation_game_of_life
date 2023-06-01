### run this code in a console
import matplotlib.pyplot as plt
import numpy as np

with np.load("tree_simulation.npz") as f:
    cells = f["state"]
    print(cells)


from matplotlib.colors import ListedColormap
# Set up the initial figure and axes
f,ax=plt.subplots(constrained_layout=True)
ax.axis("off")
cmap=ListedColormap(["white","green","red"])
array_plot=ax.imshow(cells[0],
                     vmin=cells.min(), vmax=cells.max(), animated=True, cmap = cmap)


def animate(i): 
    array_plot.set_array(cells[i])
    return[array_plot]
    
from matplotlib.animation import FuncAnimation 
from IPython.display import HTML 
anim = FuncAnimation(f, animate, frames = len(cells) , interval = 100)
HTML(anim.to_jshtml())