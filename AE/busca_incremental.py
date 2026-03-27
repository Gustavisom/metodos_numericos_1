import numpy as np
import matplotlib.pyplot as plt 
import math



limite_inferior = 3
limite_superior = 6
passo = 100
x = np.arange(limite_inferior, limite_superior, passo)

def busca_incremental(x):
    return np.sin(10*x) + np.cos(3*x)
x = np.linspace(3, 6, 100)
y = busca_incremental(x)
plt.figure()
plt.plot(x, y, label='Função')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.title('Busca Incremental')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

