class Arbre_Binaire(object):
    def __init__(self, racine=None, sag=None, sad=None) -> None:
        self.racine = racine
        self.ss_arbre_gauche = sag
        self.ss_arbre_droit = sad
        return None

    def est_vide(self):
        return self.racine is None

    def taille(self):
        if self.est_vide():
            return 1
        else:
            taille_gauche = self.ss_arbre_gauche.taille() if self.ss_arbre_gauche else 0
            taille_droite = self.ss_arbre_droit.taille() if self.ss_arbre_droit else 0

        return 1 + taille_gauche + taille_droite

    def hauteur(self):
        if self.est_vide():
            return 0
        else:
            profondeur_gauche = (
                self.ss_arbre_gauche.hauteur() if self.ss_arbre_gauche else 0
            )
            profondeur_droite = (
                self.ss_arbre_droit.hauteur() if self.ss_arbre_droit else 0
            )
        return 1 + max(profondeur_droite, profondeur_gauche)

    def parcours_largeur(self):
        if self.est_vide():
            return None
        file = [(self, 0)]
        niveaux = {}
        while file:
            noeud, niveau = file.pop(0)
            if niveau not in niveaux:
                niveaux[niveau] = []
            niveaux[niveau].append(noeud.racine)
            if noeud.ss_arbre_gauche:
                file.append((noeud.ss_arbre_gauche, niveau + 1))
            if noeud.ss_arbre_droit:
                file.append((noeud.ss_arbre_droit, niveau + 1))
        return niveaux


class Arbre_Binaire_Recherche(Arbre_Binaire):
    def __init__(self) -> None:
        self.racine = None
        self.ss_arbre_droit = None
        self.ss_arbre_gauche = None

    def insertion(self, element):
        if self.est_vide():
            self.racine = element
            self.ss_arbre_gauche = (
                Arbre_Binaire_Recherche()
            )  # pour eviter l'erreur NoneType has no attribut 'insertion'
            self.ss_arbre_droit = Arbre_Binaire_Recherche()  # pareil
        elif element <= self.racine:
            self.ss_arbre_gauche.insertion(element)
        else:
            self.ss_arbre_droit.insertion(element)

    def recherche(self, valeur):
        if self.est_vide():
            return False
        if element == valeur:
            return True
        elif element < self.racine:
            return self.ss_arbre_gauche.recherche(element)
        else:
            return self.ss_arbre_droit.recherche(element)

    def ajouter(self, valeur):
        """
        même code qu insertion
        """
        if self.est_vide():
            self.racine = valeur
            self.ss_arbre_droit = Arbre_Binaire_Recherche()
            self.ss_arbre_gauche = Arbre_Binaire_Recherche()
        elif valeur <= self.racine:
            self.ss_arbre_gauche.ajouter(valeur)
        else:
            self.ss_arbre_droit.ajouter(valeur)

    def mini(self):
        """
        cette fonction sert a trouver le minimum d'un sous arbre on l'utilise notamment pour la suppression d'un noeud dans un arbre contenant des "enfants"...
        """
        a = self
        while not a.ss_arbre_gauche.est_vide():
            a = a.ss_arbre_gauche
        return a.racine

    def supprimer(self, valeur):
        if self.est_vide():
            return Arbre_Binaire_Recherche()

        if element < self.racine:
            self.ss_arbre_gauche = self.ss_arbre_gauche.supprimer(valeur)
        elif element > self.racine:
            self.ss_arbre_droit = self.ss_arbre_droit.supprimer(valeur)
        else:
            if self.ss_arbre_gauche.est_vide() and self.ss_arbre_droit.est_vide():
                return Arbre_Binaire_Recherche()
            elif self.ss_arbre_droit.est_vide():
                return self.ss_arbre_droit
            elif self.ss_arbre_gauche.est_vide():
                return self.ss_arbre_gauche
            else:
                next = self.ss_arbre_droit.mini()
                self.racine = next
                self.ss_arbre_droit = self.ss_arbre_droit.supprimer(next)

    def abr_vers_liste(self):
        if self.est_vide():
            return []

        gauche = self.ss_arbre_gauche.abr_vers_liste() if self.ss_arbre_gauche else []
        droite = self.ss_arbre_droit.abr_vers_liste() if self.ss_arbre_droit else []

        return gauche + [self.racine] + droite


