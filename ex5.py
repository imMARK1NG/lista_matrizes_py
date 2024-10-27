tam = 2
matriz = [0] * tam
for l in range(len(matriz)):
    matriz[l] = [0] * tam

for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l][c] = int(input("Digite os elementos da matriz: "))

pos = (-1, -1)  # Inicializa a posição como inválida
valor = int(input("Digite o valor que você deseja buscar na matriz: "))
encontrado = False

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] == valor:
            pos = (l, c)
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print("Valor inválido")

for linha in matriz:
    print(linha)
print(f"O valor selecionado foi: {valor}")
print(f"A posição do valor selecionado foi: {pos}")
