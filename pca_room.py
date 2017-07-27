import numpy as np 
import matplotlib.pyplot as plt 

##Nataly Pulido Fernandez

##Leer archivos 
datos = np.genfromtxt('room-temperature.csv', delimiter= ',')
datos1=np.delete(datos,0,0)
datos=np.delete(datos1,np.s_[0],1)
#print datos

##Plot de temperatura del cuarto 
fig, medidas= plt.subplots(4,1, figsize=(10,10)) 
    
FL=datos[:,0]
#print FL
#plt.plot(FL) 
FR=datos[:,1]
#print FR
#plt.plot(FR)
BL=datos[:,2]
#print BL
#plt.plot(BL)
BR=datos[:,3]
#print BR
#plt.plot(BR)

medidas[0].plot(FL)
medidas[1].plot(FR)
medidas[2].plot(BL)
medidas[3].plot(BR)
#plt.show()
plt.close()
plt.savefig("temp.png")

##Centrar y normalizar datos 

mean_FL=np.mean(FL)
#print mean_FL
std_FL=np.std(FL)


FL_norm=[]
for i in range (len(FL)):
	a=((FL[i]-mean_FL)/std_FL)
	FL_norm.append(a) 
        #print FL_norm

mean_FR=np.mean(FR)
#print mean_FR
std_FR=np.std(FR)


FR_norm=[]
for i in range (len(FR)):
	b=((FR[i]-mean_FR)/std_FR)
	FR_norm.append(b) 
        #print FR_norm

mean_BL=np.mean(BL)
#print mean_BL
std_BL=np.std(BL)


BL_norm=[]
for i in range (len(BL)):
	c=((BL[i]-mean_BL)/std_BL)
	BL_norm.append(c) 
        #print BL_norm

mean_BR=np.mean(BR)
#print mean_BR
std_BR=np.std(BR)


BR_norm=[]
for i in range (len(BR)):
	d=((BR[i]-mean_BR)/std_BR)
	BR_norm.append(d) 
        #print BR_norm

##Matriz total
matriz_tot=[]
matriz_tot.append(FL_norm)
matriz_tot.append(FR_norm)
matriz_tot.append(BL_norm)
matriz_tot.append(BR_norm)

#print matriz_tot

##Matriz de covarianza 
matriz_cov=np.cov(matriz_tot)
print matriz_cov

##Dos componentes principales del problema 
values, vectors=np.linalg.eig(matriz_cov)
#print "values", values
#print "vectors\n", vectors 

print "La primera componente principal es", vectors[0], "con valor", values[0]
print "La segunda componente principal es", vectors[1], "con valor", values[1]

#Contribucion a la varianza 
VAR1=(values[0]/(sum(values)))*100
#print VAR1
VAR2=(values[1]/(sum(values)))*100
#print VAR2

print "La primera componente principal explica el", VAR1, "% de la varianza."
print "La segunda componente principal explica el", VAR2, "% de la varianza."

##Grafica FR vs. FL
#	COPIADO DEL NOTE BOOK 
plt.scatter(FR_norm, FL_norm)
x_line = np.linspace(-3,3)
plt.plot(x_line, x_line*vectors[1,0]/vectors[0,0], linewidth=5.0)
plt.plot(x_line, x_line*vectors[1,1]/vectors[0,1], linewidth=5.0)
plt.savefig("pca_fr_fl.pdf")
plt.close()

plt.scatter(BL_norm, FL_norm)
x_line = np.linspace(-3,3)
plt.plot(x_line, x_line*vectors[1,0]/vectors[0,0], linewidth=5.0)
plt.plot(x_line, x_line*vectors[1,1]/vectors[0,1], linewidth=5.0)
plt.savefig("pca_bl_fl.pdf")
plt.close()
