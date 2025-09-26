from main import dichotomie


def tester():
    liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    liste2 = liste1[:-1]
    liste3 = [7, 4, 1, 8, 5, 2, 9, 6, 3, 0]
    liste3_2 = [7, 7, 7, 7, 7, 7, 7, 8]
    liste4 = []
    liste5 = [1]
    liste6 = [1.0, 2.0, 3.1, 4.2, 8.6, 8.3]
    liste7 = [-1, -2, -2, -3, -4]
    liste8 = list(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )
    liste9 = [i for i in range(1, 100000)]
    assert dichotomie(liste1, 5) == True, "Test échoué : 5 devrait être dans liste1"
    assert (
        dichotomie(liste1, 11) == False
    ), "Test échoué : 11 ne devrait pas être dans liste1"

    # Tests pour liste2
    assert dichotomie(liste2, 9) == True, "Test échoué : 9 devrait être dans liste2"
    assert (
        dichotomie(liste2, 10) == False
    ), "Test échoué : 10 ne devrait pas être dans liste2"

    # Tests pour liste3
    assert dichotomie(liste3, 8) == True, "Test échoué : 8 devrait être dans liste3"
    assert (
        dichotomie(liste3, 11) == False
    ), "Test échoué : 11 ne devrait pas être dans liste3"

    # Tests pour liste3_2
    assert dichotomie(liste3_2, 7) == True, "Test échoué : 7 devrait être dans liste3_2"
    assert (
        dichotomie(liste3_2, 10) == False
    ), "Test échoué : 10 ne devrait pas être dans liste3_2"

    # Tests pour liste4
    assert (
        dichotomie(liste4, 1) == False
    ), "Test échoué : Liste vide, 1 ne devrait pas être dans liste4"
    assert (
        dichotomie(liste4, 0) == False
    ), "Test échoué : Liste vide, 0 ne devrait pas être dans liste4"

    # Tests pour liste5
    assert dichotomie(liste5, 1) == True, "Test échoué : 1 devrait être dans liste5"
    assert (
        dichotomie(liste5, 2) == False
    ), "Test échoué : 2 ne devrait pas être dans liste5"

    # Tests pour liste6
    assert dichotomie(liste6, 3.1) == True, "Test échoué : 3.1 devrait être dans liste6"
    assert (
        dichotomie(liste6, 5.5) == False
    ), "Test échoué : 5.5 ne devrait pas être dans liste6"

    # Tests pour liste7
    assert dichotomie(liste7, -3) == True, "Test échoué : -3 devrait être dans liste7"
    assert (
        dichotomie(liste7, 0) == False
    ), "Test échoué : 0 ne devrait pas être dans liste7"

    # Tests pour liste8
    assert dichotomie(liste8, "L") == True, "Test échoué : 'L' devrait être dans liste8"
    assert (
        dichotomie(liste8, "Z") == False
    ), "Test échoué : 'Z' ne devrait pas être dans liste8"

    # Tests pour liste9
    assert (
        dichotomie(liste9, 99999, True) == True
    ), "Test échoué : 99999 devrait être dans liste9"  # bypass = True because sorting_list is very slow
    assert (
        dichotomie(liste9, 0, True) == False
    ), "Test échoué : 5 ne devrait pas être dans liste9"  # bypass = True because sorting_list is very slow

    print("Tous les tests ont réussi !")


if __name__ == "__main__":
    tester()
