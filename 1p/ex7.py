# Exercice 7




s = input("Give me a list of numbers and I will add them all (separate by a space) : ")

list_numbers = map(int, s.split())
sum=0
for i in list_numbers:
    sum=sum + i 
print(sum)
