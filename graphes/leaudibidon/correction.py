def produit_cartesien(*listes):
	if not listes:
		return []
	if len(listes) == 1:
		return listes[0]
	if len(listes) == 2:
		liste1, liste2 = listes
		resultat = list()
		for tuple_1 in liste1:
			for tuple_2 in liste2:
				resultat.append(tuple_1 + tuple_2)
		return resultat
	liste1, *reste = listes
	return produit_cartesien(liste1, produit_cartesien(*reste))



liste1 = [(_,) for _ in range(3)]
liste2 = [(_,) for _ in range(5)]
liste3 = [(_,)for _ in range(8)]
print(produit_cartesien(liste1,liste2))
	
