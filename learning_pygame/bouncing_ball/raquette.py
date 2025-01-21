import sys
import pygame
from balle import Balle
from raquette import Raquette
from constantes import *

pygame.init()

# Création de la fenêtre
ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
ecran.fill(BLANC)
pygame.display.set_caption('Balle rebondissante avec raquette')

clock = pygame.time.Clock()

# Initialisation des objets
balle = Balle()
raquette = Raquette()

bouge = False

while True:  # Boucle principale
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bouge = not bouge
            elif event.key == pygame.K_LEFT:
                raquette.deplaceGauche()
            elif event.key == pygame.K_RIGHT:
                raquette.deplaceDroite()

    ecran.fill(BLANC)

    if bouge:
        balle.deplace()

    # Collision balle-raquette
    if (balle.ypos + balle.rayon >= HAUTEUR_ECRAN - 20 and
            raquette.xpos <= balle.xpos <= raquette.xpos + raquette.largeur):
        balle.yvit = -balle.yvit

    balle.affiche(ecran)
    raquette.affiche(ecran)

    pygame.display.update()
    clock.tick(60)

