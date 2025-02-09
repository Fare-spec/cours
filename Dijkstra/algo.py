# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('D', 3), ('E', 8)],
    'D': [('E', 4), ('F', 11)],
    'E': [('G', 6)],
    'F': [('G', 2)],
    'G': []
}

p = {}

def chemin(predecesseur, debut, fin):
    chemin = []
    courant = fin
    while courant != debut:
        chemin.insert(0, courant)
        courant = predecesseur.get(courant)
        if courant is None:
            return None
    chemin.insert(0, debut)
    return chemin


def initialisation(G, debut):
    distances = {key: float('inf') for key in G}
    distances[debut] = 0
    return distances


def trouve_min(Q, distances):
    mini = float('inf')
    sommet = None
    for s in Q:
        if distances[s] < mini:
            mini = distances[s]
            sommet = s
    return sommet

def poid(s1, s2):
    for voisin, poids in graph[s1]:
        if voisin == s2:
            return poids
    return float('inf')

def distances_update(s1, s2, distances, predecesseur):
    poids = poid(s1, s2)
    if distances[s2] > distances[s1] + poids:
        distances[s2] = distances[s1] + poids
        predecesseur[s2] = s1

def dijkstra(G, debut='A'):
    distances = initialisation(G, debut)
    predecesseur = {}
    Q = set(G.keys())

    while Q:
        s1 = trouve_min(Q, distances)
        if s1 is None:
            break
        Q.remove(s1)

        for voisin, _ in G[s1]:
            if voisin in Q:
                distances_update(s1, voisin, distances, predecesseur)

    return distances, predecesseur

if __name__ == "__main__":
    distances, predecesseur = dijkstra(graph, 'A')
    print("Distances depuis A :", distances)
    print("Chemin le plus court de A à G :", chemin(predecesseur, 'A', 'G'))
