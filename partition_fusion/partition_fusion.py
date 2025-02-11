#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:15:57 2025

@author: elouan.fare
"""


import liste as fifo


def renverser(liste):
    result = fifo.creer_liste()
    while not fifo.est_vide(liste):
        result = fifo.ajouter(result, fifo.tete(liste))
        liste = fifo.queue(liste)
    return result


def partition(liste, debut, fin):
    if fifo.est_vide(liste):
        return fifo.creer_liste(), fifo.creer_liste()

    current = liste
    for _ in range(debut):
        if fifo.est_vide(current):
            break
        current = fifo.queue(current)
    
    segment_inversé = fifo.creer_liste()
    for _ in range(fin - debut):
        if fifo.est_vide(current):
            break
        segment_inversé = fifo.ajouter(segment_inversé, fifo.tete(current))
        current = fifo.queue(current)
    
    segment = renverser(segment_inversé)

    return current, segment


def fusion(tab, debut, milieu, fin):
    gauche = tab[debut:milieu + 1]
    droite = tab[milieu + 1:fin + 1]
    i, j, k = 0, 0, debut

    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            tab[k] = gauche[i]
            i += 1
        else:
            tab[k] = droite[j]
            j += 1
        k += 1

    while i < len(gauche):
        tab[k] = gauche[i]
        i += 1
        k += 1

    while j < len(droite):
        tab[k] = droite[j]
        j += 1
        k += 1

def tri_fusion_partition(tab, debut, fin):
    if debut < fin:
        pivot_index = partition(tab, debut, fin)
        tri_fusion_partition(tab, debut, pivot_index - 1)
        tri_fusion_partition(tab, pivot_index + 1, fin)
        fusion(tab, debut, pivot_index, fin)


liste_test = fifo.creer_liste()
for i in range(1,10):
    liste_test = fifo.ajouter(liste_test,i)
print(liste_test)

test = partition(liste_test,1,9)


print(test)
