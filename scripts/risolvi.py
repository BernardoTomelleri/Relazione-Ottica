import numpy as np
from sympy import * 

n = 1.9 
while(n <= 2):
    a = np.sqrt((9-(n**2))/8)
    b = (np.sqrt((9-(n**2))/8))/n
    c = np.sqrt((4-(n**2))/3)
    d = (np.sqrt((4-(n**2))/3))/n
    
    i2 = np.arcsin(a)
    r2 = np.arcsin(b)
    i1 = np.arcsin(c)
    r1 = np.arcsin(d)
    
    f = 2*(i2 - r2) + 2*(np.pi - 2*r2)
    g = 2*(i1 - r1) + (np.pi - 2*r1)
    
    h = abs(np.pi - f)
    p = abs(np.pi - g)
    
    D = h/p -1.240
    
    
    if (D <= 0.001):
        print(n,)
        break
    else: n = n - 0.001

# x = Symbol('x') 
# f = np.sqrt((9-(x**2))/8)
# g = (np.sqrt((9-(x**2))/8))/x
# h = np.sqrt((4-(x**2))/3)
# p = (np.sqrt((4-(x**2))/3))/x
# 
# q = np.arcsin(f)
# r = np.arcsin(g)
# s = np.arcsin(h)
# t = np.arcsin(p)
# 
# k = 2*(q - r) + 2*(np.pi - 2*r)
# j = 2*(s - t) + (np.pi - 2*t)
# 
# z = abs(np.pi - k)
# v = abs(np.pi - j)
# 
# y = z/v -1.240
# 
# yprime = y.diff(x) 
# 
# f1 = lambdify(x, yprime, 'numpy') 
# dn = 0.001/f1 (n) 
# 
# print('%.2f +- %.2f' % (n, dn))