gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']

alunos = [
    (123, ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']),
    (456, ['a', 'c', 'b', 'd', 'e', 'a', 'd', 'b', 'c', 'e']),
    (789, ['e', 'b', 'c', 'a', 'd', 'e', 'a', 'b', 'c', 'd'])
]

for matricula, respostas in alunos:
    nota = sum(1 for i in range(10) if respostas[i] == gabarito[i])
    print(f"Matrícula: {matricula}, Nota: {nota}")
