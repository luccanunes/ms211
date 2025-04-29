import matplotlib.pyplot as plt

# Dados da Tabela 1 (Fórmula Simplificada)
k1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
xk1 = [1, -2.0, 4, -8, 16, -32, 64, -128, 256, -512]

# Gráfico para a Tabela 1
plt.figure(figsize=(8, 5))
plt.plot(k1, xk1, marker="o", linestyle="-", color="b", label="$x_0 = 1$")
plt.title("Valores de $x_k$ para $x_0 = 1$ com a fórmula simplificada", fontsize=12)
plt.xlabel("$k$ (Iterações)", fontsize=10)
plt.ylabel("$x_k$", fontsize=10)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Linha de referência no eixo y = 0
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend()
plt.savefig("grafico_tabela_xk_simplificada.png")  # Salva como arquivo
plt.clf()  # Limpa a figura

# Dados da Tabela 2
k2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
xk2 = [1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0]

# Gráfico para a Tabela 2
plt.figure(figsize=(8, 5))
plt.plot(k2, xk2, marker="o", linestyle="-", color="b", label="$x_0 = 1$")
plt.title("Valores de $x_k$ para $x_0 = 1$", fontsize=12)
plt.xlabel("$k$ (Iterações)", fontsize=10)
plt.ylabel("$x_k$", fontsize=10)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Linha de referência no eixo y = 0
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend()
plt.savefig("grafico_tabela_xk_alternada.png")  # Salva como arquivo

print("Os gráficos foram salvos como 'grafico_tabela_xk_simplificada.png' e 'grafico_tabela_xk_alternada.png'")
