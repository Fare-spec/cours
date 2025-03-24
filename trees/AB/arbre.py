class Arbre_Binaire(object):
    def __init__(self,racine = None, sag = None,sad = None) -> None:
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

        return 1+taille_gauche+taille_droite

    def hauteur(self):
        if self.est_vide():
            return 0
        else:
            profondeur_gauche = self.ss_arbre_gauche.hauteur() if self.ss_arbre_gauche else 0
            profondeur_droite = self.ss_arbre_droit.hauteur() if self.ss_arbre_droit else 0
        return 1+max(profondeur_droite,profondeur_gauche)

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
def affiche(arbre, traitement):
    if arbre:
        sag,racine,sad = arbre
        if traitement == 'prefixe':
            print(racine)
        affiche(sag,"prefixe")
        if traitement == "infixe":
            print(racine)
        affiche(sad,"infixe")
        if traitement == "postfixe":
            print(racine)
def list_to_btree(liste):
    if not liste:
        return Arbre_Binaire()
    else:
        racine = Arbre_Binaire(racine=liste[0])
        for elt in liste[1:]:
            racine.insertion(elt) # besoin de insertion
        return racine
if __name__ == "__main__":
    arbre = Arbre_Binaire(1, Arbre_Binaire(2), Arbre_Binaire(3))
    print("taille arbre :", arbre.taille())
    print("hauteur arbre :", arbre.hauteur())
