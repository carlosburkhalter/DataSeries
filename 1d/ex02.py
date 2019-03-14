#Exercice 2

import random

print("Enter the number of simulation :")

x = int(input())

head = 0
for coin in range(0,x):
    r = random.random()
    if r <= 0.5:
        print("Head")
        head += 1
    else :
        print("Tail")
    
print("Number of 'Head' : " + str(head))
