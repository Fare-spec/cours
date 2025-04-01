import sys, pygame
import balle
import raquette
from constantes import *

pygame.init()

# Creation de la fenetre
ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))

# Titre de la fenetre
pygame.display.set_caption("Casse_Brique")

clock = pygame.time.Clock()

b1 = balle.Balle()
r1 = raquette.Raquette()
bouge = False
bouge_gauche_raquette = False
bouge_droite_raquette = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bouge = not bouge

    if pygame.key.get_pressed()[pygame.K_q]:
        r1.deplaceGauche()
    if pygame.key.get_pressed()[pygame.K_d]:
        r1.deplaceDroite()

    ecran.fill(BLANC)

    if bouge:
        b1.deplace(r1)

    b1.deplace(r1)
    b1.affiche(ecran)
    r1.affiche(ecran)
    pygame.display.update()
    clock.tick(60)
