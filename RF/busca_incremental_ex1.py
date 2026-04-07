import numpy as np

def f(x):
    return np.sin(10*x) + np.cos(3*x)

n = 100
x = np.linspace(3, 6, n)
xb = []
nb = 0


for i in range(n-1):
    xl = x[i]
    xu = x[i+1]

    if (f(xl) * f(xu) < 0):
        nb += 1
        xb.append([xl, xu])
    else:    
        print("Não há raiz entre", xl, "e", xu)

print("xb = ", xb)
print("y =", f(x))
print("Número de intervalos com raiz:", nb)

