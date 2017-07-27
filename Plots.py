import numpy as np 
import matplotlib.pyplot as pyplot


mis_datos=genfromtxt("midatos.txt")

x=mis_datos[:,0]
y=mis_datos[:,1]
z=mis_datos[:,2]

plt.plot(x,y)
plt.plot(x,z)
plt.xlabel("x")
plt.ylabel("y")
plt.tittle("Conveccion")
plt.savafig("Conveccion")
plt.close()
