# Exercise 3
#1
import random
thrown = 200
number_6 = 0
for dice in range(0,thrown):
    x = random.randint(1,6)
    if x == 6 :
        number_6 += 1
        print(x)
print(number_6)
proba = str(float((number_6/thrown)*100))
print("Probability of getting a 6: " + proba + "%")
