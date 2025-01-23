import pygame
from constantes import *

class Raquette:
    """
    Définit une raquette qui se déplace horizontalement
    dans le bas de la fenêtre écran.
    Attributs : largeur (int, par défaut 100), 
                xpos (int, par défaut LARGEUR_ECRAN//2 - largeur//2), 
                vit (int, par défaut 6)
    L'épaisseur de la raquette est de 10.
    Méthodes : deplaceGauche, deplaceDroite, affiche
    """

    def __init__(self):
        self.largeur = 100
        self.xpos = LARGEUR_ECRAN // 2 - self.largeur // 2
        self.vit = 6

    def deplaceGauche(self):
        """
        Déplace la raquette vers la gauche si possible.
        """
        self.xpos = max(0, self.xpos - self.vit)

    def deplaceDroite(self):
        """
        Déplace la raquette vers la droite si possible.
        """
        self.xpos = min(LARGEUR_ECRAN - self.largeur, self.xpos + self.vit)

    def affiche(self, ecran):
        """
        Dessine la raquette sur l'écran.
        """
        pygame.draw.rect(ecran, (0, 0, 255), (int(self.xpos), HAUTEUR_ECRAN - 20, self.largeur, 10))

if __name__ == '__main__':
	pass
