from typing import Any

def creer_pile_vide() -> list:
    """Crée une pile vide sous forme de liste.

    Returns:
        list: Une pile vide représentée par une liste.
    """
    return []

def est_pile_vide(pile: list) -> bool:
    """Vérifie si la pile est vide.

    Args:
        pile (list): La pile à vérifier.

    Returns:
        bool: True si la pile est vide, False sinon.
    """
    return len(pile) == 0

def sommet(pile: list) -> Any:
    """Renvoie l'élément au sommet de la pile.

    Args:
        pile (list): La pile dont on veut connaître le sommet.

    Returns:
        Any: L'élément au sommet de la pile.

    Raises:
        AssertionError: Si la pile est vide.
    """
    assert not est_pile_vide(pile), "Pile vide!"
    return pile[-1]

def empiler(pile: list, element: Any) -> list:
    """Ajoute un élément au sommet de la pile.

    Args:
        pile (list): La pile actuelle.
        element (Any): L'élément à ajouter au sommet de la pile.

    Returns:
        list: La nouvelle pile avec l'élément ajouté.
    """
    return pile + [element]

def depiler(pile: list) -> list:
    """Retire l'élément au sommet de la pile.

    Args:
        pile (list): La pile dont on veut retirer le sommet.

    Returns:
        list: La nouvelle pile sans l'élément au sommet.

    Raises:
        AssertionError: Si la pile est vide.
    """
    assert not est_pile_vide(pile), "Pile vide!"
    return pile[:-1]
