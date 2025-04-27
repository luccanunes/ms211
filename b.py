import math

def f(x, b):
    return b - 1/x


def derivada_f(x): 
    return 1/(x*x)

def newton(x0):
    ant = 0
    while abs(x0-ant)>0.0000001:
        print(x0)
        ant = x0
        x0 = x0 - f(x0, math.pi)/derivada_f(x0)
    print(x0)

print("Executando Newton com x0 = 0.5")
newton(0.5)
print("Executando Newton com x0 = 0.7")
newton(0.7)


