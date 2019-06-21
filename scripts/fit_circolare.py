import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x, y = np.loadtxt('punti_alone_verde.txt', unpack = True)
u, v = np.loadtxt('diff_alone_verde.txt', unpack = True)
dy = np.array([3.963966933767142, 2.1069640302407757, 1.5626722928137091, 9.352532306686175, 6.908956899311899, 3.2152982950996636, 5.035185850701312, 2.212867953363089, 4.44898294015957, 8.29870183835454, 1.7938601656148332, 7.293339165255372])

xmed = 604.3333333333334
ymed = 559.9166666666666
Suu =(u**2).sum()
Suuu = (u**3).sum()


Svv =(v**2).sum()
Svvv = (v**3).sum()

Suv = (u*v).sum()
Suuv = ((u**2)*v).sum()
Suvv = ((v**2)*u).sum()

uc = (Svv*(Suuu+Suvv)-Suv*(Svvv+Suuv))/((2*(Suu*Svv)-(Suv*Suv)))
vc = (Suu*(Svvv+Suuv)-Suv*(Suuu+Suvv))/((2*(Suu*Svv)-(Suv*Suv)))
r = np.sqrt((uc**2) + (vc**2) + (Suu+Svv)/len(u)) 
xc = uc + xmed
yc = vc + ymed
print(xc)
def funzionefit(x,R):
     return yc + np.sqrt(-((x-xc)**2) + R**2)

init=(r,)

pars, covm = curve_fit(funzionefit, x, y, init, ) 
R = pars
dR = np.sqrt(covm.diagonal())

resnorm1= (( y - funzionefit(x, R))/dy)
chiquadt1 = len(x)-len(init)
dchiquadt1 = np.sqrt(2*chiquadt1)
chiquad1 = (resnorm1**2).sum()

plt.figure(2)
plt.title('Fit circolare verde', fontsize = 16)
plt.errorbar(x, y, dy, linestyle='', color='black', marker='.')
plt.xlabel('$x$ [pixel]')
plt.ylabel('$y$ [pixel]')
xx1 = np.linspace(min(x), max(x), 300000)
plt.plot(xx1, funzionefit(xx1, R), color = 'green')

print('%.1f +- %.1f' %(R, dR))
print('%.0f\(%.0f +- %.0f)'%(chiquad1, chiquadt1, dchiquadt1))
plt.show()