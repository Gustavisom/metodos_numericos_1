import numpy as np
import math
import matplotlib.pyplot as plt

# ── Função da série de MacLaurin de ln(1+x) ──────────────────────────────────
def serie_ln(x, n=10):
    u = math.log(1 + x)
    soma = 0
    estimativa, contador, EPT, EPEST = [], [], [], []
    v_old = 0
    i = 1
    eppara = 0.5 * (10 ** (2 - n))
    epest = 100

    def ex(x, i):
        return ((-1) ** (i + 1)) * (x ** i) / i

    while epest > eppara:
        soma = soma + ex(x, i)
        v_new = soma

        Ept = abs((u - soma) / u) * 100
        epest = abs((v_new - v_old) / v_new) * 100

        EPT.append(Ept)
        EPEST.append(epest)
        estimativa.append(soma)
        contador.append(i)

        v_old = v_new
        i = i + 1

    return u, estimativa, contador, EPT, EPEST


# ── Dois valores de x ─────────────────────────────────────────────────────────
valores_x = [0.5, 0.9]

for x in valores_x:

    u, estimativa, contador, EPT, EPEST = serie_ln(x)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"Série de MacLaurin — $ln(1+x)$,  x = {x}", fontsize=13)

    # Subplot esquerdo: estimativa
    ax1.plot(contador, estimativa, 'or', label=f"$ln(1+{x})$")
    ax1.axhline(u, color='blue', linestyle='--', label=f"Valor real = {u:.6f}")
    ax1.set_xlabel("Número de termos")
    ax1.set_ylabel("Estimativa")
    ax1.set_title("Estimativa")
    ax1.legend()
    ax1.grid()

    # Subplot direito: erros
    ax2.plot(contador, EPT,   'ok', label="$E_{pt}$")
    ax2.plot(contador, EPEST, 'og', label="$E_{pest}$")
    ax2.set_xlabel("Número de termos")
    ax2.set_ylabel("Erro (%)")
    ax2.set_title("Erros")
    ax2.legend()
    ax2.grid()

    # Resultados
    print(f"\n--- x = {x} ---")
    print("Valor real =", u)
    print("Última estimativa =", estimativa[-1])
    print("Número de termos usados =", len(contador))
    print("Último erro aproximado =", EPEST[-1])

plt.show()