# Inicializando uma matriz 5x5 com todos os elementos iguais a 0
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Preenchendo a diagonal principal com 1
for i in range(5):
    matriz[i][i] = 1

# Exibindo a matriz resultante
print("Matriz 5x5 com diagonal principal igual a 1 e demais elementos iguais a 0:")
for linha in matriz:
    print(linha)
