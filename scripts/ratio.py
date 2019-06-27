# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:17:25 2019

@author: berna
"""
import numpy as np
from matplotlib import pyplot as plt

deg = 180./np.pi
x = np.linspace(1., 1.55, 200)
def ratio(x):
    return (np.pi+2*np.arcsin((np.sqrt(9.-x**2))/(2*np.sqrt(2)))-6*np.arcsin(np.sqrt(9.-x**2)/(2*np.sqrt(2)*x)))/(4*np.arcsin((np.sqrt(4.-x**2))/(x*np.sqrt(3)))-2*np.arcsin((np.sqrt(4.-x**2))/(np.sqrt(3)))) -1.213

y=ratio(x)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, ax = plt.subplots()
ax.set_ylabel('Rapporto angoli $\delta_2 /\delta_1 - R/r$')
ax.set_xlabel(r'Indice di Rifrazione $n$', x=0.86)
ax.grid(color = 'gray', linestyle = '--', alpha=0.7)
ax.plot(x, y, '-', label='$\delta_2 /\delta_1 - R/r$', zorder =10)
ax.axhline(0, xmax=1, lw = 1.2, c='k', ls='-',zorder =0)
ax.axvline(1.333, ymax=0.38, lw = 1.2, c='k', ls='--', zorder = 1)
ax.plot(1.333, ratio(1.333),'ro', ms=4., label='$x \simeq 1.333$', zorder=5)
ax.xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.01))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax.tick_params(which='minor', direction='in', width=1., top=True, right=True)
legend = ax.legend(loc ='best')
plt.show()