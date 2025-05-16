import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
retorno_medio_anual = 0.07
desvio_padrao_anual = 0.20
simulacoes = 100
valor_inicial = 10000
passos = anos * 12  # Considerando períodos mensais

# Gerar múltiplas trajetórias
trajetorias = np.zeros((simulacoes, passos))
for i in range(simulacoes):
    retornos = np.random.normal(retorno_medio_anual / 12, desvio_padrao_anual / np.sqrt(12), passos)
    trajetoria = valor_inicial * np.cumprod(1 + retornos)
    trajetorias[i] = trajetoria

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(trajetorias.T, alpha=0.2)  # Trajetórias individuais com baixa opacidade
plt.plot(np.mean(trajetorias, axis=0), color='black', linewidth=2, label="Média das simulações")
plt.xlabel("Meses")
plt.ylabel("Valor da Carteira")
plt.title("Simulação de Monte Carlo para Carteira de Investimentos")
plt.legend()
plt.show()
