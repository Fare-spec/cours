import pygame

class Balle :
	"""
		Definie une balle qui se deplace dans la fenetre ecran
		Attributs : rayon , xpos , ypos , xvit , yvit
		Methodes : deplace , affiche
	"""

	def __init__ ( self ) :
		self.rayon = 10
		self.xpos = 300.0
		self.ypos = 400.0
		self.xvit = 4.5
		self.yvit = 3.0

	def deplace ( self ) :
		self.xpos += self.xvit
		self.ypos += self.yvit
		if self.xpos + self.rayon > 600 or self.xpos - self.rayon < 0:
			self.xvit = - self.xvit
		elif self.ypos + self.rayon > 800 or self.ypos - self.rayon < 0:
			self.yvit = - self.yvit
