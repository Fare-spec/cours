import LSC as lsc
from typing import Any

def creer_pile_vide() -> lsc.Liste_Simplement_Chainee:
    """Crée une pile vide sous forme de liste simplement chaînée.

    Returns:
        lsc.Liste_Simplement_Chainee: Une pile vide représentée par une liste simplement chaînée.
    """
    return lsc.creer_liste_vide()

def est_pile_vide(pile: lsc.Liste_Simplement_Chainee) -> bool:
    """Vérifie si la pile est vide.

    Args:
        pile (lsc.Liste_Simplement_Chainee): La pile à vérifier.

    Returns:
        bool: True si la pile est vide, False sinon.
    """
    return lsc.est_vide(pile)

def sommet(pile: lsc.Liste_Simplement_Chainee) -> Any:
    """Renvoie l'élément au sommet de la pile.

    Args:
        pile (lsc.Liste_Simplement_Chainee): La pile dont on veut connaître le sommet.

    Returns:
        Any: L'élément au sommet de la pile.

    Raises:
        AssertionError: Si la pile est vide.
    """
    assert not est_pile_vide(pile), "Pile vide."
    return lsc.tete(pile)

def empiler(pile: lsc.Liste_Simplement_Chainee, element: Any) -> lsc.Liste_Simplement_Chainee:
    """Ajoute un élément au sommet de la pile.

    Args:
        pile (lsc.Liste_Simplement_Chainee): La pile actuelle.
        element (Any): L'élément à ajouter au sommet de la pile.

    Returns:
        lsc.Liste_Simplement_Chainee: La nouvelle pile avec l'élément ajouté.
    """
    return lsc.ajouter_en_tete(pile, element)

def depiler(pile: lsc.Liste_Simplement_Chainee) -> lsc.Liste_Simplement_Chainee:
    """Retire l'élément au sommet de la pile.

    Args:
        pile (lsc.Liste_Simplement_Chainee): La pile dont on veut retirer le sommet.

    Returns:
        lsc.Liste_Simplement_Chainee: La nouvelle pile sans l'élément au sommet.

    Raises:
        AssertionError: Si la pile est vide.
    """
    assert not est_pile_vide(pile), "Pile vide!"
    return lsc.queue(pile)
