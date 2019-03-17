
import numpy as np
import matplotlib.pyplot as plt

filename = "gauge.dat"
eta = np.genfromtxt(filename, delimiter =",", dtype = str)

h = 1/300
t = 0
hi = []
for i in range(0,len(eta)):
    t += h
    hi.append(t)

plt.scatter(hi, eta, s = 0.5)
plt.autoscale(enable=True, axis='both')
plt.title("Time vs Eta")
plt.xlabel("Time")
plt.ylabel("Eta")
plt.tick_params(axis='y', which='Major', labelsize=1)
plt.show()
plt.savefig("Time_Eta.png")

vi = []
ai = []
for i in range(0,(len(eta)-2)):
    v0 = str((float(eta[i+2])-2*float(eta[i+1])+float(eta[i])/(2*h)))
    a0 = str((float(eta[i+2])-2*float(eta[i+1])+float(eta[i])/(h**2)))
    vi.append(v0)
    ai.append(a0)


plt.plot(hi[0:-2],eta[0:-2], hi[0:-2], vi, hi[0:-2], ai)
plt.show() 
plt.savefig('3axes.png')







    


    
