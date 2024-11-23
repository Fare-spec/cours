def transpose(carre):
    n = len(carre)  # Nombre de lignes (ou colonnes, car c'est une matrice carrée)
    return [[carre[j][i] for j in range(n)] for i in range(n)]

def transpose_en_place(carre):
    n = len(carre)  # Nombre de lignes (ou colonnes)
    for i in range(n):
        for j in range(i + 1, n):  # Commencer à j = i + 1 pour éviter de réécrire les éléments déjà transposés
            carre[i][j], carre[j][i] = carre[j][i], carre[i][j]  # Échange des éléments
