import numpy as np

A = np.array([[2, 4, -6],
              [4, 2, 2],
              [2, 8, -4]])

b = np.array([[10],
              [16], 
              [24]])

aum = np.hstack((A, b)) # matriz aumentada

n = len(b)

# eliminação progressiva

for i in range(n-1):
    for j in range(i+1, n):
        fator = aum[j,i]/aum[i,i]
        aum[j,i:n+1] = aum[j,i:n+1] - fator * aum[i,i:n+1]


print(aum)

#substituiçao regressiva

x = np.zeros(n)

x[n-1] = aum[n-1,n]/aum[n-1,n-1]

for i in range(n-2, -1, -1):
    soma = 0
    for j in range(i+1, n):
        soma += aum[i,j]*x[j]
    x[i] = (aum[i,n] - soma)/aum[i,i]

print(x)
