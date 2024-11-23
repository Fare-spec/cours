"""
Librairie des Listes Simplement Chaînées.

Elle met à distribution cette structure de données et son interface.

@author: L. JOANNIC
"""


# ############################################################################

class Liste_Simplement_Chainee(object):
    """
    Classe des Listes Simplement Chainees.

    Attributs
        - _tete : None si vide, Maillon sinon.

    Méthodes
        - est_vide
        - ajouter_en_tete
        - tete
        - queue
    """

    def __init__(self):
        """
        Construire une instance de Liste Simplement Chainee.

        Returns
        -------
        None.

        """
        self._tete = None
        return None

    def est_vide(self):
        """
        Tester si l'instance est vide.

        Returns
        -------
        bool
            Vrai ssi la liste est vide.

        """
        return (self._tete is None)

    def ajouter_en_tete(self, element):
        """
        Ajouter l'élément en tête de liste.

        Parameters
        ----------
        element : type de donnee
            Donnnée à ajouter à la liste.

        Returns
        -------
        resultat : Liste_Simplement_Chainee
            La liste à abonder.

        """
        resultat = Liste_Simplement_Chainee()
        resultat._tete = Maillon(element, self)
        return resultat

    def tete(self):
        """
        Renvoyer la donnée stockée en tête de liste.

        Returns
        -------
        type de donnee quelconque
            donnee en tete.

        """
        assert not(self.est_vide()), "Liste Vide"
        return self._tete.donnee

    def queue(self):
        """
        Renvoyer la sous-liste suivant le maillon de tete.

        Returns
        -------
        Liste_Simplement_Chainee
            Queue de la liste.

        """
        assert not(self.est_vide()), "Liste Vide"
        return self._tete.suite


# ############################################################################

def creer_liste_vide():
    """
    Créer une liste simplement chainee vide.

    Returns
    -------
    Liste_Simplement_Chainee
        Liste vide.

    Effets de bord
    --------------
        Aucun
    """
    return Liste_Simplement_Chainee()


def est_vide(liste):
    """
    Tester si la liste simplement chainee est vide.

    Parameters
    ----------
    liste : Liste Simplement Chainee
        Liste à tester.

    Returns
    -------
    bool
        Vrai ssi la liste est vide.

    Effets de bord
    --------------
        Aucun
    """
    return liste.est_vide()


def ajouter_en_tete(liste, element):
    """
    Inserer un element en tete de liste simplemeent chainee.

    Parameters
    ----------
    liste : LSC
        Liste à abonder.
    element : type de donnee
        Donnee à aouter.

    Returns
    -------
    LSC, copie de liste à laquelle element a été ajouté en tete.

    Effets de bord
    --------------
        Aucun
    """
    return liste.ajouter_en_tete(element)


def tete(liste):
    """
    Consulter la tete de liste.

    Parameters
    ----------
    liste : LSC
        Liste à consulter.

    Returns
    -------
    type de donnée
        valeur de la tete de liste.

    Effets de bord
    --------------
        Aucun
    """
    return liste.tete()


def queue(liste):
    """
    Renvoyer la liste sans sa tete.

    Parameters
    ----------
    liste : LSC
        Liste à étêter.

    Returns
    -------
    LSC
        Liste sans son maillon de tête.

    Effets de bord
    --------------
        Aucun
    """
    return liste.queue()


def afficher_liste(liste, taille=-1):
    """
    Afficher la liste en format de présentation.

    Parameters
    ----------
    liste : LSC
        Liste à énumérer.

    Returns
    -------
    None.

    Effets de bord
    --------------
        Affichage à l'écran.

    """
    reste = liste
    compteur = 0
    print('+-----\n|')
    while not(est_vide(reste)) and (taille == -1 or compteur < taille):
        print('+- {}\n|'.format(str(tete(reste))))
        reste = queue(reste)
        compteur += 1
    print('+-----')
    return None

# ############################################################################

class Maillon(object):
    """
    Classe des Maillons d'une Liste Simplement Chainee.

    Attributs
        - donnee : donnee stockee dans le maillon
        - suite : liste simplemement chainee suivant le maillon
    """

    def __init__(self, donnee=None, suite=Liste_Simplement_Chainee()):
        """
        Construire une instance de la classe des Maillons.

        Parameters
        ----------
        donnee : type de donnee, optional
            Donnee initiale dans le Maillon. The default is None.
        suite : LSC, optional
            Sous-liste suivant le Maillon courant.
            The default is Liste_Simplement_Chainee().

        Returns
        -------
        None.

        """
        self.donnee = donnee
        self.suite = suite
        return None


# ############################################################################
