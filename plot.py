import numpy as np
import matplotlib.pyplot as plt

def plotar_funcao(f, equacao, nome="", x = np.linspace(-10, 10, 500)):
    y = f(x)
    plt.plot(x, y, label=f"f(x) = {equacao}")
    plt.title(f"Gráfico da Função {nome}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color="black",linewidth=0.5)
    plt.axvline(0, color="black",linewidth=0.5)
    plt.legend()
    plt.show()