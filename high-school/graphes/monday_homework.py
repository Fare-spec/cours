def construire_bfs(graphe: dict, origine: str) -> dict:
    """
    Construit un arbre BFS à partir de graphe et d'un sommet d'origine.

    Args:
        graphe (dict): Un dictionnaire représentant le graphe, où les clés sont les sommets et les valeurs sont des listes de sommets adjacents.
        origine (str): Le sommet de départ pour la recherche en largeur.

    Returns:
        dict: Un dictionnaire représentant l'arbre BFS, où les clés sont les sommets et les valeurs sont des tuples contenant la distance depuis l'origine et le sommet precédent.

    Examples:
        >>> graphe = {
        ...     '1': ['2', '3'],
        ...     '2': ['4', '5'],
        ...     '3': ['6'],
        ...     '4': [],
        ...     '5': ['6'],
        ...     '6': []
        ... }
        >>> construire_bfs(graphe, '1')
        {'1': (0, None), '2': (1, '1'), '3': (1, '1'), '4': (2, '2'), '5': (2, '2'), '6': (2, '3')}

        >>> graphe = {
        ...     'A': ['B', 'C'],
        ...     'B': ['D'],
        ...     'C': ['E'],
        ...     'D': [],
        ...     'E': []
        ... }
        >>> construire_bfs(graphe, 'A')
        {'A': (0, None), 'B': (1, 'A'), 'C': (1, 'A'), 'D': (2, 'B'), 'E': (2, 'C')}
    """

    couleur = dict()
    resultat = dict()
    for som in graphe.keys():
        couleur[som] = 0
    frontiere = [origine]
    resultat[origine] = (0, None)
    couleur[origine] = 1
    while len(frontiere) > 0:
        courant = frontiere.pop(0)
        longueur, precedent = resultat[courant]
        for som in graphe[courant]:
            if couleur[som] == 0:
                frontiere.append(som)
                resultat[som] = (longueur + 1, courant)
                couleur[som] = 1
        couleur[courant] = 2
    return resultat


def construire_dfs(graphe: dict, origine: str) -> dict:
    """
    Construit un arbre DFS à partir de graphe et d'un sommet d'origine.

    Args:
        graphe (dict): Un dictionnaire représentant le graphe, où les clés sont les sommets et les valeurs sont des listes de sommets adjacents.
        origine (str): Le sommet de départ pour la recherche en profondeur.

    Returns:
        dict: Un dictionnaire représentant l'arbre DFS.

    Examples:
        >>> graphe = {
        ...     '1': ['2', '3'],
        ...     '2': ['4', '5'],
        ...     '3': ['6'],
        ...     '4': [],
        ...     '5': ['6'],
        ...     '6': []
        ... }
        >>> construire_dfs(graphe, '1')
        {'1': (0, None), '2': (1, '1'), '3': (1, '1'), '6': (2, '3'), '4': (2, '2'), '5': (2, '2')}

        >>> graphe = {
        ...     'A': ['B', 'C'],
        ...     'B': ['D'],
        ...     'C': ['E'],
        ...     'D': [],
        ...     'E': []
        ... }
        >>> construire_dfs(graphe, 'A')
        {'A': (0, None), 'B': (1, 'A'), 'C': (1, 'A'), 'E': (2, 'C'), 'D': (2, 'B')}
    """

    couleur = dict()
    resultat = dict()
    for som in graphe.keys():
        couleur[som] = 0
    frontiere = [origine]
    resultat[origine] = (0, None)
    couleur[origine] = 1
    while len(frontiere) > 0:
        courant = frontiere.pop()
        longueur, precedent = resultat[courant]
        for som in graphe[courant]:
            if couleur[som] == 0:
                frontiere.append(som)
                resultat[som] = (longueur + 1, courant)
                couleur[som] = 1
        couleur[courant] = 2
    return resultat


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    print(construire_dfs(g, "1"))
