import numpy as np
import math
import matplotlib.pyplot as plt

# Dados Iniciais
x = 0.5
n = 10
u = math.log(1 + x)

# Pré-alocação
soma = 0
estimativa = []
contador = []
EPT = []
EPEST = []
v_old = 0

# Variáveis de controle
i = 1
eppara = 0.5*(10**(2-n))
epest = 100

# Série de MacLaurin
def ex(x,i):
    return ((-1)**(i+1)) * (x**i)/i


while epest > eppara:
    
    soma = soma + ex(x,i) 
    v_new = soma
    
    # erro verdadeiro percentual
    Ept = abs((u - soma)/u)*100
    
    # erro aproximado percentual
    epest = abs((v_new - v_old)/v_new)*100
    
    # armazenando valores
    EPT.append(Ept)
    EPEST.append(epest)
    estimativa.append(soma)
    contador.append(i)
    
    # atualização
    v_old = v_new
    i = i + 1


# Gráfico da estimativa
plt.figure()
plt.plot(contador,estimativa,'or',label="$ln(1+x)$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("Estimativa")
plt.grid()

# Gráfico dos erros
plt.figure()
plt.plot(contador,EPT,'ok',label="$E_{pt}$")
plt.plot(contador,EPEST,'og',label="$E_{pest}$")
plt.legend()
plt.xlabel("Número de termos")
plt.ylabel("$E_{pt}$ (%)")
plt.grid()

# Resultados
print("Valor real =", u)
print("Última estimativa =", estimativa[-1])
print("Número de termos usados =", len(contador))
print("Último erro aproximado =", epest)

plt.show()
