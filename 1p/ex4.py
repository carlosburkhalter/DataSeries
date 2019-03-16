# Exercice 4
#a

# 1 : import pi
# 2 : correction in the square (replace "^" by " ** ")
# 3 : assigment can not begin by a number (1_val)
# 4 : add a  sentence if it is equal to 1

from math import sin, cos, pi
x = pi/4
val = sin(x)**2 + cos(x)**2
print (val)
if val == float(1) :
    print("Yes, it is equal to 1")
    
#b
#1 : correct v0 and t (unit not written)
#2 : following point #1 : correction of a
#3 : add parenthesis to s

v0 = 3 #m/s
t = 1 #s

a = 2*v0**2
s = v0*t + 1/2*(a*t**2)
print (s)

