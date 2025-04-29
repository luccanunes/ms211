import math
import matplotlib.pyplot as plt
import numpy as np
from newton import newton

def f(x):
    return math.pi - 1/x

def derivada_f(x): 
    return 1/(x*x)

x = np.linspace(-10, 10, 400)
y = f(x)
plt.plot(x, y)
plt.title('Gráfico de f(x) = pi - 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

dados_execucao = []
x = []
newton(0.5, f, derivada_f, dados_execucao, x)
plt.plot(x, dados_execucao)
plt.title('Execução de Newton com x0 = 0.5')
plt.xlabel('Número da iteração (k)')
plt.ylabel('Valor estimado na iteração k (xk)')
plt.show()

dados_execucao = []
x = []
newton(0.7, f, derivada_f, dados_execucao, x, True, 10)
plt.plot(x, dados_execucao)
plt.title('Execução de Newton com x0 = 0.7')
plt.xlabel('Número da iteração (k)')
plt.ylabel('Valor estimado na iteração k (xk)')
plt.show()