def affiche(arbre, traitement):
    if arbre and not arbre.est_vide():
        if traitement == "prefixe":
            print(arbre.racine)
        affiche(arbre.ss_arbre_gauche, "prefixe")
        if traitement == "infixe":
            print(arbre.racine)
        affiche(arbre.ss_arbre_droit, "infixe")
        if traitement == "postfixe":
            print(arbre.racine)


def list_to_btree(liste):
    if not liste:
        return Arbre_Binaire()
    else:
        racine = Arbre_Binaire_Recherche()
        for elt in liste[1:]:
            racine.insertion(elt)
        return racine


if __name__ == "__main__":
    arbre = Arbre_Binaire(1, Arbre_Binaire(2), Arbre_Binaire(3))
    print("taille arbre :", arbre.taille())
    print("hauteur arbre :", arbre.hauteur())

    liste = [18, 11, 19, 73, 12, 1, 20, 5, 23, 8, 10, 29]
    arbre = list_to_btree(liste)
    affiche(arbre, "prefixe")
    liste1 = arbre.abr_vers_liste()
    print(
        liste1
    )  # on observer que la liste devient triée (logique car on la trie pour la mettre dans l'arbre et on ne peut pas la recupérer comme si elle ne l'etait pas)

tas = [1, 5, 8, 10, 11, 12, 18, 19, 20, 23, 29, 73]


def ajouter(tas, element):
    tas.append(element)
    i = len(tas) - 1

    while i > 0:
        parent = (i - 1) // 2
        if tas[i] < tas[parent]:
            tas[i], tas[parent] = tas[parent], tas[i]
            i = parent
        else:
            break


# nlog(n)
class Tas_Max(object):
    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def enfant_gauche(i):
        return 2 * i + 1

    @staticmethod
    def enfant_droite(i):
        return 2 * i + 2

    def __init__(self) -> None:
        self.elements = list()
        self.taille = 0

    def existe_enfant_gauche(self, i):
        return 2 * i + 1 < self.taille

    def existe_enfant_droit(self, i):
        return 2 * i + 2 < self.taille

    def tamiser(self, racine):
        while racine > 0 and self.elements[racine] > self.elements[parent(raicne)]:
            self.elements[racine], self.element[parent(racine)] = (
                self.elements[parent(racine)],
                self.elements[racine],
            )

    def ratisser(self, racine):
        courant = racine
        if (
            self.existe_enfant_gauche(racine)
            and self.elements[enfant_gauche(racine)] > self.element[racine]
        ):
            courant = enfant_gauche(racine)
        if (
            self.existe_enfant_droit(racine)
            and self.elements[enfant_droit(racine)] > self.elements[courant]
        ):
            courant = enfant_droit(racine)
        if courant != racine:
            self.elements[racine], self.elements[courant] = (
                self.elements[courant],
                self.elements[racine],
            )

    def ajouter(self, element):
        self.elements.append(element)
        self.taille += 1
        self.tamiser(self.taille)
        return None

    def extraire_racine(self):
        if self.taille == 0:
            return None
        racine = self.elements[0]
        if self.taille > 0:
            self.elements[0] = self.elements.pop()
            self.ratisser(0)
        else:
            self.elements.pop()
        return racine


def liste_vers_tas_max(liste):
    tas = Tas_Max()
    for i in liste:
        tas.ajouter(i)
    return tas


def tas_max_vers_liste(tas):
    resultat = []
    while tas.taille > 0:
        resultat.append(tas.extraire_racine())
    return resultat


def convertir_liste_en_tas(liste):
    def ratisser(elements, taille, i):
        plus_grand = i
        g = 2 * i + 1
        d = 2 * i + 2

        if g < taille and elements[g] > elements[plus_grand]:
            plus_grand = g
        if d < taille and elements[d] > elements[plus_grand]:
            plus_grand = d
        if plus_grand != i:
            elements[i], elements[plus_grand] = elements[plus_grand], elements[i]
            ratisser(elements, taille, plus_grand)

    n = len(liste)
    for i in range(n // 2 - 1, -1, -1):
        ratisser(liste, n, i)


if __name__ == "__main__":
    l1 = [1, 2, 3, 8, 7, 6, 5, 4]
    tas = liste_vers_tas_max(l1)
