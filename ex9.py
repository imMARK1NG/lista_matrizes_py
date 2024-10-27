matriz = [
    [0, 15 , 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
]

cidade1 = input("Digite o número da primeira cidade (0-4): ")
cidade2 = input("Digite o número da segunda cidade (0-4): ")

# Converter entrada para índices
cidade1 = int(cidade1)
cidade2 = int(cidade2)

# Encontrar a distância entre as cidades
matriz = matriz[cidade1][cidade2]

print(matriz)