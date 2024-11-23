#!/usr/bin/python3
# -*- coding: utf8 -*-

############################
#
# _SOMMETS_DICT.PY
# ----------------
#
# Module des sommets
# implémentés par des dict
############################

# Un sommet est un dictionnaire
# dont les clés sont 'nom', 'altitude' et 'massif'
# - nom : STR
# - altitude : INT, altitude en m
# - massif : STR

def creer_sommet(nom, altitude, massif):
    """
    Construit le dico sommet.

    Paramètres :
    - nom : STR, le nom du sommet
    - altitude : INT, l'altitude en m
    - massif : STR, le massif contenant le sommet

    Résultat :
    - DICT, le sommet

    Pré-condition :
    - aucune (programmation défensive à envisager)

    Effet de bord : 
    - aucun 
    """
    sommet = {
            "Nom": nom,
            "Altitude": altitude,
            "Massif": massif
    }

    return sommet

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
    tmp = ''
    for symbole in altitude:
        if not(symbole in ' m'):
            tmp += symbole
    return int(tmp)

def creer_sommet_csv(ligne, massif):
    """
    Construit un sommet à partir d'une ligne du fichier csv.

    Paramètres :
    - ligne : STR, ligne du fichier csv 
    - massif : STR, basename du fichier contenant la ligne

    Résultat :
    - DICT, le sommet correspondant

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun
    """
    nom, alt = ligne.rstrip().split(',')
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

    print(f"{sommet['Nom']:35s}\t[{sommet['Massif']}]\n\taltitude : {sommet['Altitude']} m")


def nom(sommet):
    """
    Consulte le nom d'un sommet

    Paramètre :
    - sommet : DICT

    Résultat :
    - STR, le nom du sommet

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun 
    """
    return sommet["Nom"]
def altitude(sommet):
    """
    Consulte l'altitude d'un sommet

    Paramètre :
    - sommet : DICT

    Résultat :
    - INT : l'altitude du sommet

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun 
    """
    return sommet['Altitude']
def massif(sommet):
    """
    Consulte le massif d'un sommet

    Paramètre :
    - sommet : DICT

    Résultat :
    - STR, le massif du sommet

    Pré-condition :
    - aucune

    Effet de bord :
    - aucun 
    """
    return sommet["Massif"]
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
    return (len(motif) <= len(nom_sommet)) and (nom_sommet[:len(motif)] == motif)

if __name__ == '__main__':
    pass
