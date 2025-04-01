import pygame
from constantes import *


class Raquette:
    """
    Definie une raquette qui se deplace horizontalement
    dans le bas de la fenetre ecran
    Attributs : largeur (int defaut 100),
                            xpos (int defaut LARGEUR_ECRAN//2 - self.largeur//2),
                            vit (int defaut 6)
    L'épaisseur de la raquette est de 10
    Methodes : deplaceGauche, deplaceDroite, affiche
    """

    def __init__(self):
        self.largeur = 100
        self.xpos = LARGEUR_ECRAN // 2 - self.largeur // 2
        self.vit = 6

    def deplaceGauche(self):
        """
        Deplace la raquette de vit vers la gauche
        Parametres :
                self : Raquette
        Return :
                None
        Effet de bord :
                Modifie l'attribut xpos en lui enlevant,
                si c'est possible la valeur de vit (et met xpos à 0 sinon)
        """
        self.xpos -= self.vit
        if self.xpos < 0:
            self.xpos = 0

    def deplaceDroite(self):
        """
        Deplace la raquette de vit vers la droite
        Parametres :
                self : Raquette
        Return :
                None
        Effet de bord :
                Modifie l'attribut xpos en lui ajoutant,
                si c'est possible la valeur de vit (et met xpos à
                600-self.largeur sinon sinon)
        """
        self.xpos += self.vit
        if self.xpos > LARGEUR_ECRAN - self.largeur:
            self.xpos = LARGEUR_ECRAN - self.largeur

    def affiche(self, ecran):
        pygame.draw.rect(
            ecran, (0, 0, 255), (int(self.xpos), HAUTEUR_ECRAN - 20, self.largeur, 10)
        )


if __name__ == "__main__":
    pass
