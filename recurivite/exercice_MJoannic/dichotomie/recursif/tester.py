from main import dichotomie
def tester():
    liste1 = [1,2,3,4,5,6,7,8,9,10]
    liste2 = liste1[:-1]
    liste3 = [7,4,1,8,5,2,9,6,3,0]
    liste3_2 = [7,7,7,7,7,7,7,8]
    liste4 = []
    liste5 = [1]
    liste6 = [1.0,2.0,3.1,4.2,8.6,8.3]
    liste7 = [-1,-2,-2,-3,-4]
    liste8 = list("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    liste9 = [i for i in range(1,100000)]
    
    # Tests pour liste1
    assert dichotomie(liste1, 5) == True, "Test �chou� : 5 devrait �tre dans liste1"
    print("Test n�1 done")
    assert dichotomie(liste1, 11) == False, "Test �chou� : 11 ne devrait pas �tre dans liste1"
    print("Test n�2 done")

    # Tests pour liste2
    assert dichotomie(liste2, 9) == True, "Test �chou� : 9 devrait �tre dans liste2"
    print("Test n�3 done")
    assert dichotomie(liste2, 10) == False, "Test �chou� : 10 ne devrait pas �tre dans liste2"
    print("Test n�4 done")

    # Tests pour liste3
    assert dichotomie(liste3, 8) == True, "Test �chou� : 8 devrait �tre dans liste3"
    print("Test n�5 done")
    assert dichotomie(liste3, 11) == False, "Test �chou� : 11 ne devrait pas �tre dans liste3"
    print("Test n�6 done")

    # Tests pour liste3_2
    assert dichotomie(liste3_2, 7) == True, "Test �chou� : 7 devrait �tre dans liste3_2"
    print("Test n�7 done")
    assert dichotomie(liste3_2, 10) == False, "Test �chou� : 10 ne devrait pas �tre dans liste3_2"
    print("Test n�8 done")

    # Tests pour liste4
    assert dichotomie(liste4, 1) == False, "Test �chou� : Liste vide, 1 ne devrait pas �tre dans liste4"
    print("Test n�9 done")
    assert dichotomie(liste4, 0) == False, "Test �chou� : Liste vide, 0 ne devrait pas �tre dans liste4"
    print("Test n�10 done")

    # Tests pour liste5
    assert dichotomie(liste5, 1) == True, "Test �chou� : 1 devrait �tre dans liste5"
    print("Test n�11 done")
    assert dichotomie(liste5, 2) == False, "Test �chou� : 2 ne devrait pas �tre dans liste5"
    print("Test n�12 done")

    # Tests pour liste6
    assert dichotomie(liste6, 3.1) == True, "Test �chou� : 3.1 devrait �tre dans liste6"
    print("Test n�13 done")
    assert dichotomie(liste6, 5.5) == False, "Test �chou� : 5.5 ne devrait pas �tre dans liste6"
    print("Test n�14 done")

    # Tests pour liste7
    assert dichotomie(liste7, -3) == True, "Test �chou� : -3 devrait �tre dans liste7"
    print("Test n�15 done")
    assert dichotomie(liste7, 0) == False, "Test �chou� : 0 ne devrait pas �tre dans liste7"
    print("Test n�16 done")

    # Tests pour liste8
    assert dichotomie(liste8, "L") == True, "Test �chou� : 'L' devrait �tre dans liste8"
    print("Test n�17 done")
    assert dichotomie(liste8, "Z") == False, "Test �chou� : 'Z' ne devrait pas �tre dans liste8"
    print("Test n�18 done")
    
    # Tests pour liste9
    assert dichotomie(liste9, 99999, bypass_sorting=True) == True, "Test �chou� : 99999 devrait �tre dans liste9"
    print("Test n�19 done")
    assert dichotomie(liste9, 0, bypass_sorting=True) == False, "Test �chou� : 0 ne devrait pas �tre dans liste9"
    print("Test n�20 done")

    print("Tous les tests ont reussi !")


if __name__ == '__main__':
    tester()
