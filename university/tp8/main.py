from mailbox import linesep

import board as bd


def creerGrille(N, M, v=0):
    return bd.gen_grid(N, M, v)


def placerMine(grid, X):
    bd.place_mine(grid, X)


def TestMine(grid, i, j):
    return bd.test_mine(grid, (i, j))


def compteMinesVoisines(positionsMines, i, j):
    return bd.get_neighbours((i, j), positionsMines)


def afficheSolution(positionsMines):
    bd.display_mines(positionsMines)


def afficheJeu(positionsMines, casesDevoilees):
    bd.display_known(positionsMines, casesDevoilees)


def getCoords(known_grid, N, M):
    return bd.get_coords(known_grid)


def main() -> None:
    N, M = 8, 8
    grid = creerGrille(N, M)
    mines_number = 0
    while not (0 < mines_number <= N * M - 1):
        mines_number = int(
            input(f"Please input a number of mines between 0-{N * M - 1}: ")
        )
    # In theory we should put the line below after the first pick on the board or else the user could loose on their first attempt
    placerMine(grid, mines_number)
    known_grid = [[False for _ in range(N)] for _ in range(M)]
    going = True
    while going:
        afficheJeu(grid, known_grid)
        y, x = getCoords(known_grid, N, M)
        known_grid[y][x] = True
        # If the user lost:
        if TestMine(grid, y, x):
            print("You lost")
            afficheJeu(grid, known_grid)
            print("Here is the solution: ")
            afficheSolution(grid)
            going = False
        # If he won
        elif bd.is_end(known_grid, grid):
            print("Congrats ! You've just won")
            going = False
        else:
            linked = bd.linked_cells(grid, known_grid, (y, x))
            for coord in linked:
                known_grid[coord[1]][coord[0]] = True


main()
