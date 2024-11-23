#!/usr/bin/python3
# -*- coding: utf8 -*-

#################################
#
# _COLLECTION.PY
# --------------
#
# Module du type ensemble
#
#################################

# Un ensemble est une collection d'éléments, d'occurence unique.
# Les fonctions sont implémentées dans le paradigme fonctionnel.

def initialiser_ensemble():
    """
    Construit un ensemble vide.

    Paramètre :
    - aucun

    Résultat :
    - ENSEMBLE vide

    Pré-condition :
    - aucune

    Effet de bord 
    - aucune
    """
    return set()

def est_ensemble_vide(ensemble):
    """
    Teste si l'ensemble est vide.

    Paramètre :
    - ensemble : ENSEMBLE, l'ensemble à tester

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    return len(ensemble) == 0

def copier_ensemble(ensemble):
    """
    Construit la copie d'un ensemble.

    Paramètre :
    - ensemble : ENSEMBLE, la source

    Résultat :
    - ENSEMBLE : une copie de la source

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    resultat = initialiser_ensemble()
    for _ in ensemble:
        resultat.add(_)
    return resultat

def ajouter(ensemble, element):
    """
    Ajoute un element à la copie d'un ensemble

    Paramètres :
    - ensemble : ENSEMBLE, l'ensemble à abonder
    - element : ANY, l'élément à ajouter

    Résultat :
    - ENSEMBLE, l'ensemble abondé

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    resultat = copier_ensemble(ensemble)
    resultat.add(element)
    return resultat

def supprimer(ensemble, element):
    """
    Construire une copie de l'ensemble privé d'un élément.
    Si l'élément à supprimer n'est pas dans l'ensemble initial, 
    alors une copie intégrale est renvoyée.

    Paramètres :
    - ensemble ; ENSEMBLE, la collection à amender
    - element : ANY, l'élément à supprimer

    Résultat :
    - ENSEMBLE, la copie amendée de l'ensemble
    """
    resultat = initialiser_ensemble()
    for _ in ensemble:
        if not(_ == element):
            resultat = ajouter(resultat, _)
    return resultat

def rechercher(ensemble, cle, critere = lambda x, y: x==y):
    """
    Construit la sous-collection constituée des éléments d'un ensemble
    dont la clé satisfait un critère donné.

    Paramètres :
    - ensemble : ENSEMBLE, la collection à explorer
    - cle : ANY, la clé à rechercher
    - critere : FUNCTION ou LAMBDA, test utilisé pour la recherche

    Résultat :
    - ENSEMBLE, la collection extraite des éléments satisfaisant le test

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    resultat = initialiser_ensemble()
    for _ in ensemble:
        if critere(_, cle):
            resultat = ajouter(resultat, _)
    return resultat

def supprimer_critere(ensemble, cle, critere):
    """
    Construit la collection des éléments d'un ensemble, 
    dont la clé satisfait le critère donné.

    Paramètres :
    - ensemble : ENSEMBLE, la collection source
    - cle : ANY, la clé à employer pour la suppression
    - critere : FUNCTION ou LAMBDA, critère de sélection

    Résultat :
    - ENSEMBLE : la copie de l'ensemble amendée

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    resultat = copier_ensemble(ensemble)
    elements = rechercher(ensemble, cle, critere)
    for _ in elements:
        resultat = supprimer(resultat, _)
    return resultat

def lister(ensemble, affichage=print):
    """
    Afficher le contenu d'un ensemble, 
    en formattant chaque élément selon la fonction d'affichage fournie.

    Paramètres :
    - ensemble : ENSEMBLE, la collection à énumérer
    - affichage : FUNCTION, la fonction à appliquer à chaque élément.

    Résultat :
    - None : NONETYPE

    Pré-condition :
    - aucune

    Effet de bord :
    - Affichage sur la sortie standard
    """
    for element in ensemble:
        affichage(element)
    return None



if __name__ == "__main__":
    pass
