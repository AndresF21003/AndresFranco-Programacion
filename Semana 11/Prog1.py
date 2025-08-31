mi_matriz = [
    [1, 5, 9],
    [4, 8, 2],
    [7, 3, 6]
]

valor_a_buscar = 8
encontrado = False

# Búsqueda
for fila_index in range(len(mi_matriz)):
    for col_index in range(len(mi_matriz[fila_index])):
        if mi_matriz[fila_index][col_index] == valor_a_buscar:
            print(f"El valor {valor_a_buscar} se encontró en la posición: ({fila_index}, {col_index})")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")