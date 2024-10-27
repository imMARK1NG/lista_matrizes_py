# Respostas dos alunos (5x10)
matriz_respostas = [
    ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
    ['b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c'],
    ['c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'],
    ['d', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a'],
    ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
]

# Gabarito (10)
gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']

# Calculando a pontuação de cada aluno
resultado = [sum(1 for j in range(10) if matriz_respostas[i][j] == gabarito[j]) for i in range(5)]

# Exibindo o resultado
print("Pontuação de cada aluno:", resultado)
