# Exercice 4
#a
# 1 import pi, carré mal fait, variable commence par un chiffre


from math import sin, cos, pi
x = pi/4
val = sin(x)**2 + cos(x)**2
print (val)
if val == float(1) :
    print("Yes, it is equal to 1")
    
#b


v0 = 3 #m/s
t = 1 #s

a = 2*v0**2
s = v0*t + 1/2*(a*t**2)
print (s)

