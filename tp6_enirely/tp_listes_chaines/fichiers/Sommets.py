#! /usr/bin/python3
# coding=utf-8

"""
Ce fichier contient la définition des objets Sommets.

Un sommet dispose 

- des attributs
  + nom
  + altitude
  + massif
- des méthodes 
  + __lt__ : inférieur
  + __le__ : inférieur ou égal
  + __eq__ : égal
  + __ge__ : supérieur ou égal
  + __gt__ : supérieur
  + __repr__ : représentation (affichage)
"""


# ############################################################################

class Sommet(object):
    """
    Classe des Sommets montagneux.

    Attributs
        - nom : STR, nom du sommet
        - altitude : INT, altitude en mètres
        - massif : STR, nom du massif d'appartenance

    Méthodes
        - comparaison
        - représentation

    """

    def __init__(self, nom, altitude, massif):
        """
        Construire une instance de la classe Sommet.

        Parameters
        ----------
        nom : str
            nom du sommet.
        altitude : int
            altitude en m.
        massif : str
            massif d'appartenance.

        Returns
        -------
        None.

        """
        self.nom = nom
        self.altitude = altitude
        self.massif = massif
        return None

    def __repr__(self):
        """
        Construire l'affichage d'une instance de Sommet.

        Returns
        -------
        str
            chaine formattée d'affichage.

        """
        if self.altitude < 1000:
            altitude = str(self.altitude)
        else:
            altitude = str(self.altitude)
            altitude = altitude[:-3]+' '+altitude[-3:]
        return "{:<35s} [ {:^10s} ] :\t{:>10s} m".format(self.nom, self.massif, altitude)

    def __str__(self):
        """
        Construire la chaîne de caractères résumant
        une instance de Sommet.

        Returns
        -------
        str
            chaine formattée d'affichage.

        """
        if self.altitude < 1000:
            altitude = str(self.altitude)
        else:
            altitude = str(self.altitude)
            altitude = altitude[:-3]+' '+altitude[-3:]
        return "{:<35s} [ {:^10s} ] :\t{:>10s} m".format(self.nom, self.massif, altitude)


    def __gt__(self, other):
        """
        Strictement plus grand.

        Parameters
        ----------
        other : Sommet
            Sommet à comparer.

        Returns
        -------
        boolean
            Resultat du test.

        """
        return (self.altitude > other.altitude)\
            or ((self.altitude == other.altitude) and (self.nom > other.nom))

    def __lt__(self, other):
        """
        Strictement plus petit.

        Parameters
        ----------
        other : Sommet
            Sommet à comparer.

        Returns
        -------
        boolean
            Resultat du test.

        """
        return (self.altitude < other.altitude)\
            or ((self.altitude == other.altitude) and (self.nom < other.nom))

    def __eq__(self, other):
        """
        Est égal à.

        Parameters
        ----------
        other : Sommet
            Sommet à comparer.

        Returns
        -------
        boolean
            Resultat du test.

        """
        return (self.altitude == other.altitude)

    def __ge__(self, other):
        """
        Plus grand ou égal.

        Parameters
        ----------
        other : Sommet
            Sommet à comparer.

        Returns
        -------
        boolean
            Resultat du test.

        """
        return (self > other) or (self == other)

    def __le__(self, other):
        """
        Plus petit ou égal.

        Parameters
        ----------
        other : Sommet
            Sommet à comparer.

        Returns
        -------
        boolean
            Resultat du test.

        """
        return (self < other) or (self == other)


# ############################################################################

if __name__ == '__main__':
    s = Sommet('Chamechaude', 2062, 'Chartreuse')
    print(s)
