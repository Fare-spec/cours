#!/usr/bin/python3
# -*- Coding: utf-8 -*-

class Graphe_Oriente(object):
	"""
	Classe des Graphes Orientés (GO).
	
	Les graphes sont représentés par 
	- une liste de sommets
	- leur liste d'adjacence

	Attributs (publics)
	- sommets : liste des sommets
	- voisins : dictionnaire des listes d'adjacence

	Méthodes (publiques)
	- ajoute_sommet : ajout d'un sommet
	- ajoute_arcs : ajout d'un arc
	"""

	def __init__(self):
		self.sommets = list()
		self.voisins = dict()
		return None

	def ajoute_sommet(self, s):
		"""
		Ajoute le sommet s à l'instance de GO.

		:param s data: etiquette du sommet
		"""

		self.sommets.append(s)
		self.voisins[s] = list()
		return None

	def ajoute_arc(self, origine, extremite):
		"""
		Ajoute l'arc origine -> extremite à l'instance de GO.

		:param self Graphe_Oriente: instance à laquelle ajouter un arc
		:param origine data: un sommet de l'instance, origine de l'arc
		:param extremite data: un sommet de l'instance, extremité de l'arc

		:return None:

		:effet de bord: Modification de l'instance

		:pré-condition: les sommets doivent exister
		"""
		assert origine in self.sommets, "{} inconnu".format(origine)
		assert extremite in self.sommets, "{} inconnu".format(extremite)
		self.voisins[origine].append(extremite)
		return None

def construire_chemins(graphe, depart):
	"""
	Construit tous les cheminement du graphe de depart donné

	:param graphe GO: graphe à parcourir
	:param depart data: sommet de départ dans le graphe

	:return resultat dict: dictionnaire
		- clef : sommet atteint
		- valeur : tuple (longueur itinéraire, sommet prédécesseur)

	:effet de bord: Aucun
	"""
	result = {
		depart: (0,None)
	}# distance 0 et aucun truc avant
	queue = [depart]



def reconstruire_chemin_vers(dico_chemins, *arrivee):
	"""
	Remonte tout l'itinéraire depuis un sommet fixé 
	vers un ou des sommets du graphe

	:param dico_chemins dict: table des longueurs/prédécessurs
	:param *arrivee: nombre quelconque de sommet à atteindre 
		(si vide, on considère tous les sommets)
	:return resultat list: liste des chemins ie des listes de sommets traversés
	"""
	pass

def affichage_chemin(chemin):
	"""
	Produit le texte d'affichage d'un chemin

	:param chemin list: liste des sommets constituant le chemin
	:return string: chemin mis en forme pour affichage
	"""
	long = len(chemin)-1
	return '{} etapes :\n'.format(long)+'\n\t-> '.join([str(sommet) for sommet in chemin])

# DEFINITION DES OPERATIONS DE TRANSITION

def vider(numero, etat):
	"""
	Vide un bidon

	:param numero INT: index du bidon
	:param etat tuple: etat des bidons avant l'opération
	:return tuple: nouvel etat aprés opération
	:effet de bord: aucun
	"""
	index_b = list(etat)
	index_b[numero] = 0
	return tuple(index_b)
def remplir(numero, etat, capacites):
	"""
	Remplit un bidon

	:param numero INT: index du bidon
	:param etat tuple: etat des bidons avant l'opération
	:return tuple: nouvel etat aprés opération
	:effet de bord: aucun
	"""
	cap = list(capacites)
	index_b = list(etat)
	index_b[numero] = cap[numero]
	return tuple(index_b)
	

def transvaser(source, destination, etat, capacites):
	"""
	Transvase un bidon dans un autre

	:param  origine int: index du bidon source
	:param  destination int: index du bidon destination
	:param etas tuple: etat des bidons avant l'opération
	:param capacites tuple: capacités des bidons
	:return tuple: nouvel etat aprés opération
	:effet de bord: aucun
	"""
	transfer_amount = min(list(etat)[source], list(capacites)[destination] - list(etat)[destination])
	new_state = list(etat)

	new_state[source] -= transfer_amount
	new_state[destination] += transfer_amount
	return tuple(new_state)
