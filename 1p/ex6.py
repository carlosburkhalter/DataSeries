# Exercice 6

# Celsius to Fahrenheit

def C(F) :
    C = F
    F = (9/5)*C +32
    print(str(C) + " degrees Celsius = "+ str(F) +" degrees Fahrenheit")
    C1 = (5/9) * (F-32)
    if C1 == C:
        print("Boolean test : true")
C(50)    
