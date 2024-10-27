linha = int(input("Digite o tamnhao da linha:"))
coluna = int(input("Digite o tamanho da coluna:"))

matriz = [0] * linha

for l in range(len(matriz)):
        matriz[l] = [0] * coluna

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Digite os elementos da matriz:"))                

maior_valor = max(max(maior) for maior in matriz)

posi = (0, 0)

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] == maior_valor:
            posi = (l, c)


for linha in matriz:
     print(linha)

print(f"o valor maior da matriz é: {maior_valor}")
print(f"a posição do maior valor na matriz é: {posi}")