# FONCTION LIEES AU GRAPHE DU WATER_JUG

# Pour construire les etats
def produit_cartesien(*listes):
	"""
	Concatène les tuples issus des différentes listes

	:param *listes: un nombre quelconque de listes de tuples
	:return list: une liste des tuples concaténés

	Exemple :
	--------
	>>> produit_cartesien([(1,2), (3, 4)], [(5, 6), (7, 8,)])
	[(1, 2, 5, 6), (1, 2, 7, 8), (3, 4, 5, 6), (3, 4, 7, 8)]
	"""
	if listes == None:
		return []
	if len(listes) == 1:
		return listes[0]
	result = []
	for elt in listes[0]:
		for tuples in produit_cartesien(*listes[1:]):
			result.append(elt + tuples)
	return result

def creer_water_jug(*capacites):
	"""
	Création du graphe de Water Jug en fonction des capacités des bidons

	:param *capacites: capacités des bidons disponibles
	:return resultat GO: le graphe orienté du W_J
	:pre-condition: au moins 2 bidons

	:effet de bord: Aucun
	"""
	nb_bidons = len(capacites)
	assert nb_bidons >= 2, "Pas assez de bidons"
	resultat = Graphe_Oriente()
	# CREATION DES SOMMETS
	etats_marginaux = [[(contenu,) for contenu in range(1+capacite)] for capacite in capacites]
	etats_systeme = produit_cartesien(*etats_marginaux)
	for etat in etats_systeme:
		resultat.ajoute_sommet(etat)
	# CREATION DES TRANSITIONS
	for sommet in resultat.sommets:
		voisins = list()
		# VIDER
		for bidon in range(nb_bidons):
			voisin = vider(bidon, sommet)
			if voisin!=sommet and not(voisin in voisins):
				voisins.append(voisin)
		# REMPLIR
		for bidon in range(nb_bidons):
			voisin = remplir(bidon, sommet, capacites)
			if voisin != sommet and not(voisin in voisins):
				voisins.append(voisin)
		# TRANSVASER
		for origine in range(nb_bidons):
			for destination in range(nb_bidons):
				if origine != destination:
					voisin = transvaser(origine, destination, sommet, capacites)
					if voisin != sommet and not(voisin in voisins):
						voisins.append(voisin)
		# CREATION LISTES ADJACENCE
		for voisin in voisins:
			resultat.ajoute_arc(sommet, voisin)
	return resultat

def atteindre(quantite, graphe_water_jug, depart = None, plus_court=False):
	"""
	Résolution du problème pour une quantite donnée

	:param quantite int: la quantité à mesurer
	:param graphe_water_jug GO: le graphe de la situation
	:param depart tuple: etat initial, sommet d'origine dans le graphe 
		(bidons tous vides si depart est None, ie non fourni)
	:param plus_court bool: si vrai, seul le(s) plus court(s) chemin(s) 
		est (sont) retenu(s)

	:return list: la liste des tuples (sommet arrivee, nb d'etapes, ititneraire) ok
	"""
	if depart is None:
		nb_bidons = len(graphe_water_jug.sommets[0])
		depart = tuple([0 for i in range(nb_bidons)])
	chemins = construire_chemins(graphe_water_jug, depart)
	resultat = list()
	for sommet in chemins:
		if quantite in sommet:
			longueur, predecesseur = chemins[sommet]
			chemin = reconstruire_chemin_vers(chemins, sommet).pop()
			index = len(resultat)
			resultat.append((sommet, longueur, chemin))
			while index > 0 :
				if resultat[index-1][1]<longueur:
					break
				else :
					resultat[index], resultat[index-1]=resultat[index-1],resultat[index]
					index -= 1
	if len(resultat) < 2 or not(plus_court) :
		return resultat
	mini = resultat[0][1]
	return [element for element in resultat if element[1]==mini]

def main():
	pass

if __name__ == "__main__":
	main()
