import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return x**2 + np.sin(x)

i = f(-1/np.sqrt(3)) + f(1/np.sqrt(3))

print(i)
