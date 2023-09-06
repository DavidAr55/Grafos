# Definimos un grafo como un diccionario donde las claves son los nodos y los valores son las listas de nodos a los que están conectados.
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función para agregar una conexión entre dos nodos
def agregar_conexion(grafo, nodo1, nodo2):
    grafo[nodo1].append(nodo2)
    grafo[nodo2].append(nodo1)

# Ejemplo de cómo agregar una conexión
agregar_conexion(grafo, 'A', 'D')

# Imprimir el grafo
for nodo, conexiones in grafo.items():
    print(f'{nodo}: {conexiones}')