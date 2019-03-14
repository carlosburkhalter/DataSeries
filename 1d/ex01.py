# Exercise 1

from math import sqrt
import random

in_circle = 0
in_square = 1000
for i in range(0,in_square):
    x=random.random()
    y=random.random()
    if x**2+y**2<=1:
        in_circle+=1
pi=4*in_circle/in_square

print (float(pi))
