import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# pie chart
x=[10,20,30,40]
y=["c","c++","java","python"]
c=["red","yellow","blue","green"] #customise the colors 
plt.pie(x,labels=y,colors=c,autopct="%0.1f%%",shadow=True,textprops={"fontsize":15})
plt.show()