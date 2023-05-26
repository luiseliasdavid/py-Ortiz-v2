matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]


for i, fila in enumerate(matriz):
    for j, pos in enumerate(fila):
        if pos % 2 == 0:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1

print(matriz)