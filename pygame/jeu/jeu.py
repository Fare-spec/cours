from pygame.jeu import niveau


class Jeu:
    def __init__(self) -> None:
        self.niveau = niveau.Niveau()
        self.vie = 3
        self.bouge = False
        self.etat = 1

    def gereJeu(self,ecran):
        if self.etat == 1:
            pass
        elif self.etat == 2:
            for event in pygame.event.get():
                if event.type() == pygame.QUIT:
                    sys.exit
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.bouge = True
                else:
                    self.bouge = True
            niveau.affiche(ecran)
            if self.bouge:
                self.etat = 1
                return 1
        elif self.etat == 2:
            self.etat = niveau.
