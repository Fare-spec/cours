def cree_carre_entier_1_n_carre(n):
    carre = []
    compteur = 1
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(compteur)
            compteur += 1
        carre.append(ligne)
    return carre


print(cree_carre_entier_1_n_carre(8))
