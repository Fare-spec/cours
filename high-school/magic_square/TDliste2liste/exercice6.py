def diag_1(carre):
    return [carre[i][i] for i in range(len(carre))]


def diag_2(carre):
    n = len(carre)
    return [carre[i][n - 1 - i] for i in range(n)]


def colonne(j, carre):
    return [carre[i][j] for i in range(len(carre))]
