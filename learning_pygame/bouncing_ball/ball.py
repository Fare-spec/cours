import sys, pygame
import balle
##########Definitions des constantes
# Taille de la fenetre
LARGEUR_ECRAN = 600 
HAUTEUR_ECRAN = 800
# Couleur
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

pygame.init()	#initialisation des modules de pygame

# Creation de la fenetre
ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
ecran.fill(BLANC) 

pygame.display.set_caption('Balle rebondissante')

clock = pygame.time.Clock()

b1 = balle.Balle()

bouge = False

while True:		#Demarrage de la boucle infinie
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	#Evt de sortie de boucle
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			bouge = not bouge
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			bouge = not bouge
			
			
	ecran.fill(BLANC) 
	if bouge:
		b1.deplace()
	b1.affiche(ecran)
	
	pygame.display.update() #rafraichissement
	clock.tick(60)

