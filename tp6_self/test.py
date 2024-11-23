#!/usr/bin/python3
import LSC as lsc
import Pile_List as lifo
from random import shuffle
from typing import List, Tuple, Union, TypeVar, Any
T = TypeVar('T')
PileType = Union[List[T], Tuple[T,...], lsc.Liste_Simplement_Chainee]

#----------------------------------------------------------------
# Aucun effet de bord sur les fonctions ajoutés car je n'y suis pas arrivé
#----------------------------------------------------------------

def afficher(pile):
    print("|----\n|")
    while not(lifo.est_pile_vide(pile)):
        print(f"| {lifo.sommet(pile)}\n|")
        pile = lifo.depiler(pile)
    print("|----")
    return None

def hauteur_pile(pile: PileType) -> int:
    """Retourne la taille/ hauteur de la pile

    Args:
        pile (list/tuple/lsc.Liste_Simplement_Chainee): la pile a mesurer

    Returns:
        int: la taille de la pile
    """
    n = 0
    while not(lifo.est_pile_vide(pile)):
        n += 1
        pile = lifo.depiler(pile)
    return n
def copie(pile: PileType) -> PileType:
    """creer une copie de la pile

    Args:
        pile (PileType): pile a copier

    Returns:
        PileType: une copie de la pile
    """
    pile_copie = lifo.creer_pile_vide()
    while not(lifo.est_pile_vide(pile)):
        pile_copie = lifo.empiler(pile_copie, lifo.sommet(pile))
        pile = lifo.depiler(pile)
    return pile_copie

def max_pile(pile: PileType,start: int)-> int:
    """Retourne l'element le plus grand de la pile

    Args:
        start: int: la position de départ de la recherche
        pile: PileType: la pile a analyser

    Returns:
        int: l'indice de l'element le plus grand de la pile
    """

    assert start >=0, "Position de départ invalide"
    assert hauteur_pile(pile) >= start, "Position de départ dépasse la taille de la pile"
    assert not(lifo.est_pile_vide(pile)), "La pile est vide"
    pile2 = copie(copie(pile)) # <--- pas très propre c'est pour renverser la copie qui a été renversé
    # J'itère jusqu' a start:
    max_n = lifo.sommet(pile)
    for _ in range(start):
        sommet = lifo.sommet(pile2)
        pile2 = lifo.depiler(pile2)
        if sommet > max_n:
            max_n = sommet
        
    pile2 = copie(copie(pile))
    # je cherche l'index du max dans pile2
    for i in range(start):
        i+=1
        if lifo.sommet(pile2) == max_n:
            return i
        else:
            pile2 = lifo.depiler(pile2)


def retourner(pile: PileType, j: int) -> PileType:
    """retourne la pile avec les j premiers éléments renversés.

    Args:
        pile (PileType): la pile
        j (int): l'index a renverser

    Returns:
        PileType: la pile renversée
    """
    pile1 = copie(copie(pile))
    pile2 = lifo.creer_pile_vide()

    # je déplace les j premiers éléments de pile1 dans pile2
    for _ in range(j):
        sommet = lifo.sommet(pile1)
        pile1 = lifo.depiler(pile1)
        pile2 = lifo.empiler(pile2, sommet)
    # renverse Pile 2
    pile2 = copie(pile2)
    #ajoute pile2 a pile1
    while not(lifo.est_pile_vide(pile2)):
        sommet = lifo.sommet(pile2)
        pile1 = lifo.empiler(pile1,sommet)
        pile2 = lifo.depiler(pile2)
    pile = lifo.creer_pile_vide()
    # remplace Pile par Pile1
    while not(lifo.est_pile_vide(pile1)):
        sommet = lifo.sommet(pile1)
        pile = lifo.empiler(pile, sommet)
        pile1 = lifo.depiler(pile1)
    return copie(pile)
def tri_crepes(pile: PileType) -> PileType:
    """tri la pile en utilisant 'pancakes sort'

    Args:
        pile (PileType): la pile a trier

    Returns:
        PileType: la pile triée
    """
    n = hauteur_pile(pile)
    while n > 1:
        index_max = max_pile(pile, n)
        pile = retourner(pile,index_max)
        pile = retourner(pile,n)
        n-=1
    return (pile)




if __name__ == "__main__":
    ma_liste = [_ for _ in range(10)]
    shuffle(ma_liste)

    print("Liste de départ : ", ma_liste)

    ma_pile = lifo.creer_pile_vide()

    print("\nEMPILEMENT\n")

    for element in ma_liste:
        ma_pile = lifo.empiler(ma_pile, element)
    j = 4
    print("\nTaille de la pile : ", hauteur_pile(ma_pile))
    print(f"Element le plus grand de la pile à partir de l'index {j}: {max_pile(ma_pile,4)}")
    pile = retourner(ma_pile, j)
    hauteur_pile(ma_pile)
    afficher(pile)
    print("\nDEPILEMENT\n")

    pile_triee = tri_crepes(ma_pile)
    afficher(pile_triee)
    while not(lifo.est_pile_vide(ma_pile)):
        print(f"Sommet : {lifo.sommet(ma_pile)}")
        ma_pile = lifo.depiler(ma_pile)
        afficher(ma_pile)
