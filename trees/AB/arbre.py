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
def affichage(arbre):
    pass
    if arbre.est_vide():
        return ([])
    else:
        racine = arbre.racine
        prefixe = arbre.ss_arbre_gauche
        suffixe = arbre.ss_arbre_droit
    #todo


if __name__ == "__main__":
    arbre = Arbre_Binaire(1, Arbre_Binaire(2), Arbre_Binaire(3))
    print("taille arbre :", arbre.taille())
    print("hauteur arbre :", arbre.hauteur())
