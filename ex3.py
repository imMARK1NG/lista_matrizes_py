matriz = [[0 for _ in range(4)] for _ in range(4)]

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = l * c

for tab in matriz:
    print(tab)