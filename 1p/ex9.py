# Exercice 9

from math import sqrt
from math import pi
from math import exp
def gauss_function(x):
    return (1/sqrt(2*pi))*exp(-0.5*((x)**2))
    
for x in range(-5,6,1):
    z=gauss_function(x)
    print(z)