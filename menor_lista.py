# Função para encontrar o maior número na lista
def encontrar_maior(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    maior = lista[0]  # Inicializa com o primeiro elemento
    for numero in lista[1:]:
        if numero > maior:  # Compara se o número atual é MAIOR
            maior = numero  # Atualiza o MAIOR
    return maior

# Função para encontrar o menor número na lista
def encontrar_menor(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia")
    menor = lista[0]  # Inicializa com o primeiro elemento
    for numero in lista[1:]:
        if numero < menor:  # Compara se o número atual é MENOR
            menor = numero  # Atualiza o MENOR
    return menor

if __name__ == "__main__":
    # Lista de números
    numeros = [15, 42, 7, 98, 23, 5, 67]

    # Encontrando e exibindo o maior número na lista
    maior_numero = encontrar_maior(numeros)
    print("Maior número na lista:", maior_numero)

    # Encontrando e exibindo o menor número na lista
    menor_numero = encontrar_menor(numeros)
    print("Menor número na lista:", menor_numero)
