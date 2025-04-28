import math
import matplotlib.pyplot as plt
import numpy as np
from newton import newton

def f(x):
    return pow(x, 3) - 2*x + 2

def derivada_f(x): 
    return 3*pow(x, 2) - 2

x = np.linspace(-10, 10, 400)
y = f(x)
plt.plot(x, y)
plt.title('Gráfico de f(x) = x³ - 2x + 2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

dados_execucao = []
x = []
newton(0, f, derivada_f, dados_execucao, x, True, 10)
plt.plot(x, dados_execucao)
plt.title('Execução de Newton com x0 = 0')
plt.xlabel('Número da iteração (k)')
plt.ylabel('Valor estimado na iteração k (xk)')
plt.show()

dados_execucao = []
x = []
newton(0.03, f, derivada_f, dados_execucao, x, True, 10)
plt.plot(x, dados_execucao)
plt.title('Execução de Newton com x0 = 0.03')
plt.xlabel('Número da iteração (k)')
plt.ylabel('Valor estimado na iteração k (xk)')
plt.show()

dados_execucao = []
x = []
newton(-0.06, f, derivada_f, dados_execucao, x, True, 10)
plt.plot(x, dados_execucao)
plt.title('Execução de Newton com x0 = -0.06')
plt.xlabel('Número da iteração (k)')
plt.ylabel('Valor estimado na iteração k (xk)')
plt.show()

dados_execucao = []
x = []
newton(5, f, derivada_f, dados_execucao, x, True, 20)
plt.plot(x, dados_execucao)
plt.title('Execução de Newton com x0 = 5')
plt.xlabel('Número da iteração (k)')
plt.ylabel('Valor estimado na iteração k (xk)')
plt.show()
