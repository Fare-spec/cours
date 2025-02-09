from Sommets import Sommet
from LSC import creer_liste_vide, ajouter_en_tete, afficher_liste

def csv2liste(fichier_csv):
    """
    Lit un fichier CSV et retourne une liste simplement chaînée des sommets.
    
    Paramètres :
    fichier_csv (str) : Le chemin vers le fichier CSV à lire.

    Retourne :
    Une liste simplement chaînée contenant les sommets.
    """
    liste_sommets = creer_liste_vide()
    with open(fichier_csv, 'r') as fichier:
        for ligne in fichier:
            nom, altitude = ligne.strip().split(',')
            sommet = Sommet(nom, int(altitude), 'Chartreuse')  # Modifier selon le massif si nécessaire
            liste_sommets = ajouter_en_tete(liste_sommets, sommet)
    return liste_sommets

# Test
liste_sommets = csv2liste('Chartreuse.csv')
afficher_liste(liste_sommets)
from LSC import est_vide, tete, queue, ajouter_en_tete

def copier_liste(liste):
    """
    Copie une liste simplement chaînée.

    Paramètres :
    liste : Une liste simplement chaînée.

    Retourne :
    Une copie de la liste.
    """
    if est_vide(liste):
        return creer_liste_vide()
    else:
        return ajouter_en_tete(copier_liste(queue(liste)), tete(liste))

# Test
copie = copier_liste(liste_sommets)
afficher_liste(copie)
def rechercher(liste, nom):
    """
    Recherche un sommet dans la liste par son nom.

    Paramètres :
    liste : Une liste simplement chaînée.
    nom (str) : Le nom du sommet à rechercher.

    Retourne :
    bool : True si le sommet est trouvé, False sinon.
    """
    reste = liste
    while not est_vide(reste):
        sommet = tete(reste)
        if sommet.nom == nom:
            return True
        reste = queue(reste)
    return False

# Test
print(rechercher(liste_sommets, "Chamechaude"))
def modifier_altitude(liste, nom, nouvelle_altitude):
    """
    Modifie l'altitude d'un sommet dans la liste.

    Paramètres :
    liste : Une liste simplement chaînée.
    nom (str) : Le nom du sommet à modifier.
    nouvelle_altitude (int) : La nouvelle altitude du sommet.
    """
    reste = liste
    while not est_vide(reste):
        sommet = tete(reste)
        if sommet.nom == nom:
            sommet.altitude = nouvelle_altitude
            break
        reste = queue(reste)

# Test
modifier_altitude(liste_sommets, "Chamechaude", 2082)
afficher_liste(liste_sommets)

