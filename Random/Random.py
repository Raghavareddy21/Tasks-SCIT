import numpy as numpy 
import matplotlib.pyplot as plt
List=numpy.random.normal(loc=0,scale=1,size=1000)
plot=plt.hist(List,10,density=True)
plt.grid(axis='x',alpha=1)
plt.grid(axis='y',alpha=1)

plt.show()