# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 06:20:42 2019

@author: berna
"""

#Grafico dell'angolo per la diffusione con 1 riflessione interna
import numpy as np
from matplotlib import pyplot as plt
n=4./3
deg = 180./np.pi
x = np.linspace(0.083, 1.8, 200)
def diffusion(x):
    return (4*np.arcsin(np.sin(x)/n) -2*x)*deg

y=diffusion(x)
#Plot
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, ax = plt.subplots()
ax.set_ylabel('Angolo di diffusione $\delta_1$ $[\deg]$')
ax.set_xlabel(r'Angolo di incidenza $\i_1$ $[\deg]$', x=0.84)
ax.grid(color = 'gray', linestyle = '--', alpha=0.7)
ax.plot(x*deg, y, '-', label='$\delta_1$', zorder =10)
ax.plot(1.037*deg, np.max(diffusion(x)),'o',ms=4., label='Massimo')
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
ax.xaxis.set_minor_locator(plt.MultipleLocator(2))
ax.yaxis.set_major_locator(plt.MultipleLocator(10))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2))
ax.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax.tick_params(which='minor', direction='in', width=1., top=True, right=True)
legend = ax.legend(loc ='best')
plt.show()