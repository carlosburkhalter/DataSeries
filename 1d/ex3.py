
#Exercise 3

print("We will compute your money growth!")
A=float(input("First, what is the amount of money you want to invest? "))
p=float(input("Please, insert the interest rate in percent"))
n=float(input("Finally, how many years you want to leave the money?"))
ans=round(A*(1+(p/100))**n,2)
print("You will have "+ str(ans) + " swiss francs")

#Exercice 3

p = 5
A = 1000
n = 3

result = A*(((1+(p/100))**n))

print("Result : CHF "+ str(round(result,2)))
