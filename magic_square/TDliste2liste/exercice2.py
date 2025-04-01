def max_local(tableau):
    maximum = tableau[0]
    for i in tableau:
        if i > maximum:
            maximum = i
        else:
            continue
    return maximum


def indice_max(tableau):
    maximum = max_local(tableau)
    for i in range(len(tableau)):
        if tableau[i] == maximum:
            return i
        else:
            continue


if __name__ == "__main__":
    l1 = [0, 2, 3, 4, 5, 6, 7, 8, 9, 90, 91, 59, 1]
    print(max_local(l1))
    print(indice_max(l1))
