import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Basic straight line graph
x = [0,1, 2, 3]
y = [0,2, 4, 6]

plt.title("Straight Line", fontdict={"fontname": "Arial", "fontsize": 30})  # Corrected fontdict
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y)

# to show only integer values in x axis and y axis use plt.x/yticks([])
plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6])

plt.show() # to display the graph in screen
