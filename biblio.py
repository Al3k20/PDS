class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}"

# Solicita ao usuário os detalhes do livro
titulo = input("Digite o título do livro: ")
autor = input("Digite o nome do autor: ")
paginas = input("Digite o número de páginas: ")

# Cria uma instância da classe Livro
livro = Livro(titulo, autor, paginas)

# Exibe a descrição formatada do livro
print("\nDetalhes do livro:")
print(livro)
