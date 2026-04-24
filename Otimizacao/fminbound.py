import numpy as np
from scipy import optimize


def f(x):
    return x**2/10 - 2*np.sin(x)


xopt = optimize.fminbound(f, 0, 4)
print(f"xopt = {xopt:.6f}")
