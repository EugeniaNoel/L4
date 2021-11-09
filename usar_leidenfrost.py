import leidenfrost
import numpy as np
import matplotlib.pyplot as plt

#%%

med = np.loadtxt('medicion06.txt')

tiempo = med[0]
volt = med[1]

plt.figure()
plt.plot(tiempo, volt)
volt   = np.array(volt)*1000 #paso las unidades de V a mV
tiempo = np.array(tiempo)

#Convierto tensión en temperatura Kelvins
temp= leidenfrost.trmpr_k_mV2K_pol(volt)
plt.figure()
plt.plot(tiempo,temp,'.-')

#%%

#Especifico el valor de los parametros de la formula de Euler para el experimetno realizado
n=165.94/63.536             # moles de cobre
A=(0.011**2)*np.pi*0.049    #Superficie de contacto
a=0.77                      #para el cobre
b=0.26                      #para el cobre
c=9.17                      #para el cobre
tita_d=315                  #para el cobre

#Paso de temperatura a potencia entregada
q_a=leidenfrost.Q_A(temp,tiempo,n,A,a,b,c,tita_d)
q_a=q_a*(-1)

tempsat=74.2
temp=temp-tempsat

font = {'family': 'century gothic', 'weight': 'bold','size': 20 }
plt.figure()
plt.plot(temp[0:-1],q_a,'.-')
plt.xticks(np.arange(0, 253, 10.0), fontsize=20)
plt.yticks(fontsize=20)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.grid()
plt.xlabel("T-Tsat (K)", fontdict=font)
plt.ylabel("Q/A (sin unidades)", fontdict=font)
