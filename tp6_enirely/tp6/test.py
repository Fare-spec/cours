import Pile_LSC as lifo
from random import shuffle

def afficher(pile):
    """Affiche les éléments d'une pile du sommet à la base."""
    print("|----")
    temp = pile
    while not lifo.est_pile_vide(temp):
        print(f"| {lifo.sommet(temp)}")
        temp = lifo.depiler(temp)
    print("|----\n")

def copier_pile(pile):
    """Copie une pile représentée par une liste simplement chaînée."""
    copie = lifo.creer_pile_vide()
    pile_temp = lifo.creer_pile_vide()

    while not lifo.est_pile_vide(pile):
        sommet = lifo.sommet(pile)
        pile_temp = lifo.empiler(pile_temp, sommet)
        pile = lifo.depiler(pile)

    while not lifo.est_pile_vide(pile_temp):
        sommet = lifo.sommet(pile_temp)
        pile = lifo.empiler(pile, sommet)  
        copie = lifo.empiler(copie, sommet)  
        pile_temp = lifo.depiler(pile_temp)

    return copie  

def hauteur_pile(pile):
    """
    Renvoie hauteur de la pile.
    PARAMETRES : pile - pile à analyser.
    RETURN : hauteur.
    EFFET DE BORD : Aucune.
    """
    n = 0
    while not lifo.est_pile_vide(pile):
        n += 1
        pile = lifo.depiler(pile)
    return n

def retourner(pile, j):
    """
    Inverse j derniers éléments de la pile.
    PARAMETRES : pile - pile à modifier, j - nombre d'éléments à inverser.
    RETURN : Aucune.
    EFFET DE BORD : Modifie la pile.
    """
    pile_aux = lifo.creer_pile_vide()
    
    for _ in range(j):
        if lifo.est_pile_vide(pile):
            break
        pile_aux = lifo.empiler(pile_aux, lifo.sommet(pile))
        pile = lifo.depiler(pile)

    while not lifo.est_pile_vide(pile_aux):
        pile = lifo.empiler(pile, lifo.sommet(pile_aux))
        pile_aux = lifo.depiler(pile_aux)

def max_pile(pile, i):
    """
    Renvoie position du maximum parmi i derniers éléments.
    PARAMETRES : pile - pile à analyser, i - nombre d'éléments.
    RETURN : position du maximum.
    EFFET DE BORD : Aucune.
    """

    copy = copier_pile(pile)  
    max_value = lifo.sommet(copy)
    ind = 1
    ind_n = 1

    for _ in range(i):
        if lifo.est_pile_vide(copy):
            break
        current = lifo.sommet(copy)
        if current > max_value:
            max_value = current
            ind = ind_n
        copy = lifo.depiler(copy)
        ind_n += 1
        
    return ind


def tri_crepes_iteratif(pile): #ne fonctionne pas
    """
    Tri des crêpes en cours.
    PARAMETRES : pile - pile à trier.
    RETURN : pile triée.
    EFFET DE BORD : Modifie la pile.
    """

    n = hauteur_pile(pile)
    for i in range(n):
        max_position = max_pile(pile, n - i)
        if max_position!= n - i:
            retourner(pile, n - max_position)
            retourner(pile, i + 1)

    return pile


if __name__ == "__main__":
    from random import shuffle

    ma_liste = [i for i in range(10)]
    shuffle(ma_liste)

    print("Liste de départ :", ma_liste)

    ma_pile = lifo.creer_pile_vide()
    for element in ma_liste:
        ma_pile = lifo.empiler(ma_pile, element)

    print("\nPile initiale :")
    afficher(ma_pile)
    print(max_pile(ma_pile,10))
    print("Tri des crêpes en cours...")
    ma_pile = tri_crepes_iteratif(ma_pile)
    print("Pile après tri :")
    afficher(ma_pile)