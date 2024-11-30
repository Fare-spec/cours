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
    liste8 = list("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    liste9 = [i for i in range(1, 100000)]
    
    # Tests pour liste1
    assert dichotomie(liste1, 5) == 4, "Test échoué : 5 devrait être à l'index 4 dans liste1"
    print("Test n°1 réussi")
    assert dichotomie(liste1, 11) == -1, "Test échoué : 11 ne devrait pas être dans liste1"
    print("Test n°2 réussi")

    # Tests pour liste2
    assert dichotomie(liste2, 9) == 8, "Test échoué : 9 devrait être à l'index 8 dans liste2"
    print("Test n°3 réussi")
    assert dichotomie(liste2, 10) == -1, "Test échoué : 10 ne devrait pas être dans liste2"
    print("Test n°4 réussi")
    '''
    # Tests pour liste3 (tri nécessaire)
    assert dichotomie(liste3, 8) == 7, "Test échoué : 8 devrait être à l'index 7 après tri dans liste3"
    print("Test n°5 réussi")
    assert dichotomie(liste3, 11) == -1, "Test échoué : 11 ne devrait pas être dans liste3"
    print("Test n°6 réussi")
    '''
    # Tests pour liste3_2
    assert dichotomie(liste3_2, 7) == 3, "Test échoué : 7 devrait être dans liste3_2"
    print("Test n°7 réussi")
    assert dichotomie(liste3_2, 10) == -1, "Test échoué : 10 ne devrait pas être dans liste3_2"
    print("Test n°8 réussi")

    # Tests pour liste4
    print(dichotomie(liste4,1))
    assert dichotomie(liste4, 1) == -1, "Test échoué : Liste vide, 1 ne devrait pas être dans liste4"
    print("Test n°9 réussi")
    assert dichotomie(liste4, 0) == -1, "Test échoué : Liste vide, 0 ne devrait pas être dans liste4"
    print("Test n°10 réussi")

    # Tests pour liste5
    assert dichotomie(liste5, 1) == 0, "Test échoué : 1 devrait être à l'index 0 dans liste5"
    print("Test n°11 réussi")
    assert dichotomie(liste5, 2) == -1, "Test échoué : 2 ne devrait pas être dans liste5"
    print("Test n°12 réussi")

    # Tests pour liste6
    assert dichotomie(liste6, 3.1) == 2, "Test échoué : 3.1 devrait être à l'index 2 dans liste6"
    print("Test n°13 réussi")
    assert dichotomie(liste6, 5.5) == -1, "Test échoué : 5.5 ne devrait pas être dans liste6"
    print("Test n°14 réussi")

    # Tests pour liste7 (tri nécessaire)
    assert dichotomie(liste7, -3) == 1, "Test échoué : -3 devrait être à l'index 1 après tri dans liste7"
    print("Test n°15 réussi")
    assert dichotomie(liste7, 0) == -1, "Test échoué : 0 ne devrait pas être dans liste7"
    print("Test n°16 réussi")

    # Tests pour liste8
    assert dichotomie(liste8, "A") == 0, "Test échoué : 'L' devrait être à l'index 0 dans liste8"
    print("Test n°17 réussi")
    assert dichotomie(liste8, "Z") == -1, "Test échoué : 'Z' ne devrait pas être dans liste8"
    print("Test n°18 réussi")
    
    # Tests pour liste9 (tri déjà fait)
    assert dichotomie(liste9, 99999, bypass_sorting=True) == 99998, "Test échoué : 99999 devrait être à l'index 99998 dans liste9"
    print("Test n°19 réussi")
    assert dichotomie(liste9, 0, bypass_sorting=True) == -1, "Test échoué : 0 ne devrait pas être dans liste9"
    print("Test n°20 réussi")

    print("Tous les tests ont réussi !")


if __name__ == '__main__':
    tester()
