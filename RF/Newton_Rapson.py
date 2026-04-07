import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

eppest = 100
i = 8
eppara = 0.5 * (10 ** (2 - i))
x0 = 0

def newton_raphson(f, df, x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new

while eppest > eppara:

    raiz = newton_raphson(f, df, x0)
    print(f"{raiz}")

