### D'après WIKIPEDIA
def racine_raphson(number: float, precision: float) -> float:
    assert number > 0, "La racine du nombre n'est pas réelle."

    y = (number / 3) + 1
    diff = precision + 1

    while diff > precision:
        y_next = (y + number / y) / 2.0
        diff = abs(y_next - y)
        y = y_next

    return y


if __name__ == "__main__":
    print(racine_raphson(36, 0.000000000000001) ** 2 == 36)


def dichotomie(
    liste: list[any],
    element: any,
    start: int = 0,
    end: int = None,
    bypass_sorting: bool = False,
) -> int:
    """Recherche la partie entière de la racine carrée d'un nombre en utilisant une recherche dichotomique.

    Args:
        liste (list[any]): Liste de nombres simulée pour la recherche.
        element (any): Le nombre dont on cherche la racine carrée entière.
        start (int, optional): Index de départ. Defaults to 0.
        end (int, optional): Index de fin. Defaults to None.
        bypass_sorting (bool, optional): Ignoré dans cette version.

    Returns:
        int: La partie entière de la racine carrée.
    """
    if end is None:
        end = len(liste) - 1

    if start > end:
        return end  # Retourne la partie entière trouvée.

    middle = (start + end) // 2
    squared = middle * middle

    if squared == element:
        return middle
    elif squared < element:
        return dichotomie(liste, element, middle + 1, end, bypass_sorting=True)
    else:
        return dichotomie(liste, element, start, middle - 1, bypass_sorting=True)


def racine_dich(number: int) -> int:
    """
    Calcul de la partie entière de la racine carrée d'un nombre entier.

    Args:
        number (int): Nombre dont on cherche la racine carrée.

    Returns:
        int: La partie entière de la racine carrée.
    """
    assert number >= 0, "Le nombre doit être positif ou nul."
    liste = [i for i in range(number // 2 + 2)]  # Simule une "liste" pour la dichotomie
    return dichotomie(liste, number)


if __name__ == "__main__":
    print(racine_dich(36))  # Retourne 6
    print(racine_dich(20))  # Retourne 4
    print(racine_dich(0))  # Retourne 0
    print(racine_dich(1))  # Retourne 1
