def bellman(graphe, sommet):
    """Une fonction qui prend en parametre un graphe et renvoie un dictionnaire contenant le cout des chemins de tous les points du graphe

    Args:
        graphe (dict): dictionnaire
        sommet (str): le point de depart

    Raises:
        ValueError: boucle infini (quand la comme des cout est negative)

    Returns:
        dict: un dictionnaire contenant les couts
    >>> bellman({"A":[("B",3),("C",4)],"B":[("C",0)],"C":[]},"A")
    {'A': 0, 'B': 3, 'C': 3}
    """
    distance = {sommet: float("inf") for sommet in graphe}
    distance[sommet] = 0

    for i in range(len(graphe) - 1):
        for j in graphe:
            for k, coef in graphe[j]:
                if distance[j] + coef < distance[k]:
                    distance[k] = distance[j] + coef

    for j in graphe:
        for k, coef in graphe[j]:
            if distance[j] + coef < distance[k]:
                raise ValueError("Cycle infini (le valeurs deviennent de plus en plus petite vers -inf)")

    return distance


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    graphe = {
        "A": [("G", 8), ("H", 4)],
        "G": [("H", 1), ("L", 2)],
        "H": [("L", 5), ("E", 7)],
        "L": [("E", 2)],
        "E": [],
    }
    distances = bellman(graphe, "A")
    print(distances)
