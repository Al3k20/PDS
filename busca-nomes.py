# Lista com pelo menos 8 nomes
nomes = ["Ana", "Carlos", "Fernanda", "Bruno", "Isabela", "João", "Tatiane", "Gabriel"]

# Solicita ao usuário uma letra ou sequência
sequencia = input("Digite uma letra ou sequência para buscar nos nomes: ").lower()

# Filtra os nomes que contêm a sequência (sem diferenciar maiúsculas/minúsculas)
nomes_filtrados = [nome for nome in nomes if sequencia in nome.lower()]

# Exibe o resultado
if nomes_filtrados:
    print("\nNomes encontrados:")
    for nome in nomes_filtrados:
        print(f"- {nome}")
else:
    print("\nNenhum nome foi encontrado com essa sequência.")
