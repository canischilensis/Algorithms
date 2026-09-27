import heapq

# Definimos el grafo dirigido como un diccionario de adyacencia:
#  vértice -> lista de tuplas (vecino, peso)
graph = {
    "A": [("F", 5), ("B", 9)],
    "F": [("G", 9), ("B", 12)],
    "B": [("I", 8), ("C", 2)],
    "G": [("H", 8), ("I", 3), ("D", 5)],
    "H": [("E", 28), ("D", 17)],
    "I": [("C", 7)],      # desde I a C
    "C": [("D", 3)],
    "D": [("E", 11)],
    "E": []               # destino final, sin salidas
}

def dijkstra(graph, start, goal):
    """Devuelve (distancia, camino) más corto desde start hasta goal."""
    pq = [(0, start, [])]           # (distancia acumulada, nodo actual, camino hasta aquí)
    visited = set()
    
    while pq:
        dist, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        
        if node == goal:
            return dist, path
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (dist + weight, neighbor, path))
    
    return float("inf"), []         # no hay camino

# (1) Camino más corto A → G
dist_AG, path_AG = dijkstra(graph, "A", "G")

# (2) Camino más corto G → E
dist_GE, path_GE = dijkstra(graph, "G", "E")

# (3) Unimos ambos caminos (evitando repetir el vértice G)
total_distance = dist_AG + dist_GE
full_path = path_AG + path_GE[1:]

# Mostramos los resultados
print("Camino más corto A → G : ", " → ".join(path_AG), f"({dist_AG} min)")
print("Camino más corto G → E : ", " → ".join(path_GE), f"({dist_GE} min)")
print("Ruta completa A → G → E:", " → ".join(full_path), f"({total_distance} min)")
