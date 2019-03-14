# Exercice 15

c = ""
A = "A"+"B"+"C"+"D"+"E"+"F"+"G"+"H"+"I"+"J"+"K"+"L"+"M"+"N"+"O"+"P"+"Q"+"R"+"S"+"T"+"U"+"V"+"W"+"X"+"Y"+"Z"
a = A.lower()
d = A+a
print(A+a)
for i in range(0,len(A)):
    c += A[i]+a[i]
print(c)

for i in range(0,len(d),10):
    t = "|"+ c[i:i+10] +"|"
    t = " ".join(t)
    print(t)
    

print(list(a))