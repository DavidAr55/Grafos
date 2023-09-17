class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_edge(self, start, end, weight):
        self.vertices.add(start)
        self.vertices.add(end)
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append((end, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        shortest_path = {}
        unvisited_vertices = self.vertices.copy()

        while unvisited_vertices:
            current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
            unvisited_vertices.remove(current_vertex)

            for neighbor, weight in self.edges.get(current_vertex, []):
                potential_route = distances[current_vertex] + weight

                if potential_route < distances[neighbor]:
                    distances[neighbor] = potential_route
                    shortest_path[neighbor] = current_vertex

        return distances, shortest_path

# Crear un grafo y agregar las aristas desde tu conjunto de datos
grafo = Graph()

# Agregar aristas desde tu conjunto de datos (usando un subconjunto de tus datos)
grafo.add_edge("Austria", "Belgium", 112800000)
grafo.add_edge("Austria", "Germany", 112800000)

# Calcular la distancia más corta desde un punto de inicio
start_country = "Austria"
distances, shortest_path = grafo.dijkstra(start_country)

# Imprimir resultados
for country, distance in distances.items():
    if distance == float('infinity'):
        print(f"No hay ruta desde {start_country} a {country}")
    else:
        path = []
        current_country = country
        while current_country in shortest_path:
            path.insert(0, current_country)
            current_country = shortest_path[current_country]
        path.insert(0, start_country)
        print(f"Distancia desde {start_country} a {country}: {distance}")
        print(f"Ruta más corta: {' -> '.join(path)}")
