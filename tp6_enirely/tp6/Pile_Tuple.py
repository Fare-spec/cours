def creer_pile_vide():
    """Crée une pile vide sous forme de tuple.

    Returns:
        tuple: Une pile vide représentée par un tuple vide.
    """
    return ()

def est_pile_vide(pile):
    """Vérifie si la pile est vide.

    Args:
        pile (tuple): La pile à vérifier.

    Returns:
        bool: True si la pile est vide, False sinon.
    """
    return pile == ()

def sommet(pile):
    """Renvoie l'élément au sommet de la pile.

    Args:
        pile (tuple): La pile dont on veut connaître le sommet.

    Returns:
        _type_: L'élément au sommet de la pile.

    Raises:
        AssertionError: Si la pile est vide.
    """
    assert not est_pile_vide(pile), "Pile vide!"
    return pile[-1]

def empiler(pile, elt):
    """Ajoute un élément au sommet de la pile.

    Args:
        pile (tuple): La pile actuelle.
        elt (_type_): L'élément à ajouter au sommet de la pile.

    Returns:
        tuple: La nouvelle pile avec l'élément ajouté.
    """
    return pile + (elt,)

def depiler(pile):
    """Retire l'élément au sommet de la pile.

    Args:
        pile (tuple): La pile dont on veut retirer le sommet.

    Returns:
        tuple: La nouvelle pile sans l'élément au sommet.

    Raises:
        AssertionError: Si la pile est vide.
    """
    assert not est_pile_vide(pile), "Pile vide!"
    return pile[:-1]
