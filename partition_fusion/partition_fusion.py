#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:15:57 2025

@author: elouan.fare
"""


import liste as fifo


def taille(liste):
    a = 0
    while not(fifo.est_vide(liste)):
        liste = fifo.queue(liste)
        a+=1
    return a

def divise2(liste):
    n = taille(liste)
    droite, gauche = partition(liste,0,n//2)
    return droite,gauche



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


def fusion(gauche,droite):
    if fifo.est_vide(gauche):
        return droite
    if fifo.est_vide(droite):
        return gauche

    if fifo.tete(gauche)<=fifo.tete(droite):
        return fifo.ajouter(fusion(fifo.queue(gauche),droite),fifo.tete(gauche))
    else:
        return fifo.ajouter(fusion(gauche,fifo.queue(droite)),fifo.tete(droite))

liste_initiale = fifo.creer_liste()
for i in reversed(range(10)):
    liste_initiale = fifo.ajouter(liste_initiale, i)
gauche, droite = partition(liste_initiale,3 ,7)
print(gauche, droite)
print(taille(liste_initiale))

