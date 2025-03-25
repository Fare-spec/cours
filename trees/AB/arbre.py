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
                self.racine =next
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
    print(liste1) # on observer que la liste devient triée (logique car on la trie pour la mettre dans l'arbre et on ne peut pas la recupérer comme si elle ne l'etait pas)

    # Exercice 5 ?
    pass
