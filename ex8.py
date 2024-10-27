# Matriz fornecida
matriz = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]

# Inicializando a lista para somas das linhas
soma_linhas = [0] * len(matriz)
soma_colunas = [0] * len(matriz)
soma_diagonal_p = 0
soma_diagonal_s = 0


for l in range(len(matriz)):
    soma_linhas[l]= sum(matriz[l])
    for c in range(len(matriz[l])):
        soma_colunas[c] += matriz[l][c]
        if l == c: 
            soma_diagonal_p += matriz[l][c]
        if l + c == len(matriz) - 1:
            soma_diagonal_s += matriz[l][c]

print(soma_linhas)
print(soma_colunas)
print(soma_diagonal_p)
print(soma_diagonal_s)