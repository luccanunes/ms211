from newton import newton_lucca
from plot import plotar_funcao

def f(x):
    return x**(1/3)

def df(x):
    return 1/(3 * x ** (2/3))

# Plotando o gráfico de f
plotar_funcao(f, "∛x")

# Aplicando método de Newton em f para x0 = 1
print(f"Aproximação da raiz com x0 = 1 limitado a 20 iterações: {newton_lucca(1, f, df, True, 20)}")

# Aplicando método de Newton em f para x0 = 0.00000001
print(f"Aproximação da raiz com x0 = 0.00000001 limitado a 20 iterações: {newton_lucca(1e-8, f, df, True, 20)}")


# Usando a expressão simplificada de f(xn)/df(xn) para evitar números imaginários:

def newton_simplificado(x0, show=False, max_iter = 1000, eps = 1e-10):
    ant = 0
    i = 0
    while abs(x0 - ant) > eps and i < max_iter:
        if show:
            print(x0)
        ant = x0
        x0 = -2*x0
        i += 1
    return x0

# Aplicando método de Newton em f para x0 = 1
print(f"Aproximação da raiz com x0 = 1 com a expressão simplificada: {newton_simplificado(1, True, 20)}")

# Aplicando método de Newton em f para x0 = 0.00000001
print(f"Aproximação da raiz com x0 = 0.00000001 com a expressão simplificada: {newton_simplificado(1e-8, True, 20)}")