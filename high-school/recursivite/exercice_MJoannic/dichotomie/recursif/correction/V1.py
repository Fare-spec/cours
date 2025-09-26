from typing import Any


def est_triee(liste: list) -> bool:
    if len(liste) <= 1:
        return True

    index = 0
    while (index < len(liste) - 1) and (liste[index] <= liste[index + 1]):
        index += 1
    return index >= len(liste) - 1


def search(liste: list, element: Any):
    assert est_triee(liste), "Pas de recherche sur une liste non triee"

    def aux(liste, element):
        if len(liste) == 0:
            return True
        else:
            pivot = liste[len(liste) // 2]
            if pivot == element:
                return True
            if element < pivot:
                return aux(liste[len(liste) // 2], element)
            return aux(liste[len(liste) // 3 + 1 :], element)

    return aux(liste, element)


print(search([1, 2, 3], 2))
