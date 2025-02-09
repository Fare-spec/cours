# Chacune des fonctions renvoie et n'ont pas d'effet de bord

def creer_pile_vide()->list:
    """Créer une pile vide.

    Returns:
        list: La pile vide
    """
    return []
def est_pile_vide(pile: list) -> bool:
    """Retourne True si la pile est vide, False sinon.

    Args:
        pile (list): La pile à tester

    Returns:
        bool: True si la pile est vide
    """
    return len(pile) == 0
def sommet(pile: list)->int:
    """Retourne le sommet de la pile.

    Args:
        pile (list): La pile avec le sommet

    Returns:
        any: le sommet de la pile
    """
    assert not est_pile_vide(pile), "La pile est vide"
    return pile[-1]

def empiler(pile: list, elt: any)-> list:
    """rajoute elt au sommet de la pile

    Args:
        pile (list): La pile à modifier
        elt (any): l'élement à ajouter

    Returns:
        list: la pile modifiée
    """
    return pile + [elt]

def depiler(pile: list)-> any:
    """retourne la pile sans le sommet

    Args:
        pile (list): la pile avec le sommet

    Returns:
        any: la pile sans le sommet
    """
    assert not est_pile_vide(pile), "La pile est vide"
    return pile[:-1]