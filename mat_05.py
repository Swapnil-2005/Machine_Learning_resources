import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data for the bar chart
x = ['A', 'B', 'C']  # Fixed the typo in the list
y = [1, 4, 2]
c=["red","blue","yellow"]

# Create a bar chart
bars=plt.bar(x, y,width=0.5,color=c,edgecolor="red",linewidth=5) # changing the width

plt.title("Bar Graph")
plt.xlabel("Grade",fontsize=10)
plt.ylabel("student",fontsize=10)

# desingning each pattern 
patterns=["/","o","*"]
for bar in bars:
    bar.set_hatch(patterns.pop(0)) #The pop(0) function handles iterating over patterns (removes and returns the first pattern on each call).
    

# Display the chart
plt.show()