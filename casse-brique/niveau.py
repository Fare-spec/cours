import sys, pygame
import balle, raquette, murdebrique
from constantes import *


class Niveau:
    """gère le jeu d'un niveau"""

    def __init__(self):
        self.b1 = balle.Balle()
        self.r1 = raquette.Raquette()
        self.m1 = murdebrique.Murdebrique()

    def affiche(self, ecran):
        ecran.fill(BLANC)
        self.b1.affiche(ecran)
        self.r1.affiche(ecran)
        self.m1.affiche(ecran)

    def gereNiveau(self, ecran):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Evt de sortie de boucle
                sys.exit()
        if pygame.key.get_pressed()[pygame.K_q] == True:
            self.r1.deplaceGauche()
        if pygame.key.get_pressed()[pygame.K_d] == True:
            self.r1.deplaceDroite()

        self.b1.deplace(self.r1)
        self.m1.collision(self.b1)
        self.affiche(ecran)
        return 2
