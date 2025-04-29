import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 1/x 

def f2(x):
	return 1 + x**3

x = np.linspace(-1, 1, 400)  # range from -10 to 10
y1 = f1(x) 
y2 = f2(x)

plt.plot(x, y1, label='f(x) = 1/x')
plt.title("Problema 1")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y2, label='f(x) = x³ + 1')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.show()
