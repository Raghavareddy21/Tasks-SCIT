import numpy as numpy 
import csv
import matplotlib.pyplot as plt
List=numpy.random.poisson(25,1000)
plot=plt.hist(List,10,density=True)
plt.grid(axis='x',alpha=1)
plt.grid(axis='y',alpha=1)
plt.show()
with open('points.csv', 'w') as csvfile:
	fieldnames=['points']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in List:
		writer.writerow({'points': i})

