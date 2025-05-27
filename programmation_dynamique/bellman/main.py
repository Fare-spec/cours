def bellman_ford(graphe, sommet):
    distance = {sommet: float("inf") for sommet in graphe}
    distance[sommet] = 0

    for i in range(len(graphe) - 1):
        for u in graphe:
            for v, coef in graphe[u]:
                if distance[u] + coef < distance[v]:
                    distance[v] = distance[u] + coef

    for u in graphe:
        for v, coef in graphe[u]:
            if distance[u] + coef < distance[v]:
                raise ValueError("Cycle négatif détecté")

    return distance


if __name__ == "__main__":
    graphe = {
        "A": [("G", 8), ("H", 4)],
        "G": [("H", 1), ("L", 2)],
        "H": [("L", 5), ("E", 7)],
        "L": [("E", -2)],
        "E": [],
    }
    distances = bellman_ford(graphe, "A")
    print(distances)
