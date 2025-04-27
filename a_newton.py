import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 1 + x**3 - 1/x
def f_linha(x): 
	return 3*x**2 + 1/(x**2)

def newton_lucca(x0, f, df, show=false, max_iter = 1000, eps = 1e-10):
    ant = 0
    i = 0
    while abs(x0 - ant) > eps and i < max_iter:
        if show:
            print(x0)
        ant = x0
        x0 = x0 - f(x0)/df(x0)
        i += 1
    return x0

print(f(newton_lucca(0.1, f, f_linha, True, eps=1e-9)))
