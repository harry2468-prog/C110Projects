import math as mt
import matplotlib.pyplot as plt
Pdata =[]
Tdata=[]
for P in range(11,1300000):
         Pdata.append(P)
         T=29.365*mt.log(P,mt.e)+204.46
         Tdata.append(T)
plt.plot(Pdata,Tdata)
plt.title('P-T Diagram of Distillation of glycerol and methly oleate')
plt.xlabel('Pressure in Pa')
plt.ylabel('Temperature in K')
plt.show()

