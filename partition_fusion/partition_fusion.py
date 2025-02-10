#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:15:57 2025

@author: elouan.fare
"""


import liste as fifo


def partition(liste, debut, fin):
    liste1 = liste
    liste2 = liste
    if fifo.est_vide(liste):
        return (fifo.creer_liste(), fifo.creer_liste())
    else:
        left_liste = fifo.creer_liste()
        for _ in range(int((debut + fin )/2)):
            liste1 = fifo.tete(liste1)
        for _ in range(debut,fin):
            left_liste = fifo.ajouter(left_liste, fifo.queue(liste2))
    return liste1, left_liste
    

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

liste = fifo.creer_liste()
for i in range(10):
    liste = (liste, i)
print(liste)

liste = fifo.queue(liste)
print(liste)




