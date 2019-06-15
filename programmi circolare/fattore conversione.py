import numpy as np

x, y = np.loadtxt('coordinate pixel.txt', unpack = True)
az, pol = np.loadtxt('coordinate_celesti.txt', unpack = True)

az = (az*np.pi)/180
pol= (pol*np.pi)/180

A = np.cos(pol[0])*np.cos(pol[1])+ np.sin(pol[0])*np.sin(pol[1])*np.cos(az[0]-az[1])
alfa1 = np.arccos(A)


A = np.cos(pol[1])*np.cos(pol[2])+ np.sin(pol[1])*np.sin(pol[2])*np.cos(az[1]-az[2])
alfa2 = np.arccos(A)


A = np.cos(pol[2])*np.cos(pol[0])+ np.sin(pol[2])*np.sin(pol[0])*np.cos(az[2]-az[0])
alfa3 = np.arccos(A)


d1 = np.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)


d2 = np.sqrt((x[1] - x[2])**2 + (y[1] - y[2])**2)


d3 = np.sqrt((x[2] - x[0])**2 + (y[2] - y[0])**2)

f1 = alfa1/d1

f2 = alfa2/d2

f3 = alfa3/d3

f = (f1+f2+f3)/3
f = (f/np.pi)*180
print('%.2f' %(f))
a = f*197.6
da = f*0.2
print('%.2f +- %.2f' %(a, da))

a = a*(np.pi/180)

n = (np.sin((a + (np.pi)/3)/2))/(np.sin(np.pi/6))
dn = abs(np.cos((a +(np.pi/3)/2)))*da
print('%.2f +- %.2f' %(n, dn))