class Niveau:
    def __init__(self) -> None:
        self.b1 = balle.Balle()
        self.r1 = raquette.Raquette()
        self.m1 = murdebrique.Wall()

    def affiche(self,ecran):
        ecran.fill(BLANC)
        self.b1.affiche(ecran)
        self.r1.affiche(ecran)
        self.m1.affiche(ecran)

    def levelmanager():
        for event in pygame.
