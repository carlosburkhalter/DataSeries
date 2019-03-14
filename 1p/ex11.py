
# Exercice 11

import numpy as np

data = np.genfromtxt('density_air.dat')
data2= np.genfromtxt('density_water.dat')

print(data); print(data2)

x=data[:,0]
print(str(x))
y=data[:,1]
print(str(y))
x2=data2[:,0]
print(str(x))
y2=data2[:,1]
print(str(y))
"""
%matplotlib inline 
%config InlineBackend.figure_format= 'svg'
"""

import numpy as np
import matplotlib.pyplot as plt 
plt.scatter(x,y, s=10)
plt.xlabel("Temperature")
plt.ylabel("Air density")
plt.show()
plt.scatter(x2,y2, s=10)
plt.xlabel("Temperature")
plt.ylabel("Water density")