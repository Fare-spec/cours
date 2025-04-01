class Tableau:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def imin(self):
        return -len(self.gauche)

    def imax(self):
        return len(self.droite) - 1

    def append(self, elt):
        self.droite.append(elt)

    def prepend(self, elt):
        self.gauche.append(elt)

    def __getitem__(self, i):
        if i < 0:
            try:
                return self.gauche[i]
            except IndexError:
                print(f"erreur lors de l'index")
        else:
            try:
                return self.droite[i]
            except IndexError:
                print("error")

    def __setitem__(self, i, v):
        if i < 0:
            try:
                self.gauche[i] = v
            except IndexError:
                print("error")
        else:
            try:
                self.droite[i] = v
            except IndexError:
                print("error")

    def __str__(self) -> str:
        string = "|"
        for i in self.gauche:
            string += str(i) + "|"
        for i in self.droite:
            string += str(i) + "|"
        return string


if __name__ == "__main__":
    tab = Tableau([1, 2], [3, 4])
    tab.prepend(5)
    print(tab.__str__())
