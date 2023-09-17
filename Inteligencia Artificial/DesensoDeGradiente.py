import numpy as np

# Función de costo de ejemplo (puedes cambiarla según tus necesidades)
def costo(x):
    return x[0]**2 + x[1]**2 + x[2]**2

# Gradiente de la función de costo (derivadas parciales)
def gradiente(x):
    return [2 * x[0], 2 * x[1], 2 * x[2]]

# Tasa de aprendizaje (ajusta este valor según tus necesidades)
tasa_aprendizaje = 0.1

# Número de iteraciones
num_iteraciones = 100

# Valor inicial de los parámetros (3 dimensiones)
parametros = [1.0, 2.0, 3.0]

# Lista para almacenar el historial de valores de costo
historial_costo = []

# Descenso de gradiente
for i in range(num_iteraciones):
    # Calcula el valor actual de la función de costo
    costo_actual = costo(parametros)
    
    # Almacena el costo en el historial
    historial_costo.append(costo_actual)
    
    # Calcula el gradiente en el punto actual
    gradiente_actual = gradiente(parametros)
    
    # Actualiza los parámetros usando el descenso de gradiente
    for j in range(len(parametros)):
        parametros[j] -= tasa_aprendizaje * gradiente_actual[j]
    
    # Muestra información en cada iteración
    print(f"Iteración {i + 1}: Parámetros = {parametros}, Costo = {costo_actual}")

# Resultado final
print("\nResultado final:")
print(f"Parámetros finales = {parametros}")
print(f"Costo final = {costo_actual}")
