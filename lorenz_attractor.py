import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import fftpack

#Condiciones iniciales (sigma, rho, beta)
s=10.0
r=28.0
b=8.0/3.0
t=4.0
h=0.01
mi= 0.0
ma= 4.0
##Cantidad de puntos
n=int((ma-mi)/h)
#print n

#coor=([1, 1, 1])
x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)
t = np.zeros(n)


def mi_funcion1(x, y, z, t):
    dx = s * (y - x)
    return dx
def mi_funcion2(x, y, z, t):
    dy = x * (r - z) - y
    return dy
def mi_funcion3(x, y, z):
    dz = x * y - b * z
    return dz

x[0]=1
y[0]=1
z[0]=1
t[0]=1

##Euler
for i in range (1, n):
    t[i]=t[i-1] + h
    x[i]=x[i-1] + h * mi_funcion1(x[i-1],y[i-1], z[i-1])
    y[i]=y[i-1] + h * mi_funcion2(x[i-1],y[i-1], z[i-1])
    z[i]=z[i-1] + h * mi_funcion3(x[i-1],y[i-1], z[i-1])



