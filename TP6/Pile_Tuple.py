def creer_pile_vide():
    return ()


def est_pile_vide(pile):
    return pile == ()


def sommet(pile):
    return pile[-1]


def empiler(pile, elt):
    return pile + [elt]


def depiler(pile):
    return pile[:-1]
