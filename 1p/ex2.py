# Exercice 2

x = input("Length in meter(s): ")
cm = float(x)*100
inch = cm / 2.54
feet = inch/12
yard = feet/3
BritMile = yard/1760
print(str(x) + " meters correpond to : " +"\n"
      + str(round(inch,2)) + " inch(es), " +"\n"
      + str(round(feet,2)) + " foot (feet), "+"\n"
      + str(round(yard,2)) + " yard(s) " +"\n"
      + str(round(BritMile,4)) + " mile(s) ")

print("Welcome ! We will transform meters into inches, feets, yards and miles with this little programm")
meters=float(input("First, how many meters you want to transform ?"))
cm=meters*100
ans1=round(cm/2.54,2)
ans2=round(ans1/12,2)
ans3=round(ans2/3,2)
ans4=round(ans3/1760,4)
print("So "+ str(meters) + " meters are equivalent to "+ str(ans1) + " inches,"+
str(ans2)+" feets," + str(ans3)+" yards," + str(ans4)+" British Miles.")



