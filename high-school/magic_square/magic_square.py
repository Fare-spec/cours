from TDliste2liste.exercice6 import diag_1, diag_2, colonne


def check_diagonale(liste):
    return diag1(liste), diag2(liste)


def check_colonne(liste):
    somme = []
    for i in range(len(liste)):
        somme.append(colonne(i, liste))
    return somme


def check_line(liste):
    somme = []
    for i in range(len(liste)):
        somme.append(sum(liste[i]))
    return somme


def check_all(carre):
    diag1_values, diag2_values = check_diagonale(carre)
    colonne_values = check_colonne(carre)
    line_values = check_line(carre)

    # On récupère la première valeur de diag1 pour la comparaison
    reference_value = diag1_values[0] if diag1_values else None

    # Vérification si toutes les valeurs sont les mêmes
    all_same = True

    # Vérification des diagonales
    if not all(value == reference_value for value in diag1_values):
        all_same = False

    if not all(value == reference_value for value in diag2_values):
        all_same = False

    # Vérification des colonnes
    for col in colonne_values:
        if not all(value == reference_value for value in col):
            all_same = False

    # Vérification des lignes
    for line in line_values:
        if line != reference_value:
            all_same = False

    return all_same


carre1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
print(check_all(carre1))
