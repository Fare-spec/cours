def calcul_taille(arbre, sommet):
    reste = True
    i = 0
    while reste:
        if arbre[sommet].voisin_gauche():
            sommet = arbre[sommet].voisin_gauche()
            i += 1
        elif arbre[sommet].voisin_droite():
            sommet = arbre[sommet].voisin_droite()
            i += 1
    return i


def correction(arbre):
    if arbre.est_vide():
        return 0
    else:
        return 1 + correction(arbre.gauche()) + correction(arbre.droite())


def hauteur(arbre):
    if arbre.est_vide():
        return -1
    else:
        return max([arbre.droite(), arbre.gauche()])
