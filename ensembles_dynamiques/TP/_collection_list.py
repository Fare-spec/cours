#!/usr/bin/python3
# -*- coding: utf8 -*-

#################################
#
# _COLLECTION_LIST.PY
# -------------------
#
# Module du type ensemble
# implémenté sur les listes
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

    Effet de bord :
    - aucune
    """
    return list()


def est_ensemble_vide(ensemble):
    """
    Teste si l'ensemble est vide.

    Paramètre :
    - ensemble : LIST, l'ensemble à tester

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
    - ensemble : LIST, la source

    Résultat :
    - LIST : une copie de la source

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    return ensemble[:]


def ajouter(ensemble, element):
    """
    Ajoute un element à la copie d'un ensemble

    Paramètres :
    - ensemble : LIST, l'ensemble à abonder
    - element : ANY, l'élément à ajouter

    Résultat :
    - LIST, l'ensemble abondé

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    copie = ensemble.copy()
    copie.append(element)
    return copie


def supprimer(ensemble, element):
    """
    Construire une copie de l'ensemble privé d'un élément.
    Si l'élément à supprimer n'est pas dans l'ensemble initial,
    alors une copie intégrale est renvoyée.

    Paramètres :
    - ensemble ; LIST, la collection à amender
    - element : ANY, l'élément à supprimer

    Résultat :
    - LIST, la copie amendée de l'ensemble
    """
    resultat = ensemble[:]
    return resultat.remove(element)


def rechercher(ensemble, cle, critere=lambda x, y: x == y):
    """
    Construit la sous-collection constituée des éléments d'un ensemble
    dont la clé satisfait un critère donné.

    Paramètres :
    - ensemble : LIST, la collection à explorer
    - cle : ANY, la clé à rechercher
    - critere : FUNCTION ou LAMBDA, test utilisé pour la recherche

    Résultat :
    - LIST, la collection extraite des éléments satisfaisant le test

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    return [element for element in ensemble if critere(element, cle)]


def supprimer_critere(ensemble, cle, critere):
    """
    Construit la collection des éléments d'un ensemble,
    dont la clé satisfait le critère donné.

    Paramètres :
    - ensemble : LIST, la collection source
    - cle : ANY, la clé à employer pour la suppression
    - critere : FUNCTION ou LAMBDA, critère de sélection

    Résultat :
    - LIST : la copie de l'ensemble amendée

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    return [element for element in ensemble if not critere(element, cle)]


def lister(ensemble, affichage=print):
    """
    Afficher le contenu d'un ensemble,
    en formattant chaque élément selon la fonction d'affichage fournie.

    Paramètres :
    - ensemble : LIST, la collection à énumérer
    - affichage : FUNCTION, la fonction à appliquer à chaque élément.

    Résultat :
    - None : NONETYPE

    Pré-condition :
    - aucune

    Effet de bord :
    - Affichage sur la sortie standard
    """
    for item in ensemble:
        affichage(item)


if __name__ == "__main__":
    pass
