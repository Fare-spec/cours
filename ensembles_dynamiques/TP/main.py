#!/usr/bin/python3
# -*- coding: utf8 -*-

#######################################
#
# MAIN.PY
# -------
#
# Interface principale
#
#######################################

import _collection_list as col
import _sommets as som

# Le module _collection définit nos ENSEMBLES
# Le module _sommets définit nos SOMMETS

def file_2_set(fichier='./data/Chartreuse.csv'):
    """
    Lecture du fichier csv contenant les caractéristiques des sommets.

    Paramètres :
    - fichier : STR, le nom complet du fichier csv à parcourir

    Résultat : 
    - resultat : ENSEMBLE, la collection des sommets

    Pré-conditions : 
    - aucune

    Effets de bord :
    - aucun
    """
    massif = fichier[7:-4]
    resultat = col.initialiser_ensemble()
    with open(fichier) as src:
        ligne = src.readline()
        while ligne:
            resultat = col.ajouter(resultat, som.creer_sommet_csv(ligne, massif))
            ligne = src.readline()
    return resultat

def rechercher(ensemble, motif):
    """
    Recherche les sommets de la collection dont le nom 
    correspond à un motif donné.

    Paramètres :
    - ensemble : ENSEMBLE, la collection des somets
    - motif : STR, la chaîne de caractères à identifier

    Résultat : 
    - ENSEMBLE, la sous-collection des sommets satisfaisant au critère

    Pré-condition : 
    - aucune

    Effet de bord :
    - aucun 
    """
    return col.rechercher(ensemble, motif, som.coincide_nom)


if __name__ == '__main__':
    col.lister(col.supprimer_critere(file_2_set(), 'Grand', som.coincide_nom), \
            som.afficher)
