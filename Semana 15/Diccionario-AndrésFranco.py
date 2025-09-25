# Crear un diccionario
informacion_personal = {
    "nombre": "Eduardo Franco",
    "edad": 23,
    "ciudad": "Estudiante",
    "profesion": "Ingeniero"
}

# Imprimir cada clave y valor en una nueva línea
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# 2. Acceder y Modificar Valores (por teclado)
clave_modificar = input("Ingresa la clave que deseas modificar (ej. 'ciudad'): ")
if clave_modificar in informacion_personal:
    nuevo_valor = input(f"Ingresa el nuevo valor para '{clave_modificar}': ")
    informacion_personal[clave_modificar] = nuevo_valor
    print(f"El valor de '{clave_modificar}' ha sido modificado.")
else:
    print(f"La clave '{clave_modificar}' no existe en el diccionario.")

# 3. Verificar Existencia de Claves (por teclado)
clave_verificar = input("Ingresa la clave que deseas verificar (ej. 'telefono'): ")
if clave_verificar in informacion_personal:
    print(f"La clave '{clave_verificar}' ya existe en el diccionario.")
else:
    print(f"La clave '{clave_verificar}' no existe. Por favor, ingresa un valor para agregarla.")
    nuevo_valor_existencia = input(f"Ingresa el valor para '{clave_verificar}': ")
    informacion_personal[clave_verificar] = nuevo_valor_existencia
    print(f"La clave '{clave_verificar}' ha sido agregada con el valor '{nuevo_valor_existencia}'.")

# 4. Eliminar una Clave (por teclado)
clave_eliminar = input("Ingresa la clave que deseas eliminar (ej. 'edad'): ")
if clave_eliminar in informacion_personal:
    del informacion_personal[clave_eliminar]
    print(f"La clave '{clave_eliminar}' ha sido eliminada del diccionario.")
else:
    print(f"La clave '{clave_eliminar}' no existe en el diccionario.")


# 5. Imprimir el diccionario final
print("\n--- Diccionario Final ---")
print(informacion_personal)