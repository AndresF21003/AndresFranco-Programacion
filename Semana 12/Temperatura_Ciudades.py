# Crear la matriz 3D con datos de temperatura
ciudades = ["Quito", "Bogota", "Miami"]
semanas = 3
dias_por_semana = 7

# temperaturas[0] -> Quito
# temperaturas[0][0] -> Temperaturas de Quito, Semana 1
# temperaturas[0][0][0] -> Temperatura de Quito, Semana 1, Día 1
temperaturas = [
    # Temperaturas Quito
    [
        [25, 26, 24, 27, 28, 26, 25],  # Semana 1
        [22, 23, 21, 24, 25, 23, 22],  # Semana 2
        [28, 29, 27, 30, 31, 29, 28]   # Semana 3
    ],
    # Temperaturas Bogota
    [
        [20, 21, 19, 22, 23, 21, 20],  # Semana 1
        [18, 19, 17, 20, 21, 19, 18],  # Semana 2
        [24, 25, 23, 26, 27, 25, 24]   # Semana 3
    ],
    # Temperaturas Miami
    [
        [30, 31, 29, 32, 33, 31, 30],  # Semana 1
        [28, 29, 27, 30, 31, 29, 28],  # Semana 2
        [34, 35, 33, 36, 37, 35, 34]   # Semana 3
    ]
]

print("-- Matriz de temperaturas --")
for i, ciudad in enumerate(ciudades):
    print(f"\n- {ciudad}:")
    for semana in temperaturas[i]:
        print(f"  {semana}")

# Calcular el promedio de temperaturas por semana para cada ciudad
print("")
print("Promedio de temperaturas por ciudad y semana:")

# Bucle para las ciudades
for i, ciudad in enumerate(ciudades):
    print("")
    print(f"Ciudad: {ciudad}")
    # Bucle para las semanas de cada ciudad
    for j in range(semanas):
        # Obtener la lista de temperaturas para la semana actual
        temperaturas_semana = temperaturas[i][j]

        # Calcular el promedio
        promedio = sum(temperaturas_semana) / len(temperaturas_semana)

        # Mostrar el promedio
        print(f"  - Semana {j + 1}: {promedio:.2f}°C")
    print("---------------------------------")
    print("")