import heapq

# Implementación del algoritmo de Dijkstra
def dijkstra(graph, start, end):
    # Inicializar las distancias de todos los nodos como infinito, excepto el nodo de inicio
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Crear una cola de prioridad para almacenar los nodos a visitar
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Si ya hemos procesado este nodo con una distancia menor, lo ignoramos
        if current_distance > distances[current_vertex]:
            continue
        
        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_vertex].items():
            # Calcular la distancia a través del nodo actual al vecino
            distance = current_distance + weight
            # Si encontramos un camino más corto hacia el vecino, actualizamos la distancia
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Agregamos el vecino a la cola de prioridad para explorar sus vecinos
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Definir el grafo
G = {
    'A': {'C': 8, 'E': 3, 'F': 4},
    'B': {'C': 6, 'D': 2, 'H': 7},
    'C': {'A': 8, 'B': 6, 'F': 1, 'G': 5},
    'D': {'B': 2, 'I': 2},
    'E': {'A': 3},
    'F': {'A': 4, 'C': 1},
    'G': {'C': 5, 'I': 3},
    'H': {'B': 7, 'I': 3},
    'I': {'D': 2, 'G': 3, 'H': 3}
}

start_node = 'E'
end_node = 'H'

# Ejecutar el algoritmo de Dijkstra
shortest_distances = dijkstra(G, start_node, end_node)
shortest_distance = shortest_distances[end_node]

# Imprimir el resultado
print(f"La ruta más corta desde '{start_node}' hasta '{end_node}' es: {shortest_distance}")