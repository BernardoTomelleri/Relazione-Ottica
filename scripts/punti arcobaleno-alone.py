import numpy as np

x, y = np.loadtxt('punti_alone_verde.txt', unpack = True)

def devstand(sample):
    m = sample.mean()
    return m
    
    
print(devstand(x)) 

u = x- devstand(x) 

print(u)

print(devstand(y))

v = y - devstand(y)
print(v)