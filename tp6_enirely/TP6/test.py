import Pile_LSC as lifo
import LSC as blsc
from random import shuffle

def afficher(pile):
    """Affiche les éléments d'une pile du sommet à la base."""
    print("|----")
    while not lifo.est_pile_vide(pile):
        print(f"| {lifo.sommet(pile)}")
        pile = lifo.depiler(pile)
    print("|----\n")

def hauteur_pile(pile):
    """Renvoie la hauteur de la pile sans la modifier."""
    copie = pile
    n = 0
    while not lifo.est_pile_vide(copie):
        copie = lifo.depiler(copie)
        n += 1
    return n
def max_pile(pile: blsc.Liste_Simplement_Chainee, i: int):
    """Trouve le maximum parmi les i premiers éléments de la pile."""
    total = hauteur_pile(pile)
    #assert i > total (f"Taille insuffisante : attendu au moins {i} éléments")
    meilleur = lifo.sommet(pile)  # Premier élément comme point de départ
    temporaire = pile

    for _ in range(i):
        courant = lifo.sommet(temporaire)
        temporaire = lifo.depiler(temporaire)

        if courant > meilleur:
            meilleur = courant

    return meilleur
def retourner(pile, j):
    """Inverse les j derniers éléments de la pile."""
    pile_aux = lifo.creer_pile_vide()
    
    # Depile les éléments dans une pile temporaire:
    for _ in range(j):
        pile_aux = lifo.empiler(pile_aux, lifo.sommet(pile))
        pile = lifo.depiler(pile)

    # Remets les éléments inversés dans la pile principale:
    while not lifo.est_pile_vide(pile_aux):
        pile = lifo.empiler(pile, lifo.sommet(pile_aux))
        pile_aux = lifo.depiler(pile_aux)

    return pile

def tri_crepes_recursif(pile, n=None):
    """Trie la pile en utilisant le tri des crêpes de manière récursive."""
    if n is None:
        n = hauteur_pile(pile)
    # pas besoin de tri en si len(pile) == 1
    if n <= 1:
        return pile

    pos_max = max_pile(pile, n)

    if pos_max != 1:
        pile = retourner(pile, pos_max)

    pile = retourner(pile, n)
    return tri_crepes_recursif(pile, n - 1)

if __name__ == "__main__":
    # Initialisation d'une pile avec des valeurs aléatoires
    # Tri des crêpes récursif
    ma_liste = [_ for _ in range(10)]
    shuffle(ma_liste)

    print("Liste de départ : ", ma_liste)

    ma_pile = lifo.creer_pile_vide()

    print("\nEMPILEMENT\n")

    for element in ma_liste:
        ma_pile = lifo.empiler(ma_pile, element)
        afficher(ma_pile)

    print("\nDEPILEMENT\n")

    while not(lifo.est_pile_vide(ma_pile)):
        print(f"Sommet : {lifo.sommet(ma_pile)}")
        ma_pile = lifo.depiler(ma_pile)
        afficher(ma_pile)
    print(max_pile(ma_pile,1))
