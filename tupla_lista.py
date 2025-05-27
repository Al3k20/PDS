class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista dinâmica para armazenar os livros

    def adicionar_livro(self, titulo: str, autor: str, ano: int):
        livro = (titulo, autor, ano)  # Criando uma tupla imutável
        self.livros.append(livro)  # Adicionando à lista dinâmica
        print(f'Livro adicionado: {livro}')

    def consultar_livros(self):
        print("\nColeção de livros:")
        for livro in self.livros:
            print(livro)

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
biblioteca.adicionar_livro("1984", "George Orwell", 1949)
biblioteca.adicionar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

# Consultando livros armazenados
biblioteca.consultar_livros()
