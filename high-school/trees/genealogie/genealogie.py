Genealogie = [
    ["Henri IV", 1553, 1610, "1589-1610", [1]],
    ["Louis XIII", 1601, 1643, "1610-1643", [2, 3]],
    ["Louis XIV", 1638, 1715, "1643-1715", [4]],
    ["Philippe Ier, duc d'Orleans", 1640, 1701, "", [15]],
    ["Louis le Grand Dauphin", 1661, 1711, "", [5, 6]],
    ["Louis, duc de Bourgogne", 1682, 1712, "", [7]],
    ["Philippe V, roi d'Espagne", 1683, 1746, "", []],
    ["Louis XV", 1710, 1774, "1715-1774", [8]],
    ["Louis, Dauphin", 1729, 1765, "", [9, 10, 11]],
    ["Louis XVI", 1754, 1793, "1754-1793", [13]],
    ["Louis XVIII", 1755, 1824, "1815-1824", []],
    ["Charles X", 1756, 1832, "1824-1830", []],
    ['Louis-Philippe-Joseph "Philippe Egalite"', 1747, 1793, "", [14]],
    ["Louis XVII", 1785, 1795, "", []],
    ["Louis-Philippe Ier, roi des Français", 1773, 1850, "", []],
    ["Philippe II", 1674, 1723, "", [16]],
    ["Louis, duc d'Orleans", 1703, 1752, "", [17]],
    ["Louis-Philippe Ier, duc d'Orleans", 1725, 1785, "", [12]],
]


def creer_arbre():
    return ()


def est_vide(arbre):
    return arbre == () or arbre is None


def rechercher(arbre, valeur):
    if not (est_vide(arbre)):
        racine, enfants = arbre
        if racine == valeur:
            return arbre
        resultat = creer_arbre()
        for ss_arbre in enfants:
            resultat = rechercher(ss_arbre, valeur)
            if not (est_vide(resultat)):
                break
        return resultat
    return arbre


def ajouter_enfant(arbre, enfant, cle_parent):
    if est_vide(arbre):
        return enfant
    return arbre.insert(cle_parent + 1, enfant)


Bourbons = [
    ["Nom", "naissance", "mort", "règne"],
    ["Henri IV", 1553, 1610, "1589-1610"],
    ["Louis XIII", 1601, 1643, "1610-1643"],
    ["Louis XIV", 1638, 1715, "1643-1715"],
    ["Philippe, duc d'Orleans", 1640, 1701, ""],
    ["Louis le Grand Dauphin", 1661, 1711, ""],
    ["Louis, duc de Bourgogne", 1682, 1712, ""],
    ["Philippe V, roi d'Espagne", 1683, 1746],
    ["Louis XV", 1710, 1774, "1715-1774"],
    ["Louis, Dauphin", 1729, 1765, ""],
    ["Louis XVI", 1754, 1793, "1765-1792"],
    ["Louis XVIII", 1755, 1824, "1814-1824"],
    ["Charles X", 1756, 1832, "1824-1830"],
    ['Louis-Philippe-Joseph "Philippe Egalite"', 1747, 1793, ""],
    ["Louis XVII", 1785, 1795, ""],
    ["Louis Philippe Ier", 1773, 1850, "1830-1848"],
]

Genealogie = (
    1,
    [
        (
            2,
            [
                (
                    3,
                    [
                        (
                            5,
                            [
                                (6, [(8, [(9, [(10, [14]), (11, []), (12, [])])])]),
                                (7, []),
                            ],
                        )
                    ],
                ),
                (4, []),
            ],
        )
    ],
)
print("ENUMERATION :")
for rg, bourbon in enumerate(Bourbons):
    print(rg, bourbon[0])
print()
print("RECHERCHE :")
print(rechercher(Genealogie, 8))


class Arbre(object):
    def __init__(self, racine=None, ss_arbres=[]) -> None:
        self.racine = racine
        self.ss_arbres = ss_arbres

    def est_vide(self):
        return self.racine == None

    def rechercher(self, valeur):
        if not (self.est_vide()):
            if self.racine == valeur:
                return self
            resultat = Arbre()
            for ss_arbre in self.ss_arbres:
                ss_arbre = Arbre(racine=None, ss_arbres=ss_arbre)
                resultat = ss_arbre.rechercher(valeur)
                if not (resultat == None):
                    break
            return resultat
        return Arbre()

    def ajouter(self, elt):
        if self.est_vide():
            return Arbre(racine=elt)
        else:
            return Arbre(elt, self)

    def enlever(self, elt):
        pass

    def display(self):
        pass
