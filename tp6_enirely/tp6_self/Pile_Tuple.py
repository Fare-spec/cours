# Chacune des fonctions renvoie et n'ont pas d'effet de bord
def creer_pile_vide() -> tuple:
    """Créer une pile vide.

    Returns:
        Tuple: La pile vide
    """
    return ()

def est_pile_vide(pile: tuple) -> bool:
    """Retourne True si la pile est vide, False sinon.

    Args:
        pile (tuple): La pile à tester

    Returns:
        bool: True si la pile est vide
    """
    return len(pile) == 0

def sommet(pile: tuple) -> any:
    """Renvoie le sommet de la pile.

    Args:
        pile (tuple): La pile contenant le sommet

    Returns:
        any: Le sommet de la pile
    """
    return pile[-1]

def empiler(pile: tuple, elt: any)-> tuple:
    """ajoute elt au sommet de la pile

    Args:
        pile (tuple): la pile a modifier
        elt (any): l'élement à ajouter

    Returns:
        tuple: la pile avec l'élement ajouté
    """
    return pile + (elt,)

def depiler(pile: tuple) -> tuple:
    """Retire le sommet de la pile

    Args:
        pile (tuple): La pile avec le sommet

    Returns:
        tuple: La pile avec le sommet retiré
    """
    assert not est_pile_vide(pile), "La pile est vide"
    return pile[:-1]