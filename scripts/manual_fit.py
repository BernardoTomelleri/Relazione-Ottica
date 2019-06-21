import numpy as np
from matplotlib import pyplot as plt

u = np.array([-526.4,	-524.4,	-452.4,	-256.4,	-53.4,	89.6,	252.6,	443.6,	514.6,	512.6])
v = np.array([298.7,	191.7,	-22.3,	-204.3,	-266.3,	-263.3,	-202.3,	-21.3,	189.7,	299.7])
du = 0.5
dv = 0.5
n=10

#Manual Implementation of Least Squares fit
xmed = np.mean(u)
ymed = np.mean(v)
Suu=0
Svv=0
Suv=0
Suuu=0
Svvv=0
Suuv=0
Suvv=0
    
for i in range(0,n):
    u[i] = u[i] - xmed
    v[i] = v[i] - ymed
    Suu = Suu + u[i] * u[i]
    Svv = Svv + v[i] * v[i]
    Suv = Suv + u[i] * v[i]
    Suuu = Suuu + u[i] * u[i] * u[i]
    Svvv = Svvv + v[i] * v[i] * v[i]
    Suuv = Suuv + u[i] * u[i] * v[i]
    Suvv = Suvv + u[i] * v[i] * v[i]

uc=(Svv*(Suuu+Suvv)-Suv*(Svvv+Suuv))/(2*(Suu*Svv-Suv*Suv))
vc=(Suv*(Suuu+Suvv)-Suu*(Svvv+Suuv))/(2*(Suv*Suv-Suu*Svv))

#Optimal Parameters for the circle
R=np.sqrt(uc*uc+vc*vc+(Suu+Svv)/n)
xc=uc+(xmed)
yc=vc+(ymed)

#Plotting data points with arbitrary uncertainty
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, ax = plt.subplots()

plt.xlabel('x [pixel]')
plt.ylabel('y [pixel]')
plt.title('Arcobaleno')
plt.grid(color = 'gray')
plt.errorbar(u, v, dv, du, '+', label = 'data')

# Fitting with a Bezier-approximated circle
ax.add_patch(plt.Circle((0,0), R, color='orange', fill = False, label ='modello'))
ax.set_aspect('equal', adjustable='datalim')
ax.plot()   #Causes an autoscale update.
plt.legend()

print('Ascissa Centro x_c= %.1f +- %.1f' %(xc, du))
print('Ordinata Centro y_c= %.1f +- %.1f' %(yc, dv))
print('Raggio R= %.1f +- %.1f' %(R, dv))
plt.show()