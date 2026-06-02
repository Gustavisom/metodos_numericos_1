import numpy as np

A = np.array([[8, 3, 1],
              [-6, 0, 7],
              [2, 4, -1]])

b = np.array([12, 1, 5])

n = len(b)
xold = np.ones(n) * 100
eppara = 0.5 * (10 ** (2 - 6))
xnew = np.zeros(n)
epest = np.ones(n) * 100
k = 0


while max(epest) >= eppara and k < 100:
    for i in range(n):
        soma = 0
        for j in range(n):
            if j != i:
                soma += A[i, j] * xnew[j]
        xnew[i] = (b[i] - soma) / A[i, i]
    
    k += 1
    epest = abs((xnew - xold) / xnew) * 100
    xold = xnew.copy()

print("Solução:", xnew)
print("Número de iterações:", k)