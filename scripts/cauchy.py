# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:56:22 2019

@author: berna
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

n=np.array([1.3393, 1.33257])
dn=np.full(len(n), 0.0001)
l=np.array([0.57, 0.65])
dl=np.full(len(l), 0.01)
n_0 = 4./3
def cauchy(l, A):
    return n_0 + A/(l**2)

# Fit di V vs t
popt, pcov = curve_fit(cauchy, l, n, 0.004, dn, absolute_sigma = True)
A_fit = popt
dA_fit = np.sqrt(pcov.diagonal())
print('A = %f +- %f cm/s' % (A_fit, dA_fit))

#Calcolo del Chi quadro su fit_v
chisq = (((n - cauchy(l, A_fit))/dn)**2).sum()
ndof = len(n) - 2
#Chi quadro ridotto, ovvero diviso per il numero di gradi di libertà
chirid = chisq/ndof
print('Chi quadro/ndof = %f/%d' % (chisq, ndof))
print('Chi quadro ridotto_v:', chirid)
res = n - cauchy(l, A_fit)
resnorm = res/dn
ll = np.linspace(min(l)-0.3, max(l)+0.1, 100)
fig1,(ax1, ax2) = plt.subplots(2,1, True, gridspec_kw={'wspace':0.05, 'hspace':0.05, 'height_ratios': [3, 1]})
ax1.set_ylabel('Refractive index $n$ [a.u.]')
ax1.grid(color = 'gray', linestyle = '--', alpha=0.7)
ax1.errorbar(l, n, dn, dl, 'ko', elinewidth = 0.7, capsize=0.7, markersize=1., linestyle='', label='data', zorder=0)
ax1.plot(ll, cauchy(ll, A_fit), label='fit', zorder=10)
#ax1.xaxis.set_major_locator(plt.MultipleLocator(20.))
#ax1.xaxis.set_minor_locator(plt.MultipleLocator(5.))
#ax1.yaxis.set_major_locator(plt.MultipleLocator(5.))
#ax1.yaxis.set_minor_locator(plt.MultipleLocator(1.))
ax1.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax1.tick_params(which='minor', direction='in', width=1., top=True, right=True)
legend = ax1.legend(loc ='best')

ax2.set_xlabel('Wavelength $\lambda$ [$\mu$m]', x=0.9)
ax2.set_ylabel('Residuals')
ax2.plot(ll, 0*ll, 'r', zorder=10)
ax2.errorbar(l, resnorm, 1., None, 'ko', elinewidth = 0.7, capsize=0.7, markersize=1., linestyle='', zorder=0)
ax2.grid(color ='gray', linestyle = '--', alpha=0.7)
#ax2.xaxis.set_major_locator(plt.MultipleLocator(20.))
#ax2.xaxis.set_minor_locator(plt.MultipleLocator(5.))
#ax2.yaxis.set_major_locator(plt.MultipleLocator(1.))
#ax2.yaxis.set_minor_locator(plt.MultipleLocator(1./2))
ax2.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax2.tick_params(which='minor', direction='in', width=1., top=True, right=True)
