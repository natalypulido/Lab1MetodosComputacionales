#Nataly Pulido Fernandez 201216338
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

archivo = np.loadtxt("datos_CAMINATA.txt")
#print archivo 

fila1 = archivo[1,:]
#print fila1
 
plt.hist(fila1, bins=60, normed = True)
plt.savefig("bonomial.png")
plt.close()

#crear lista suma de c/u
lista1 = []
for i in archivo:
    new = np.sum(i)
    lista1.append(new)
#print lista1

plt.hist(lista1, bins=60, normed = True)
s, m = norm.fit(lista1)
x = np.linspace(3300, 3700, 100)
y = norm.pdf(x, s, m)
plt.plot(x,y)
plt.savefig("normal.png")

#media todas
print s

#Miu(1000)=mediatodas
M=1000
N = 10

p = s/(N*M)
print ("La probabilidad de sacar una cara con esta moneda es :", p)
