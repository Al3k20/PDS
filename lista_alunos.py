# Lista de alunos com nome e nota
alunos = [
    {"nome": "Carlos", "nota": 8.5},
    {"nome": "Ana", "nota": 9.2},
    {"nome": "Bruno", "nota": 7.8},
    {"nome": "Daniel", "nota": 6.9},
    {"nome": "Eduarda", "nota": 9.5}
]

# Ordenando a lista pelo nome (modifica a lista original)
alunos.sort(key=lambda x: x["nome"])

print("Lista ordenada por nome:")
for aluno in alunos:
    print(aluno)

# Ordenando por nota em ordem decrescente (gera uma nova lista)
alunos_ordenados_por_nota = sorted(alunos, key=lambda x: x["nota"], reverse=True)

print("\nLista ordenada por nota (decrescente):")
for aluno in alunos_ordenados_por_nota:
    print(aluno)
