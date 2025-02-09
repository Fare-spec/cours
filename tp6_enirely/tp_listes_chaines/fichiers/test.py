import LSC as lc
import csv
import Sommets as sm
liste = lc.creer_liste_vide()
with open("Chartreuse.csv", mode="r",encoding='utf-8') as f:
    lecteur_csv = csv.reader(f)
    for ligne in lecteur_csv:
        nom = ligne[0].strip()
        altitude_str = ligne[1].strip()
        altitude = int(altitude_str.replace('m', '').replace(' ', ''))
        sommet = sm.Sommet(nom, altitude, "Chartreuse")
        liste = lc.ajouter_en_tete(liste, sommet)
    lecteur_csv = csv.reader(f)
    for ligne in lecteur_csv:
        nom = ligne[0].strip()
        altitude_str = ligne[1].strip()
        altitude = int(altitude_str.replace('m', '').replace(' ', ''))
        sommet = sm.Sommet(nom, altitude, "Chartreuse")
        liste = lc.ajouter_en_tete(liste, sommet)
lc.afficher_liste(liste.queue())
liste1 = liste.tete()
print(liste1[0])
