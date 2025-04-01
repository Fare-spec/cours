#!/usr/bin/python3
# -*- coding: utf8 -*-

###################################
#
# _SOMMETS.PY
# -----------
#
# Module de traitement des Sommets
#
###################################

# Un sommet est un tuple (nom, altitude, massif)
# - nom : STR
# - altitude : INT, altitude en m
# - massif : STR


def creer_sommet(nom, altitude, massif):
    """
    Construit le tuple sommet.

    Paramètres :
    - nom : STR, le nom du sommet
    - altitude : INT, l'altitude en m
    - massif : STR, le massif contenant le sommet

    Résultat :
    - TUPLE, le sommet

    Pré-condition :
    - aucune (programmation défensive à envisager)

    Effet de bord :
    - aucun
    """
    return (nom, altitude, massif)


def altitude_en_m(altitude):
    """
    Conversion de l'altitude en entier ("2 062 m" -> 2062)

    Paramètre :
    - altitude : STR, chaîne du type "2 062 m", avec espaces et 'm'

    Résultat :
    - INT, l'altitude en m

    Pré-condition :
    - aucune (prog def à envisager)

    Effet de bord :
    - aucun
    """
    tmp = ""
    for symbole in altitude:
        if not (symbole in " m"):
            tmp += symbole
    return int(tmp)


def creer_sommet_csv(ligne, massif):
    """
    Construit un sommet à partir d'une ligne du fichier csv.

    Paramètres :
    - ligne : STR, ligne du fichier csv
    - massif : STR, basename du fichier contenant la ligne

    Résultat :
    - TUPLE, le sommet correspondant

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    nom, alt = ligne.rstrip().split(",")
    return creer_sommet(nom, altitude_en_m(alt), massif)


def afficher(sommet):
    """
    Affichage formatté du sommet.

    Paramètres :
    - sommet : TUPLE, le sommet à afficher

    Résultat :
    - NONETYPE, None

    Pré-condition :
    - aucune

    Effet de bord :
    - Affichage sur la sortie standard
    """
    nom, altitude, massif = sommet
    print(f"{nom:35s}\t[{massif}]\n\taltitude : {altitude} m")
    return None


def nom(sommet):
    """
    Consulte le nom d'un sommet

    Paramètre :
    - sommet : TUPLE

    Résultat :
    - STR, le nom du sommet

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    return sommet[0]


def altitude(sommet):
    """
    Consulte l'altitude d'un sommet

    Paramètre :
    - sommet : TUPLE

    Résultat :
    - INT : l'altitude du sommet

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    return sommet[1]


def massif(sommet):
    """
    Consulte le massif d'un sommet

    Paramètre :
    - sommet : TUPLE

    Résultat :
    - STR, le massif du sommet

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    return sommet[2]


def coincide_nom(sommet, motif):
    """
    Compare le nom du sommet au motif

    Paramètres :
    - sommet : TUPLE, le sommet à tester
    - motif : STR, le motif à identifier

    Résultat :
    - BOOL : Vrai ssi le nom du sommet correspond au motif

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    nom_sommet = nom(sommet)
    return (len(motif) <= len(nom_sommet)) and (nom_sommet[: len(motif)] == motif)


if __name__ == "__main__":
    pass
