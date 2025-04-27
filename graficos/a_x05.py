import matplotlib.pyplot as plt

# Given data
x_values = [0, 1, 2, 3, 4]
y_values = [0.5, 0.6842105263157895, 0.7240998948362555, 0.724491938691257, 0.7244919590005156]

# Create a plot
plt.plot(x_values, y_values, marker='o', color='b', linestyle='-', label='Data')

# Adding labels and title
plt.xlabel('Número da iteração')
plt.ylabel('valor da iteração x')
plt.title('Método de Newton')

# Show legend
plt.legend()

# Show the plot
plt.show()

