import LSC as lsc
# Chacune des fonctions renvoie et n'ont pas d'effet de bord
def creer_pile_vide():
    """Creer une pile vide.

    Returns:
        lsc.Liste_Simplement_Chainee: La liste vide
    """
    return lsc.creer_liste_vide()
def est_pile_vide(pile: lsc.Liste_Simplement_Chainee):
    """Retourne True si la pile est vide, False sinon.

    Args:
        pile (lsc.Liste_Simplement_Chainee): La pile à tester

    Returns:
        bool: True si la pile est vide
    """
    return lsc.est_vide(pile)

def sommet(pile: lsc.Liste_Simplement_Chainee):
    """Retourne le sommet de la pile.

    Args:
        pile (lsc.Liste_Simplement_Chainee): La pile avec le sommet

    Returns:
        any: Le sommet de la pile
    """
    assert not est_pile_vide(pile), "La pile est vide"
    return lsc.tete(pile)

def empiler(pile: lsc.Liste_Simplement_Chainee,elt: any):
    """Ajoute un element en tete de la pile

    Args:
        pile lsc.Liste_Simplement_Chainee: La pile à modifier
        elt any: l'element a ajouter

    Returns:
        lsc.Liste_Simplement_Chainee : La pile avec l'element ajouté
    """
    return lsc.ajouter_en_tete(pile, elt)
    
def depiler(pile: lsc.Liste_Simplement_Chainee):
    """Retire le sommet de la pile

    Args:
        pile (lsc.Liste_Simplement_Chainee): La pile avec le sommet

    Returns:
        lsc.Liste_Simplement_Chainee: La pile avec le sommet retiré
    """
    assert not est_pile_vide(pile), "La pile est vide"
    return lsc.queue(pile)
