#Exercise 4
import random
n_test = 10
dic = {
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
}
for i in range(0,n_test):
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = x + y
    for x in dic :
        t = x == z
        if t == True:
            dic[z] += 1          
for x,y in dic.items():
    print(x,y)
for y in dic:
    p = (dic[y])/n_test
    print(p)
