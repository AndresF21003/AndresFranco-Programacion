matriz_original = [
    [9, 2, 7],
    [1, 8, 3],
    [5, 4, 6]
]

fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz_original:
    print(fila)

# Bubble Sort para la fila
fila_seleccionada = matriz_original[fila_a_ordenar]
n = len(fila_seleccionada)

for i in range(n):
    for j in range(0, n - i - 1):
        if fila_seleccionada[j] > fila_seleccionada[j + 1]:
            fila_seleccionada[j], fila_seleccionada[j + 1] = fila_seleccionada[j + 1], fila_seleccionada[j]

print("\nMatriz con la fila ordenada:")
for fila in matriz_original:
    print(fila)