# Création du fichier complet TP5_1.py avec toutes les fonctions demandées
contenu_tp5 = """
import re
from Sommets import Sommet
from LSC import creer_liste_vide, ajouter_en_tete, afficher_liste, est_vide, tete, queue

# 1. Fonction extraire_altitude
def extraire_altitude(chaine):
    \"\"\"
    Extrait la partie numérique de l'altitude depuis une chaîne du type '1 029 m'.

    Paramètres :
    chaine (str) : La chaîne contenant l'altitude et l'unité.

    Retourne :
    int : La valeur numérique de l'altitude.
    \"\"\"
    return int(re.sub(r'\\D', '', chaine))

# 2. Fonction csv2liste
def csv2liste(fichier_csv):
    \"\"\"
    Lit un fichier CSV et retourne une liste simplement chaînée des sommets.
    
    Paramètres :
    fichier_csv (str) : Le chemin vers le fichier CSV à lire.

    Retourne :
    Une liste simplement chaînée contenant les sommets.
    \"\"\"
    liste_sommets = creer_liste_vide()
    with open(fichier_csv, 'r') as fichier:
        for ligne in fichier:
            nom, altitude = ligne.strip().split(',')
            altitude = extraire_altitude(altitude)  # Extraction de la valeur numérique
            sommet = Sommet(nom, altitude, 'Chartreuse')  # Le massif est 'Chartreuse'
            liste_sommets = ajouter_en_tete(liste_sommets, sommet)
    return liste_sommets

# 3. Fonction copier_liste
def copier_liste(liste):
    \"\"\"
    Copie une liste simplement chaînée.

    Paramètres :
    liste : Une liste simplement chaînée.

    Retourne :
    Une copie de la liste.
    \"\"\"
    if est_vide(liste):
        return creer_liste_vide()
    else:
        return ajouter_en_tete(copier_liste(queue(liste)), tete(liste))

# 4. Fonction rechercher
def rechercher(liste, nom):
    \"\"\"
    Recherche un sommet dans la liste par son nom.

    Paramètres :
    liste : Une liste simplement chaînée.
    nom (str) : Le nom du sommet à rechercher.

    Retourne :
    bool : True si le sommet est trouvé, False sinon.
    \"\"\"
    reste = liste
    while not est_vide(reste):
        sommet = tete(reste)
        if sommet.nom == nom:
            return True
        reste = queue(reste)
    return False

# 5. Fonction modifier_altitude
def modifier_altitude(liste, nom, nouvelle_altitude):
    \"\"\"
    Modifie l'altitude d'un sommet dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    nom (str) : Le nom du sommet à modifier.
    nouvelle_altitude (int) : La nouvelle altitude du sommet.
    \"\"\"
    reste = liste
    while not est_vide(reste):
        sommet = tete(reste)
        if sommet.nom == nom:
            sommet.altitude = nouvelle_altitude
            break
        reste = queue(reste)

# 6. Fonction supprimer_sommet
def supprimer_sommet(liste, nom):
    \"\"\"
    Supprime la première occurrence du sommet de nom donné dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    nom (str) : Le nom du sommet à supprimer.

    Retourne :
    Une liste simplement chaînée avec la première occurrence du sommet supprimée.
    \"\"\"
    if est_vide(liste):
        return liste
    elif tete(liste).nom == nom:
        return queue(liste)
    else:
        return ajouter_en_tete(supprimer_sommet(queue(liste), nom), tete(liste))

# 7. Fonction supprimer_sommets
def supprimer_sommets(liste, nom):
    \"\"\"
    Supprime toutes les occurrences du sommet de nom donné dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    nom (str) : Le nom du sommet à supprimer.

    Retourne :
    Une liste simplement chaînée avec toutes les occurrences du sommet supprimées.
    \"\"\"
    if est_vide(liste):
        return liste
    elif tete(liste).nom == nom:
        return supprimer_sommets(queue(liste), nom)
    else:
        return ajouter_en_tete(supprimer_sommets(queue(liste), nom), tete(liste))

# 8. Fonction longueur
def longueur(liste):
    \"\"\"
    Renvoie le nombre d'éléments de la liste simplement chaînée.

    Paramètres :
    liste : Une liste simplement chaînée.

    Retourne :
    int : Le nombre d'éléments dans la liste.
    \"\"\"
    if est_vide(liste):
        return 0
    else:
        return 1 + longueur(queue(liste))

# 9. Fonction inserer
def inserer(liste, element, rang):
    \"\"\"
    Insère un élément à un rang donné dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    element : L'élément à insérer.
    rang (int) : Le rang auquel insérer l'élément.

    Retourne :
    Une liste simplement chaînée avec l'élément inséré.
    \"\"\"
    if rang == 0:
        return ajouter_en_tete(liste, element)
    else:
        return ajouter_en_tete(inserer(queue(liste), element, rang - 1), tete(liste))

# 10. Fonction supprimer
def supprimer(liste, rang):
    \"\"\"
    Supprime un élément à un rang donné dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    rang (int) : Le rang de l'élément à supprimer.

    Retourne :
    Une liste simplement chaînée avec l'élément supprimé.
    \"\"\"
    if rang == 0:
        return queue(liste)
    else:
        return ajouter_en_tete(supprimer(queue(liste), rang - 1), tete(liste))

# 11. Fonction modifier
def modifier(liste, rang, element):
    \"\"\"
    Modifie un élément à un rang donné dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    rang (int) : Le rang de l'élément à modifier.
    element : Le nouvel élément à insérer à ce rang.

    Retourne :
    Une liste simplement chaînée avec l'élément modifié.
    \"\"\"
    if rang == 0:
        return ajouter_en_tete(queue(liste), element)
    else:
        return ajouter_en_tete(modifier(queue(liste), rang - 1, element), tete(liste))

# 12. Fonction rechercher_par_rang
def rechercher_par_rang(liste, element):
    \"\"\"
    Recherche l'élément dans la liste et retourne son rang.

    Paramètres :
    liste : Une liste simplement chaînée.
    element : L'élément à rechercher.

    Retourne :
    int : Le rang de l'élément ou -1 s'il n'est pas trouvé.
    \"\"\"
    reste = liste
    rang = 0
    while not est_vide(reste):
        if tete(reste) == element:
            return rang
        reste = queue(reste)
        rang += 1
    return -1

# 13. Fonction lire
def lire(liste, rang):
    \"\"\"
    Renvoie l'élément à un rang donné dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    rang (int) : Le rang de l'élément à lire.

    Retourne :
    L'élément à ce rang.
    \"\"\"
    if rang == 0:
        return tete(liste)
    else:
        return lire(queue(liste), rang - 1)

# 14. Fonction trier
def trier(liste, ordre=lambda x, y: x < y):
    \"\"\"
    Trie la liste dans un ordre donné.

    Paramètres :
    liste : Une liste simplement chaînée.
    ordre : Une fonction de comparaison, par défaut x < y.

    Retourne :
    Une liste simplement chaînée triée.
    \"\"\"
    if est_vide(liste):
        return liste
    else:
        pivot = tete(liste)
        sous_liste = queue(liste)

        # Séparer en deux listes
        inferieurs = creer_liste_vide()
        superieurs = creer_liste_vide()
        while not est_vide(sous_liste):
            elt = tete(sous_liste)
            if ordre(elt, pivot):
                inferieurs = ajouter_en_tete(inferieurs, elt)
            else:
                superieurs = ajouter_en_tete(superieurs, elt)
            sous_liste = queue(sous_liste)

        # Trier les sous-listes
        inferieurs = trier(inferieurs, ordre)
        superieurs = trier(superieurs, ordre)

        # Ajouter le pivot au résultat
        return ajouter_en_tete(superieurs, pivot)
"""

# Sauvegarder le fichier
path = "/home/spectre/Python/tp_listes_chaines/TP5.py"

