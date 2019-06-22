# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 02:34:33 2019

@author: berna
"""

import numpy as np
from matplotlib import pyplot as plt
n=1.31
phi = np.pi/3.
deg = 180./np.pi
x = np.linspace(0.3, 1.51, 200)
def diffusion(i):
    return (i -phi + np.arcsin(np.sin(phi)*np.sqrt(n**2 - np.sin(i)**2) - np.cos(phi)*np.sin(i)))*deg

y=diffusion(x)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, ax = plt.subplots()
ax.set_ylabel('Angolo di diffusione $\delta_m$ $[\deg]$')
ax.set_xlabel(r'Angolo di incidenza $i$ $[\deg]$', x=0.84)
ax.grid(color = 'gray', linestyle = '--', alpha=0.7)
ax.plot(x*deg, y, '-', label='$\delta_m$', zorder =10)
ax.plot(41, np.min(diffusion(x)),'o', ms=4., label='Minimo')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax.tick_params(which='minor', direction='in', width=1., top=True, right=True)
legend = ax.legend(loc ='best')
plt.show()