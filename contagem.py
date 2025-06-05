# Solicita ao usuário uma entrada
entrada = input("Digite uma frase ou uma lista de itens separados por vírgula: ")

# Verifica se a entrada contém vírgulas (indicando uma lista)
if "," in entrada:
    lista = entrada.split(",")  # Se
