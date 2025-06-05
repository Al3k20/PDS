# Solicita ao usuário que insira os nomes, separados por vírgula
nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

# Remove espaços extras
nomes = [nome.strip() for nome in nomes]

# Itera sobre a lista com enumerate e exibe os nomes com seus índices
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
