# a) Lista pré-definida com 10 títulos de livros
livros = [
    "Dom Casmurro",
    "O Pequeno Príncipe",
    "Cem Anos de Solidão",
    "Grande Sertão: Veredas",
    "O Senhor dos Anéis",
    "Memórias Póstumas de Brás Cubas",
    "1984",
    "A Revolução dos Bichos",
    "Orgulho e Preconceito",
    "O Código Da Vinci"
]

# b) Solicita a palavra-chave ao usuário
palavra_chave = input("Digite uma palavra ou sequência de caracteres para buscar nos títulos: ").lower()

# c) Filtra os títulos com base na palavra-chave (ignora maiúsculas/minúsculas)
resultados = [livro for livro in livros if palavra_chave in livro.lower()]

# d) Exibe o resultado da busca
if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print(f"- {titulo}")
else:
    print("\nNenhum título corresponde à sua busca.")
