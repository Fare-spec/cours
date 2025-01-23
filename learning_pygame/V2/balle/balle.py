import pygame
from constantes import *
import raquette
from math import *

class Balle(object):
    
    def __init__(self):
         self.rayon = 10
         self.xpos = LARGEUR_ECRAN/2
         self.ypos = HAUTEUR_ECRAN/2
         self.xvit =4.5
         self.yvit = 3.0
         
        
    def deplace(self,raquette):
        self.xpos += self.xvit
        self.ypos += self.yvit
        self.rebonds(raquette)
            
        
    def affiche(self, ecran):
        pygame.draw.circle(ecran,(0,0,0) , (int(self.xpos),int(self.ypos)) , self.rayon)
        
    def rebonds(self, raquette):
        if self.xpos + self.rayon > LARGEUR_ECRAN or self.xpos - self.rayon < 0:
            self.xvit = - self.xvit
        if self.ypos + self.rayon > HAUTEUR_ECRAN or self.ypos - self.rayon < 0:
            self.yvit = - self.yvit
            
        if self.ypos >= HAUTEUR_ECRAN-20:
            if self.xpos >= raquette.xpos:
                if self.xpos <= raquette.xpos + raquette.largeur :
                    self.yvit = - self.yvit
                    if self.xpos >= raquette.xpos + raquette.largeur - raquette.largeur/10:
                        self.xvit = 4.0
                        self.yvit = 6.0
                    
                if self.xpos <= raquette.xpos + raquette.largeur/20:
                    self.xvit = -4.0
                    self.yvit = 6.0