import functools

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):
    return (a.nota > b.nota) - (a.nota < b.nota)

# Criando lista de alunos a partir da entrada do usuário
alunos = []
for _ in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = int(input("Digite a nota do aluno: "))
    alunos.append(Aluno(nome, nota))

# Ordenando a lista de alunos
alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))

print("Alunos ordenados por nota:")
for aluno in alunos_ordenados:
    print(aluno)
