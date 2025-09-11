def calcular_promedio_ciudades(datos_temperatura, ciudades):
    """
    Calcula la temperatura promedio de cada ciudad a lo largo de todas las semanas.

    Parámetros:
    - datos_temperatura (list): Una matriz 3D con las temperaturas.
      La estructura es: [Ciudad [Semana [Día]]].
    - ciudades (list): Una lista de nombres de las ciudades, en el mismo orden que en datos_temperatura.

    Retorna:
    - dict: Un diccionario donde las claves son los nombres de las ciudades y los valores
      son sus respectivas temperaturas promedio.
    """
    promedios_por_ciudad = {}

    # Bucle para recorrer cada ciudad en la matriz de datos
    for i, ciudad in enumerate(ciudades):

        # Obtener todas las temperaturas para la ciudad actual.
        # temperatures_ciudad es una lista que contiene las listas de temperaturas de cada semana.
        temperaturas_ciudad = datos_temperatura[i]

        # Calcular el promedio de todas las temperaturas de la ciudad.
        # Primero, aplanar la lista de listas (matriz de semanas) para tener todas las temperaturas en una sola lista.
        todas_las_temperaturas = [temp for semana in temperaturas_ciudad for temp in semana]

        # Calcular el promedio total de la ciudad.
        if todas_las_temperaturas:  # Asegura que no se divida por cero si la lista está vacía
            promedio_ciudad = sum(todas_las_temperaturas) / len(todas_las_temperaturas)
            promedios_por_ciudad[ciudad] = promedio_ciudad
        else:
            promedios_por_ciudad[ciudad] = 0.0  # Asigna 0.0 si no hay datos

    return promedios_por_ciudad


# Datos de ejemplo
ciudades = ["Quito", "Bogotá", "Miami"]
# Matriz de temperaturas para 3 ciudades y 4 semanas
temperaturas_3d = [
    # Quito
    [
        [15, 16, 14, 15, 17, 16, 15],  # Semana 1
        [12, 13, 11, 14, 15, 13, 12],  # Semana 2
        [18, 19, 17, 20, 21, 19, 18],  # Semana 3
        [16, 17, 15, 18, 19, 17, 16]  # Semana 4
    ],
    # Bogotá
    [
        [17, 18, 16, 19, 20, 18, 17],
        [15, 16, 14, 17, 18, 16, 15],
        [21, 22, 20, 23, 24, 22, 21],
        [18, 19, 17, 20, 21, 19, 18]
    ],
    # Miami
    [
        [28, 29, 27, 30, 31, 29, 28],
        [26, 27, 25, 28, 29, 27, 26],
        [32, 33, 31, 34, 35, 33, 32],
        [29, 30, 28, 31, 32, 30, 29]
    ]
]

# Llamar a la función y guardar el resultado
promedios_finales = calcular_promedio_ciudades(temperaturas_3d, ciudades)

# Mostrar los resultados
print("Temperaturas promedio por ciudad:")
for ciudad, promedio in promedios_finales.items():
    print(f"  - {ciudad}: {promedio:.2f}°C")