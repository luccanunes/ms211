from newton import newton_lucca
from plot import plotar_funcao

def f(x):
    return x**3 - 5*x

def df(x):
    return 3*x**2 - 5

# Plotando o gráfico de f
plotar_funcao(f, "x³ - 5x")

# Aplicando método de Newton em f para x0 = 1
print(f"Aproximação da raiz com x0 = 1 limitado a 20 iterações: {newton_lucca(1, f, df, False, 20)}")

# Aplicando método de Newton em f para x0 = -1
print(f"Aproximação da raiz com x0 = -1 limitado a 20 iterações: {newton_lucca(-1, f, df, False, 20)}")

# Aplicando método de Newton em f para x0 = 0.5
print(f"Aproximação da raiz com x0 = 0.5 limitado a 20 iterações: {newton_lucca(0.5, f, df, False, 20)}")

# Aplicando método de Newton em f para x0 = -0.5
print(f"Aproximação da raiz com x0 = -0.5 limitado a 20 iterações: {newton_lucca(-0.5, f, df, False, 20)}")

# Aplicando método de Newton em f para x0 = -0.5
print(f"Aproximação da raiz com x0 = -0.5 limitado a 20 iterações: {newton_lucca(-0.5, f, df, False, 20)}")