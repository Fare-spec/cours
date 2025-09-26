def dijkstra(graph: dict, start: any) -> tuple:
    """
    L'algorithme de Dijkstra pour trouver les plus courts chemins depuis un sommet de départ.

    Args:
        graph (dict): Le graphe à parcourir sous forme de dictionnaire, où les clés sont les sommets
                      et les valeurs sont des listes de tuples (voisin, poids).
        start (any): Le sommet de départ.

    Returns:
        tuple: Un tuple contenant deux dictionnaires :
               - Le premier associe à chaque sommet la distance minimale depuis le sommet de départ.
               - Le second associe à chaque sommet (sauf le départ) son prédécesseur sur le chemin le plus court.

    Exemples:
    >>> graph = {
    ...     'A': [('B', 4), ('C', 2)],
    ...     'B': [('C', 5), ('D', 10)],
    ...     'C': [('D', 3), ('E', 8)],
    ...     'D': [('E', 4), ('F', 11)],
    ...     'E': [('G', 6)],
    ...     'F': [('G', 2)],
    ...     'G': []
    ... }
    >>> distances, predecesseur = dijkstra(graph, 'A')
    >>> distances['A']
    0
    >>> distances['B']
    4
    >>> distances['C']
    2
    >>> distances['D']
    5
    >>> distances['E']
    9
    >>> distances['F']
    16
    >>> distances['G']
    15
    >>> predecesseur['B']
    'A'
    >>> predecesseur['C']
    'A'
    >>> predecesseur['D']
    'C'
    >>> predecesseur['E']
    'D'
    >>> predecesseur['F']
    'D'
    >>> predecesseur['G']
    'E'
    """
    distances, predecesseur, unvisited = {}, {}, {}
    for sommet in graph:
        distances[sommet] = float("inf")
        unvisited[sommet] = distances[sommet]
    distances[start] = 0
    while unvisited:
        current = min(unvisited, key=unvisited.get)
        del unvisited[current]
        for voisin, poid in graph[current]:
            new_distance = distances[current] + poid
            if new_distance < distances[voisin]:
                distances[voisin] = new_distance
                predecesseur[voisin] = current
                if voisin in unvisited:
                    unvisited[voisin] = new_distance
    return distances, predecesseur


def reconstruire_chemin(predecesseur: dict, start: any, end: any) -> list:
    """reconstruit le chemin grace au predecesseur

    Args:
        predecesseur (dict): les predecesseurs
        start (any): le debut
        end (any): la fin

    Returns:
        list: renvoie une liste contenant le chemin le plus court (si aucun trouver alors renvoie liste vide)
    Examples:
        >>> pred = {'B': 'A', 'C': 'A', 'D': 'C', 'E': 'D', 'F': 'D', 'G': 'E'}
        >>> reconstruire_chemin(pred, 'A', 'F')
        ['A', 'C', 'D', 'F']
        >>> reconstruire_chemin(pred, 'A', 'G')
        ['A', 'C', 'D', 'E', 'G']
    """
    chemin = [end]
    current = end
    while current != start:
        if current not in predecesseur:
            return []
        current = predecesseur[current]
        chemin.append(current)
    chemin.reverse()
    return chemin


def solutions_dijkstra(graph: dict, start: any) -> dict:
    """elle renvoie le dictionnaire des noeud et distances grace au chemin

    Args:
        graph (dict): le graphe
        start (any): le debut

    Returns:
        dict: contenant les noeuds et leurs distances
    Exemples:
        >>> graph = {
        ...     'A': [('B', 4), ('C', 2)],
        ...     'B': [('C', 5), ('D', 10)],
        ...     'C': [('D', 3), ('E', 8)],
        ...     'D': [('E', 4), ('F', 11)],
        ...     'E': [('G', 6)],
        ...     'F': [('G', 2)],
        ...     'G': []
        ... }
        >>> sol = solutions_dijkstra(graph, 'A')
        >>> sol['F']
        {'distance': 16, 'chemin': ['A', 'C', 'D', 'F']}
        >>> sol['G']
        {'distance': 15, 'chemin': ['A', 'C', 'D', 'E', 'G']}
    """
    distances, predecesseur = dijkstra(graph, start)
    solutions = {}
    for sommet in graph:
        if sommet == start:
            chemin = [start]
        else:
            chemin = reconstruire_chemin(predecesseur, start, sommet)
            if not chemin:
                chemin = None
        solutions[sommet] = {"distance": distances[sommet], "chemin": chemin}
    return solutions


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 5), ("D", 10)],
        "C": [("D", 3), ("E", 8)],
        "D": [("E", 4), ("F", 11)],
        "E": [("G", 6)],
        "F": [("G", 2)],
        "G": [],
    }
    solution = solutions_dijkstra(graph, "A")
    for sommet, info in solution.items():
        print(
            f"sommet: {sommet} ----- Distance: {info['distance']} ------- chemin: {info['chemin']}"
        )
