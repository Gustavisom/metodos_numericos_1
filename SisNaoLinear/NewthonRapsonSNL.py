import numpy as np

def f1(x, y):
    return x**2 - x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

def df1_dx(x, y):
    return 2*x - y

def df1_dy(x, y):
    return -x

def df2_dx(x, y):
    return 3*y**2

def df2_dy(x, y):
    return 1 + 6*x*y

xold = np.array([1.5, 3.5])

jacobiano = np.array([[df1_dx, df1_dy],
                      [df2_dx, df2_dy]])

epest = np.ones(2) * 100
i = 6
eppara = 0.5 * (10 ** (2 - i))



while np.max(epest) >= eppara:

    jacobiano = np.array([[df1_dx(xold[0], xold[1]), df1_dy(xold[0], xold[1])],
                          [df2_dx(xold[0], xold[1]), df2_dy(xold[0], xold[1])]])

    den = jacobiano[0, 0] * jacobiano[1, 1] - jacobiano[0, 1] * jacobiano[1, 0]
    num1 = (f1(xold[0], xold[1]) * jacobiano[1, 1]) - (f2(xold[0], xold[1]) * jacobiano[0, 1])
    num2 = (f2(xold[0], xold[1]) * jacobiano[0, 0]) - (f1(xold[0], xold[1]) * jacobiano[1, 0])

    xnew = np.array([xold[0] - num1/den,
                     xold[1] - num2/den])

    epest = np.abs((xnew - xold) / xnew) * 100
    xold = xnew.copy()

print("Solução:", xnew)
