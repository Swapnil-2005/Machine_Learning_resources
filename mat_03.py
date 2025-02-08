import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Basic straight line graph
x = [0,1, 2, 3]
y = [0,2, 4, 6]
# add line 

#resize graph
plt.figure(figsize=(5,3),dpi=100)

#add 2nd line 

x2 = np.arange(0, 4.5, 0.5)  # Corrected np.arange with start=0, stop=4, step=0.5
plt.plot(x2, x2**2, label="x^2", color="blue", linestyle="-")  # Added label and style for x^2 line



plt.title("Straight Line", fontdict={"fontname": "Arial", "fontsize": 30})  # Corrected fontdict
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y,label="2x",color="red",linewidth=5,marker=".",markersize=30,markeredgecolor="green",linestyle="--") #coloring our graph

# to show only integer values in x axis and y axis use plt.x/yticks([])
plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6])

plt.legend() # to add label i.e to identify

plt.show() # to display the graph in screen
