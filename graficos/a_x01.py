import matplotlib.pyplot as plt

# Iteration steps
x_values = list(range(7))  # [0, 1, 2, 3, 4, 5, 6]

# Corresponding values
y_values = [
    0.1,
    0.18996301109667102,
    0.34299487543519513,
    0.5548025139560337,
    0.7062019827079513,
    0.7244316965740877,
    0.724491958523868
]

# Plotting the data
plt.plot(x_values, y_values, marker='o', linestyle='-', color='green', label='Newton Iterations')

# Labels and title
plt.xlabel("Iteração")
plt.ylabel("Valor de x")
plt.title("Evolução da Solução pelo Método de Newton")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

