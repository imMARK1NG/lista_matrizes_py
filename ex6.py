# Inicializando as matrizes 2x2
tam = 2
matriz1 = [[0] * tam for _ in range(tam)]
matriz2 = [[0] * tam for _ in range(tam)]
matriz3 = [[0] * tam for _ in range(tam)]

# Lendo os elementos da matriz1
print("Elementos da matriz 1:")
for l in range(tam):
    for c in range(tam):
        matriz1[l][c] = int(input(f"Digite os elementos [{l}, {c}] da matriz1: "))

# Lendo os elementos da matriz2
print("\nElementos da matriz 2:")
for l in range(tam):
    for c in range(tam):
        matriz2[l][c] = int(input(f"Digite os elementos [{l}, {c}] da matriz2: "))

# Construindo a matriz3 com os maiores valores de cada posição
for l in range(tam):
    for c in range(tam):
        matriz3[l][c] = max(matriz1[l][c], matriz2[l][c])

# Exibindo a matriz3
print("\nDados da matriz 3:")
for linha in matriz3:
    print(linha)
