import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2/10 - 2*np.sin(x)

i = 6
epara = 0.5 * (10 ** (2 - i))
epest = 100

x1 = 0
x2 = 1
x3 = 4
x4_old = []

while epest >= epara:
    x4_new = (x1 + x2 + x3) / 3
    x4_old.append(x4_new)
    if f(x4_old) < f(x1):
        x1 = x2
        x2 = x4_old
    else:
        x3 = x4_old
        x4_new = x4_old[-1]

    epest = abs((x4_new - x4_old[-2]) / x4_new) * 100
x4_old = x4_new

print(f"x4 = {x4_new:.6f}")