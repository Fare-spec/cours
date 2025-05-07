pyramide = [["x"], ["y", "z"], ["a", "b", "c"]]
# tableau triangulaire meilleur rendement avec un double boucle
# exemple:
# [1],[4,2],[9,7,3],[10,6,100,1]
# meilleur chemin 100, 7, 4, 1 (on ne peut pas faire 100 9 4 1 car 100 et 9 sont eloigner d'une distance > 1 au niveau de l'abcisse dans les étages)


def meilleur_rendement(pyramide: list[list[int]]):
    copie_l = [ligne for ligne in pyramide[::-1]]
    pyramide = pyramide[::-1]
    for i in range(1, len(pyramide)):
        for j in range(len(pyramide[i])):
            pyramide[i][j] += max(pyramide[i - 1][j], pyramide[i - 1][j + 1])
    return pyramide[-1][0]


def print_pyramide(pyramide):
    for l in pyramide:
        print(f"{l}\n")
    return None


if __name__ == "__main__":
    pyramide1 = [[1], [4, 2], [9, 7, 3], [10, 6, 100, 1]]
    print_pyramide(pyramide1[::-1])
    print(meilleur_rendement(pyramide1))
