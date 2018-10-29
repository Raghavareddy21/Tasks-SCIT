import numpy as numpy
import random 
from Poisson import List as L1
from Random import List as L2
import matplotlib.pyplot as plt
List1=[]
List2=[]
for i in range(100):
	List1.append(random.choice(L1))
	List2.append(random.choice(L2))
List3 = numpy.array([List1,List2])
List3=numpy.average(List3, axis=0)
plot=plt.hist(List3,10,density=True)
plt.grid(axis='x',alpha=1)
plt.grid(axis='y',alpha=1)
plt.show()
