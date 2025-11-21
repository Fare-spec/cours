import board as bd


# 4.8.1.1 : création de la grille
def creerGrille(N, M, v=0):
    """Crée une grille N x M initialisée à la valeur v."""
    return bd.gen_grid(N, M, v)


# 4.8.1.2 : placement des mines
def placerMines(grid, X):
    """Place X mines (valeur 1) dans la grille à des positions aléatoires."""
    bd.place_mine(grid, X)


# 4.8.2.1 : test d'une mine
def testMine(grid, i, j):
    """Renvoie True s'il y a une mine à la case (i, j)."""
    return bd.test_mine(grid, (i, j))


# 4.8.2.2 : compte des mines voisines
def compteMinesVoisines(positionsMines, i, j):
    """Renvoie le nombre de mines voisines de la case (i, j)."""
    return bd.count_near_mines(positionsMines, (i, j))


# 4.8.3.1 : affichage de la solution
def afficheSolution(positionsMines):
    """Affiche la grille solution : '-' pour vide, '*' pour mine."""
    bd.display_mines(positionsMines)


# 4.8.3.2 : affichage du jeu
def afficheJeu(positionsMines, casesDevoilees):
    """
    Affiche la grille telle que vue par le joueur :
    '?' pour inconnue, '*' pour mine découverte,
    nombre de mines voisines autrement.
    """
    bd.display_known(positionsMines, casesDevoilees)


# 4.8.4.1 : lecture filtrée du nombre de mines
def getNbMines(N, M):
    """
    Lit et renvoie un nombre de mines X tel que 1 <= X <= N*M - 1.
    Évite le cas où le placement serait impossible.
    """
    max_mines = N * M - 1
    nb = 0
    while not (1 <= nb <= max_mines):
        try:
            nb = int(input(f"Nombre de mines (entre 1 et {max_mines}) ? "))
        except ValueError:
            nb = 0
    return nb


# 4.8.4.2 : lecture filtrée des coordonnées
def getCoords(casesDevoilees, N, M):
    """
    Demande à l'utilisateur des coordonnées (ligne, colonne) :
    - dans les bornes,
    - sur une case non encore dévoilée.
    Ne redemande que la coordonnée incorrecte.
    Renvoie (i, j) correctes.
    """
    max_i = N - 1
    max_j = M - 1

    i = -1
    j = -1

    while True:
        # Lecture de la ligne
        while not (0 <= i <= max_i):
            try:
                if i == -1:
                    i = int(input("Ligne? "))
                else:
                    i = int(input(f"Ligne < {N} svp ? "))
            except ValueError:
                i = -1

        while not (0 <= j <= max_j):
            try:
                if j == -1:
                    j = int(input("Colonne? "))
                else:
                    j = int(input(f"Colonne < {M} svp ? "))
            except ValueError:
                j = -1

        if not casesDevoilees[i][j]:
            return i, j

        print("Case deja devoilee, recommence")
        i = -1
        j = -1


def main():
    """
    Programme principal :
    - initialise une grille,
    - demande le nombre de mines,
    - lance la boucle de jeu,
    - s'arrête quand le joueur perd ou gagne.
    """
    N, M = 8, 8
    grid = creerGrille(N, M)
    nb_mines = getNbMines(N, M)
    placerMines(grid, nb_mines)

    # Grille des cases dévoilées : N lignes, M colonnes
    casesDevoilees = [[False for _ in range(M)] for _ in range(N)]

    nb_coups = 0
    en_cours = True

    while en_cours:
        nb_coups += 1
        print(f"Coup numero {nb_coups}")
        afficheJeu(grid, casesDevoilees)
        print("A toi de jouer !")

        i, j = getCoords(casesDevoilees, N, M)
        casesDevoilees[i][j] = True

        # Mine touchée -> perdu
        if testMine(grid, i, j):
            print("Perdu, touche une mine !")
            afficheJeu(grid, casesDevoilees)
            print("La solution etait :")
            afficheSolution(grid)
            en_cours = False
        else:
            # Expansion façon démineur (bonus, pas demandé mais utile)
            linked = bd.linked_cells(grid, casesDevoilees, (i, j))
            for cy, cx in linked:
                casesDevoilees[cy][cx] = True
            # Fin de partie
            if bd.is_end(casesDevoilees, grid):
                afficheJeu(grid, casesDevoilees)
                print(f"Tu as gagne en {nb_coups} coups, bravo !")
                en_cours = False


if __name__ == "__main__":
    main()
