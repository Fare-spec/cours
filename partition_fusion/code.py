def partition(tab, debut, fin):
    pivot = tab[fin]
    i = debut - 1
    for j in range(debut, fin):
        if tab[j] <= pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[fin] = tab[fin], tab[i + 1]
    return i + 1

def fusion(tab, debut, milieu, fin):
    gauche = tab[debut:milieu + 1]
    droite = tab[milieu + 1:fin + 1]
    i, j, k = 0, 0, debut

    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            tab[k] = gauche[i]
            i += 1
        else:
            tab[k] = droite[j]
            j += 1
        k += 1

    while i < len(gauche):
        tab[k] = gauche[i]
        i += 1
        k += 1

    while j < len(droite):
        tab[k] = droite[j]
        j += 1
        k += 1

def tri_fusion_partition(tab, debut, fin):
    if debut < fin:
        pivot_index = partition(tab, debut, fin)
        tri_fusion_partition(tab, debut, pivot_index - 1)
        tri_fusion_partition(tab, pivot_index + 1, fin)
        fusion(tab, debut, pivot_index, fin)

tableau = [34, 7, 23, 32, 5, 62, 32, 8, 9]
tri_fusion_partition(tableau, 0, len(tableau) - 1)
print("Tableau trié :", tableau)

