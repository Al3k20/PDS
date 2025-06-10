# Função para encontrar o menor número na lista
def encontrar_menor(lista):
    menor = lista[0] # Inicializa com o primeiro elemento
    for numero in lista:
        if numero < menor: # Compara se o número atual é MENOR
            menor = numero # Atualiza o MENOR
    return menor
    
# Encontrando e exibindo o menor número na lista
menor_numero = encontrar_menor(numeros)
print("Menor número na lista:", menor_numero)
