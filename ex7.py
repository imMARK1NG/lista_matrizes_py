# Inicializando a matriz 3x3
tam = 3
matriz = [[0] * tam for _ in range(tam)]

# Lendo os elementos da matriz
print("Digite os elementos da matriz 3x3:")
for l in range(tam):
    for c in range(tam):
        matriz[l][c] = int(input(f"Elemento [{l}][{c}]: "))

# a) Soma dos números ímpares fornecidos
soma_impares = sum(matriz[l][c] for l in range(tam) for c in range(tam) if matriz[l][c] % 2 != 0)

# b) Soma de cada uma das 3 colunas
soma_colunas = [sum(matriz[l][c] for l in range(tam)) for c in range(tam)]

# c) Soma de cada uma das 3 linhas
soma_linhas = [sum(matriz[l]) for l in range(tam)]


for linha in matriz:
    print("\n",linha)

# Exibindo os resultados
print(f"\nSoma dos números ímpares: {soma_impares}")
print(f"Soma das colunas: {soma_colunas}")
print(f"Soma das linhas: {soma_linhas}")
