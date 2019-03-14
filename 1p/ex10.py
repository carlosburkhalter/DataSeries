# Exercice 10 

numbers = list(range(10))
print(numbers)



for n in range(0,len(numbers)):
    i = int(len(numbers)/2)
    numbers.pop(i)
    print(numbers)
    
print(numbers)
    


