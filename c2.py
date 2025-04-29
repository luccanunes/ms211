from newton import newton
from plot import plotar_funcao

def f(x):
    return x**3 - 5*x

def df(x):
    return 3*x**2 - 5

# Plotando o gráfico de f
plotar_funcao(f, "x³ - 5x")

# Aplicando método de Newton em f para x0 = 1
print(f"Aproximação da raiz com x0 = 1 limitado a 20 iterações: {newton(1, f, df, show=False, max_iter=20)}")
# Aplicando método de Newton em f para x0 = -1
print(f"Aproximação da raiz com x0 = -1 limitado a 20 iterações: {newton(-1, f, df, show=False, max_iter=20)}")

# Aplicando método de Newton em f para x0 = 0.5
print(f"Aproximação da raiz com x0 = 0.5 limitado a 20 iterações: {newton(0.5, f, df, show=False, max_iter=20)}")
# Aplicando método de Newton em f para x0 = -0.5
print(f"Aproximação da raiz com x0 = -0.5 limitado a 20 iterações: {newton(-0.5, f, df, show=False, max_iter=20)}")

# Aplicando método de Newton em f para x0 = √5 - 1
print(f"Aproximação da raiz com x0 = √5 - 1 limitado a 20 iterações: {newton(5**.5 - 1, f, df, show=False, max_iter=21)}")
# Aplicando método de Newton em f para x0 = -(√5 - 1)
print(f"Aproximação da raiz com x0 = -(√5 - 1) limitado a 20 iterações: {newton(1 - 5**.5, f, df, show=False, max_iter=21)}")

# Aplicando método de Newton em f para x0 = 1.5
print(f"Aproximação da raiz com x0 = 1.5 limitado a 20 iterações: {newton(1.5, f, df, show=False, max_iter=20)}")
# Aplicando método de Newton em f para x0 = -1.5
print(f"Aproximação da raiz com x0 = -1.5 limitado a 20 iterações: {newton(-1.5, f, df, show=False, max_iter=20)}")

# Aplicando método de Newton em f para x0 = 3.5
print(f"Aproximação da raiz com x0 = 3.5 limitado a 20 iterações: {newton(3.5, f, df, show=False, max_iter=20)}")
# Aplicando método de Newton em f para x0 = -3.5
print(f"Aproximação da raiz com x0 = -3.5 limitado a 20 iterações: {newton(-3.5, f, df, show=False, max_iter=20)}")