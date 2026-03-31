import numpy as np
import matplotlib.pyplot as plt

g = 9.81
cd = 0.25
v = 36
t = 4
n = 100
m = np.linspace(100, 200, n)

i = 8
eppara = 0.5 * (10 ** (2 - i))
xl = 100
xu = 200
xr = (xl + xu) / 2
epest = 100

def f(x):
    return np.sqrt((g * x) / cd) * np.tanh(np.sqrt((g * cd) / x) * t) - v


while epest >= eppara:
    xr = (xl + xu) / 2
    f_xl = f(xl)
    f_xr = f(xr)

    epest = abs(f_xr)  

    if f_xr * f_xl < 0:
        xu = xr
    else:
        xl = xr

print("Raiz aproximada:", xr)