import numpy as np 

A = np.array([[3, -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])

b = np.array([[7.85],
              [-19.3], 
              [71.4]])


xold = np.zeros(len(b))
n = len(b)
eppara = 0.5 * (10 ** (2 - 6))
xnew = np.zeros(len(b))

epest = abs((xnew - xold) / xnew) * 100

while max(epest) >= eppara:
    for i in range(n):
        soma = 0
        for j in range(i):
            if j < i:
                soma += A[i,j]*xnew[j]
            soma += A[i,j]*xnew[j]
        xnew[i] = (b[i] - soma) / A[i,i]
    epest = abs((xnew - xold) / xnew) * 100
    xold = xnew

print("A solução é: ", xnew)

