import numpy as np

A = np.array([[-7, 3, 5],
              [-2, 4, -5],
              [0, 2, -1]], dtype=float)
b = np.array([7, -3, 1], dtype=float)

n = len(b)
xold = np.ones(n) * 100
eppara = 0.5 * (10 ** (2 - 6))
xnew = np.zeros(n)
epest = np.ones(n) * 100
maxit = 100
k = 0

while max(epest) >= eppara and k < maxit:
    for i in range(n):
        soma = 0
        for j in range(n):
            if j < i:
                soma += A[i, j] * xnew[j]  
            elif j > i:
                soma += A[i, j] * xold[j]  
        xnew[i] = (b[i] - soma) / A[i, i]

    k += 1
    epest = abs((xnew - xold) / xnew) * 100
    xold = xnew.copy()

print("Número de iterações:", k)
print("Solução:", xnew)