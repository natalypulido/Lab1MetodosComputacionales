import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import fftpack
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.mlab as mlab

#Importing image data into Numpy arrays
datos=[]
imagen =plt.imread('moonlanding.png')
#print imagen
datos.append(imagen)
#print datos
#plt.imshow(imagen)
#plt.show()


##Tomar las transformada
fourier = np.fft.fft2(imagen)
#print fourier
normaliza = abs(fourier)
#print normaliza
EP=normaliza**2
#print EP
img=plt.imshow(EP, cmap=cm.Blues)
power_cut = 95.0
clipped_power = mlab.prctile(power.flatten(), power_cut)
img.set_clim(0, clipped_power)
plt.show()

#Hacer igual cero frec
camfrec = fourier.copy()
#Primeras y ultimas 
camfrec[:,50:-50] = 0
tam1 = np.shape(camfrec)
cam=np.fft.ifft2(camfrec)
norm=abs(cam)
img=plt.imshow(cam)
power_cut = 95.0
clipped_power = mlab.prctile(power.flatten(), power_cut)
img.set_clim(0, clipped_power)
