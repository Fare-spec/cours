def cree_tableau_n_m(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


def cree_tableau_carre_n(n):
    return [[0 for _ in range(n)] for _ in range(n)]


if __name__ == "__main__":
    print(cree_tableau_n_m(3, 5))
    print(cree_tableau_carre_n(5))
