from typing import Any


def partitionement(liste: list[Any], debut, fin):
    pivot = liste[debut]
    gauche = debut + 1
    droite = fin - 1
    while gauche <= droite:
        while (gauche <= droite) and (liste[gauche] <= pivot):
            gauche += 1

        while (gauche <= droite) and (liste[droite] > pivot):
            droite -= 1

        if gauche < droite:
            exchange(liste, gauche, droite)
            gauche += 1
            droite -= 1
        exchange(liste, droite, debut)
    return droite


def exchange(liste, indx_g, indx_d):
    liste[indx_g], liste[indx_d] = liste[indx_d], liste[indx_g]


l = [12, 4, 0, 44, 27]
print(partitionement(l, 0, len(l) - 1))
