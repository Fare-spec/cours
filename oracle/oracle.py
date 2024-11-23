 
from tri import triage, triii
total_tests = 0
successes = 0
failures = 0

def run_test(func, input_data, expected_output, test_name):
    global total_tests, successes, failures
    total_tests += 1
    
    try:
        result = func(input_data)
        if result == expected_output:
            print(f"[SUCCÈS] {test_name}")
            successes += 1
        else:
            print(f"[ÉCHEC] {test_name}: attendu {expected_output}, mais obtenu {result}")
            failures += 1
    except Exception as e:
        print(f"[ERREUR] {test_name}: exception {e}")
        failures += 1

def test_triage():
    run_test(triage, [], [], "triage avec liste vide")
    run_test(triage, [5], [5], "triage avec un seul élément")
    run_test(triage, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "triage avec liste déjà triée")
    run_test(triage, [3, 1, 4, 2, 5], [1, 2, 3, 4, 5], "triage avec liste non triée")
    run_test(triage, [9, 3, 7, 1, 5], [1, 3, 5, 7, 9], "triage avec liste non triée aléatoire")

def test_triii():
    run_test(triii, [], [], "triii avec liste vide")
    run_test(triii, [7], [7], "triii avec un seul élément")
    run_test(triii, [1, 2, 3], [1, 2, 3], "triii avec liste déjà triée")
    run_test(triii, [3, 2, 1, 4], [1, 2, 3, 4], "triii avec liste non triée")
    run_test(triii, [6, 3, 9, 1, 2], [1, 2, 3, 6, 9], "triii avec liste non triée aléatoire")

if __name__ == '__main__':
    print("Tests pour la fonction triage:")
    test_triage()
    print("\nTests pour la fonction triii:")
    test_triii()


    print("\n--- Résumé des tests ---")
    print(f"Total de tests exécutés : {total_tests}")
    print(f"Tests réussis : {successes}")
    print(f"Tests échoués : {failures}")

    if failures == 0:
        print("Tous les tests ont réussi !")
    else:
        print(f"{failures} tests ont échoué.")