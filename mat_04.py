import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data for the bar chart
x = ['A', 'B', 'C']  # Fixed the typo in the list
y = [1, 4, 2]

# Create a bar chart
bars=plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("Grade",fontsize=10)
plt.ylabel("Grade",fontsize=10)

# desingning each pattern 
patterns=["/","o","*"]
for bar in bars:
    bar.set_hatch(patterns.pop(0)) #The pop(0) function handles iterating over patterns (removes and returns the first pattern on each call).
    

# Display the chart
plt.show()
