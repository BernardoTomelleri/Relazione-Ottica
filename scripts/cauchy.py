# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:56:22 2019

@author: berna
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
#Dati ingresso
n=np.array([1.331, 1.335, 1.343])
dn=np.array([0.002, 0.002, 0.002])
l=np.array([0.63, 0.57, 0.45])
dl=np.full(len(l), 0.005)
ll = np.linspace(min(l)-0.2, max(l)+0.1, 100)
n_0 = 1.3175
#n_0 = 1.318+-0.005
# Fit con Cauchy
def cauchy(l, A):
    return n_0 + A/(l**2)

popt, pcov = curve_fit(cauchy, l, n, 0.004, dn, absolute_sigma = True)
A_fit = popt
dA_fit = np.sqrt(pcov.diagonal())
print('A = %f +- %f' % (A_fit, dA_fit))
#Calcolo del Chi quadro
res = n - cauchy(l, A_fit)
resnorm = res/dn
chisq = (resnorm**2).sum()
ndof = len(n) - 1
chirid = chisq/ndof
print('Chi quadro/ndof = %f/%d' % (chisq, ndof))
print('Chi quadro ridotto:', chirid)
#Plot
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig1,(ax1, ax2) = plt.subplots(2,1, True, gridspec_kw={'wspace':0.05, 'hspace':0.05, 'height_ratios': [3, 1]})
ax1.set_ylabel('Indice di rifrazione $n$ [a.u.]')
ax1.grid(color = 'gray', linestyle = '--', alpha=0.7)
ax1.errorbar(l, n, dn, dl, 'ko', elinewidth = 1., capsize=1., ms=1., linestyle='', label='data', zorder=0)
ax1.plot(ll, cauchy(ll, A_fit), label='fit', zorder=10)
ax1.xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax1.xaxis.set_minor_locator(plt.MultipleLocator(0.01))
ax1.yaxis.set_major_locator(plt.MultipleLocator(0.01))
ax1.yaxis.set_minor_locator(plt.MultipleLocator(0.002))
ax1.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax1.tick_params(which='minor', direction='in', width=1., top=True, right=True)
legend = ax1.legend(loc ='best')

ax2.set_xlabel('Lunghezza d\'onda $\lambda$ [$\mu$m]', x=0.84)
ax2.set_ylabel('Residui')
ax2.axhline(0, c='r',zorder =1)
ax2.errorbar(l, resnorm, 1., None, 'ko', elinewidth = 1., capsize=1., ms=1., linestyle='', zorder=5)
ax2.grid(color ='gray', linestyle = '--', alpha=0.7, zorder=0)
ax1.xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax1.xaxis.set_minor_locator(plt.MultipleLocator(0.01))
ax2.yaxis.set_major_locator(plt.MultipleLocator(1.))
ax2.yaxis.set_minor_locator(plt.MultipleLocator(1./2))
ax2.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax2.tick_params(which='minor', direction='in', width=1., top=True, right=True)
plt.show()