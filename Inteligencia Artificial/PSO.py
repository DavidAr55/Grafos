import random

# Función de optimización de ejemplo: f(x, y, z) = x^2 + y^2 + z^2
def objective_function(x, y, z):
    return x**2 + y**2 + z**2

# Parámetros del algoritmo PSO
num_particles = 30  # Número de partículas en el enjambre
max_iterations = 100  # Número máximo de iteraciones
c1 = 1.5  # Coeficiente de influencia cognitiva
c2 = 1.5  # Coeficiente de influencia social
w = 0.7  # Peso de la inercia
bounds = [(-10, 10), (-10, 10), (-10, 10)]  # Límites para las coordenadas (x, y, z)

# Inicialización de partículas aleatorias
particles = []
for _ in range(num_particles):
    x = random.uniform(bounds[0][0], bounds[0][1])
    y = random.uniform(bounds[1][0], bounds[1][1])
    z = random.uniform(bounds[2][0], bounds[2][1])
    velocity = [0, 0, 0]
    particles.append((x, y, z, objective_function(x, y, z), velocity))

# Mejor posición global inicial
global_best_position = particles[0][:3]
global_best_value = particles[0][3]

# Algoritmo PSO
for iteration in range(max_iterations):
    for i, particle in enumerate(particles):
        x, y, z, fitness, velocity = particle
        
        # Actualizar la velocidad
        r1 = random.random()
        r2 = random.random()
        new_velocity = [
            w * velocity[0] + c1 * r1 * (global_best_position[0] - x) + c2 * r2 * (global_best_position[0] - x),
            w * velocity[1] + c1 * r1 * (global_best_position[1] - y) + c2 * r2 * (global_best_position[1] - y),
            w * velocity[2] + c1 * r1 * (global_best_position[2] - z) + c2 * r2 * (global_best_position[2] - z)
        ]
        
        # Actualizar la posición
        new_x = x + new_velocity[0]
        new_y = y + new_velocity[1]
        new_z = z + new_velocity[2]
        
        # Aplicar límites
        new_x = max(min(new_x, bounds[0][1]), bounds[0][0])
        new_y = max(min(new_y, bounds[1][1]), bounds[1][0])
        new_z = max(min(new_z, bounds[2][1]), bounds[2][0])
        
        # Calcular el valor de la nueva posición
        new_fitness = objective_function(new_x, new_y, new_z)
        
        # Actualizar la posición y la mejor posición personal
        particles[i] = (new_x, new_y, new_z, new_fitness, new_velocity)
        
        if new_fitness < fitness:
            particles[i] = (new_x, new_y, new_z, new_fitness, new_velocity)
            
            # Actualizar la mejor posición global si es necesario
            if new_fitness < global_best_value:
                global_best_position = (new_x, new_y, new_z)
                global_best_value = new_fitness

    print(f"Iteración {iteration + 1}: Valor óptimo = {global_best_value}")

print("Mejor solución encontrada:")
print(f"Coordenadas: {global_best_position}")
print(f"Valor óptimo: {global_best_value}")
