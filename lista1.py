# Recebe um número inteiro positivo n
n = int(input("Digite um número inteiro positivo: "))

# Cria uma lista para armazenar os números
lista = []

# Lê n números inteiros e os adiciona à lista
print(f"Digite {n} números inteiros:")
for _ in range(n):
    numero = int(input())
    lista.append(numero)

# Recebe um número inteiro x
x = int(input("Digite o número a ser verificado: "))

# Verifica se x pertence à lista
if x in lista:
    print(f"{x} pertence à lista.")
else:
    print(f"{x} não pertence à lista.")
