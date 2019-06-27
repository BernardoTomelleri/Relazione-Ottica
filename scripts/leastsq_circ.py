# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:18:43 2019

@author: berna
"""
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
# Testo dei grafici in LaTeX (opzionale)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
# Definizione dati in ingresso e offset dallo 0 degli assi di GIMP
rnbw_offset = 866
halo_offset = 800
x, y = np.loadtxt('./data/alone.txt', skiprows=1, unpack = True)
y = halo_offset - y
dy = np.full(len(y), 1.)

def calc_R(x,y, xc, yc):
    " calcola la distanza di ogni punto dal centro (xc, yc) "
    return np.sqrt((x-xc)**2 + (y-yc)**2)

def f(c, x, y):
    " calcola distanza algebrica tra i dati e il cerchio centrato in c=(xc, yc) "
    Ri = calc_R(x, y, *c)
    return Ri - Ri.mean()

def leastsq_circle(x,y):
    # coordinate del baricentro
    x_m = np.mean(x)
    y_m = np.mean(y)
    center_estimate = x_m, y_m
    center, ier = optimize.leastsq(f, center_estimate, args=(x,y))
    xc, yc = center
    Ri       = calc_R(x, y, *center)
    R        = Ri.mean()
    res   = ((Ri - R))
    return xc, yc, R, res

# Fit
xc, yc, R, res = leastsq_circle(x,y)
print(res)
print('Raggio R = %f' %R)
print('Coordinate centro (xc, yc) = (%f, %f)' %(xc, yc))
theta_fit = np.linspace(-np.pi, np.pi, 180)
x_fit = xc + R*np.cos(theta_fit)
y_fit = yc + R*np.sin(theta_fit)
# Chi quadro
resnorm = res/dy
chisq = (resnorm**2).sum()
ndof = len(y) - 3
print('Chi quadro/ndof = %f/%d' % (chisq, ndof))
print('Chi quadro ridotto:', (chisq/ndof))

# Grafici
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8, 8), gridspec_kw={'wspace':0.08, 'hspace':0.08, 'height_ratios': [4, 1]})
ax1.axis('equal',adjustable='datalim')
ax1.set_title('Fit Alone Verde')
ax1.grid(color = 'gray', linestyle = '--', alpha=0.7)
ax1.plot(x_fit, y_fit, 'g-', label='modello')
ax1.plot([xc], [yc], 'k.', mec='y', mew=1)
ax1.errorbar(x, y, dy, dy, 'k+', label='data', mew=1)
ax1.set_ylabel('y [pixel]')   
ax1.xaxis.set_major_locator(plt.MultipleLocator(50.))
ax1.xaxis.set_minor_locator(plt.MultipleLocator(10.))
ax1.yaxis.set_major_locator(plt.MultipleLocator(25.))
ax1.yaxis.set_minor_locator(plt.MultipleLocator(5.))
ax1.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax1.tick_params(which='minor', direction='in', width=1., top=True, right=True)   
ax1.legend(loc='best',labelspacing=0.1 )
# Residui
ax2.grid(color ='gray', linestyle = '--', alpha=0.7, zorder=0)
ax2.axhline(0, c='r',zorder=1)
ax2.errorbar(x, resnorm, dy, dy, 'ko', markersize=2., elinewidth=1.2, capsize=2., linestyle='')
ax2.set_xlabel('x [pixel]')
ax2.set_ylabel('Residui [a.u.]')
ax2.xaxis.set_major_locator(plt.MultipleLocator(50.))
ax2.xaxis.set_minor_locator(plt.MultipleLocator(10.))
ax2.yaxis.set_major_locator(plt.MultipleLocator(1.))
ax2.yaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax2.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax2.tick_params(which='minor', direction='in', width=1., top=True, right=True)           
plt.show()