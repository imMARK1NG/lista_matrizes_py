linha = int(input("Digite a quantidade de linhas:"))
coluna = int(input("Digite o tamanho da coluna:"))

matriz = [0] * linha

for l in range(len(matriz)):
    matriz[l] = [0] * coluna

for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l][c] = int(input(f"Informe os elementos da matriz:"))

contador = 0

for l in range(len(matriz)):
    for c in range(len(matriz)):
        if matriz[l][c] >= 10:
            contador = contador + 1

print(f"A {contador} valores maiores que 10 na matriz.")