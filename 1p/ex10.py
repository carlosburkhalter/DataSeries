# Exercice 10 



"""
numbers = range(10)                            
>>> print numbers                              
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for n in numbers:                          
i = len(numbers)/2                         
del numbers[i]                                 
print (’n=%d, del %d’ % (n,i), numbers)        
n=0, del 5 [0, 1, 2, 3, 4, 6, 7, 8, 9]
n=1, del 4 [0, 1, 2, 3, 6, 7, 8, 9]
n=2, del 4 [0, 1, 2, 3, 7, 8, 9]
n=3, del 3 [0, 1, 2, 7, 8, 9]
n=8, del 3 [0, 1, 2, 8, 9]
"""

# create a list from 0 to 9
# print the list
# take the length of numbers(= 10) and divide by 2 => =5
# del numbers[5]
# print list numbers without the [5] (= 5)
# take the length of numbers without the 5 => = 9 and divide by 2 => = 4.5
# take the integer = 4
# del numbers[4]
# print list numbers without the [5] (= 5) and the [4] (=4). 
# it continues like this (taking each time the integer). -> be carefull with this function because of the integer. 

