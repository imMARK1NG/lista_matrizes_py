import random

# Gerando números únicos de 0 a 99
numeros_bingo = random.sample(range(100), 25)

# Transformando a lista em uma matriz 5x5
cartela = [numeros_bingo[i*5:(i+1)*5] for i in range(5)]

# Exibindo a cartela
print("Cartela de Bingo:")
for linha in cartela:
    print(linha)
