# Lista pré-definida com nomes de cidades
cidades = [
    "Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte",
    "Porto Alegre", "Recife", "Salvador", "Brasília"
]

# Solicita ao usuário uma letra ou sequência de caracteres
filtro = input("Digite uma letra ou sequência de caracteres para buscar nas cidades: ").lower()

# Filtra as cidades que contêm o texto fornecido (ignorando maiúsculas/minúsculas)
cidades_filtradas = [cidade for cidade in cidades if filtro in cidade.lower()]

# Exibe o resultado
if cidades_filtradas:
    print("\nCidades encontradas:")
    for cidade in cidades_filtradas:
        print(f"- {cidade}")
else:
    print("\nNenhuma cidade corresponde ao critério de busca.")
