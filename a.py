import numpy as np
from newton import newton

def f(x):
	return 1 + x**3 - 1/x
def f_linha(x): 
	return 3*x**2 + 1/(x**2)

print(f(newton(0.1, f, f_linha, show=True, eps=1e-9)))
