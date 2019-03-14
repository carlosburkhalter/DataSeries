# Exercice 5
"""
The first problem that appears is that delta can take negative values. Meaning that when we try to compute the square root of a negative value we obtain an error. So the program should be constructed with a if/else strcuture allowing to stop the program whether the discriminant is negative. And if delta is not negative the program can continue normally.

The second problem is on the last line. Print should not be written in this way when we want to output results.The correct way is:

print(str(x1),str(x2))
"""

a = -2; b = 5; c = 4
from math import sqrt
q = b*b - 4*a*c
if q<0:
    print("No solution")
else :
    q = sqrt(q)
    x1 = str((-b + q)/(2*a))
    x2 = str((-b - q)/(2*a))
print("x1 = " + x1+", x2 = "+x2)   

