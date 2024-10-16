import numpy as np
### Desafio de Calculo 4

n = 2

def fun(x):
    x = 1/(x*(np.log(x))**2)
    return x

while fun(n) > 0.00000001:
    soma = 0
    soma += fun(n)
    n += 1

soma = np.ceil(soma)
print(f"A soma discreta de 1/(x*(ln(x)^2) de 2 à +inf converge para {soma}")
