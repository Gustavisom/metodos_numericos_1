import numpy as np
from scipy import optimize


def f(x):
    return 2 + x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2


x0 = [0, 0]


resultado = optimize.minimize(f, x0)
print(f"resultado = {resultado}")
