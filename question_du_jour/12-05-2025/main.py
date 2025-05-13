def force_brute(liste, i, j):
    summs = []
    for start in range(i, j):
        for end in range(start + 1, j + 1):
            summs.append(sum(liste[start:end]))
    return max(summs)


def somme_max(liste):
    max_actuel =  max_total = liste[0]
    for x in liste[1:]:
        max_actuel = max(x, max_actuel + x)
        max_total = max(max_total, max_actuel)
    return max_total


if __name__ == "__main__":
    liste = [4, -1, -2, 5, -2]
    m = force_brute(liste, 0, 5)
    print(m)
