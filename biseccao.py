import matplotlib.pyplot as plt
import numpy as np

def biseccao(f, a, b, n = 100):
    for _ in range(n):
        x = (a + b) / 2
        eixo_x.append(_)
        dados_execucao.append(x)
        if f(a) * f(x) <= 0:
            b = x
        else:
            a = x

def f(x):
    return 1+pow(x, 3)-1/x

dados_execucao = []
eixo_x = []
biseccao(f, 0.1, 1, 5)
plt.plot(eixo_x, dados_execucao)
plt.title('Execução da bissecção com a0 = 0.1 e b0 = 1')
plt.xlabel('Número da iteração (k)')
plt.ylabel('Valor estimado na iteração k (xk)')
plt.show()


