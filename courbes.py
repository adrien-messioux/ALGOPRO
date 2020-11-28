#projet info 

import numpy as np
import matplotlib.pyplot as plt 



#x = np.array([])
#y = np.array([])

#plt.plot(x, y)
#plt.show()

import pandas as pd 
T = pd.read_csv("EIVP_KM.csv", sep=';')
#print (T)


L = list(T)
#print(L)


L1 = T['id'].tolist()
#print (L1)

L2 = T['noise'].tolist()
#print (L2)

L3 = T['temp'].tolist()

L4 = T['humidity'].tolist()

L5 = T['lum'].tolist()
L6 = T['co2'].tolist()

L7 = T['sent_at'].tolist()



# séparer les valeurs en fonction des capteurs 

def capteurs(L1):
    l1 = []
    l2 = []
    for i in range(len(L1)):
        if L1[i] == 1 :
            l1.append(L1[i])
        else :
            l2.append(L1[i])
    return l1, l2
        
l1, l2 = capteurs(L1)
#print (l1, l2)


def new(L2):
    L2a = L2[:1336]
    return L2a

L2a = new(L2)
#print (L2a)
    
L7a = new(L7)
#print (L7a)

y = np.array(L2a)
x = np.array(L7a)
    
plt.plot(x, y)
plt.show()

L5a = new(L5)
x = np.array(L7a)
y = np.array(L5a)
    
plt.plot(x, y)

plt.xlabel("sent_at")
plt.ylabel("lum")
plt.title("courbe des valeurs de la lumière en fonction du temps")

plt.show()

#calcul minimum 
def min(L):
    m = L[0]
    for i in range (len(L)):
        if L[i] <= m:
            m = L[i]
    return m 

m2 = min (L2a)
#print (m2)

m3 = min (L3a)

m4 = min (L4a)

m5 = min (L5a)

m6 = min (L6a)

#calcul maximum 
def max(L):
    M = L[0]
    for i in range (len(L)):
        if L[i] >= M:
            M = L[i]
    return M

M2 = max(L2a)
#print (M2)

M3 = max(L3a)

M4 = max(L4a)

M5 = max(L5a)

M6 = max(L6a)

#calcul moyenne 
def moyenne (L):
    somme = 0
    for i in range (len(L)):
        somme = somme + L[i]
    return somme/len(L)

#print(moyenne(L2a))

#détection anomalies

def anomalies():
    
    
        