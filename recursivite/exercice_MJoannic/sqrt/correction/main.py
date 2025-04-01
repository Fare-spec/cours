def racine(n):
    def aux(gauche, droite):

        if gauche > droite:
            return droite

        milieu = (gauche + droite) // 2

        if milieu * milieu == n:
            return milieu

        elif milieu * milieu > n:
            return aux(gauche, milieu - 1)

        else:
            return aux(milieu + 1, droite)

    return aux(0, n)


def racine_decimale(n, precision=1e-6):

    def aux(gauche, droite):
        milieu = (gauche + droite) / 2

        if droite - gauche < precision:
            return milieu

        if milieu * milieu == n:
            return milieu

        elif milieu * milieu < n:
            return aux(milieu, droite)

        else:
            return aux(gauche, milieu)

    partie_entiere = racine(n)

    return aux(partie_entiere, partie_entiere + 1)
