from sort_list import sort_list
from typing import Any

def dichotomie(liste: list[Any], element: Any, start: int = 0, end: int = None, bypass_sorting: bool = False) -> int:
    """Performs a dichotomy search to determine if an element exists in a list or not.

    Args:
        liste (list[Any]): The list in which to search for the element.
        element (Any): The element to search for.
        start (int, optional): The starting index of the sublist to search. Defaults to 0.
        end (int, optional): The ending index of the sublist to search. Defaults to None.
        bypass_sorting (bool, optional): If True, skips sorting the list. Defaults to False.

    Returns:
        int: retourne l'indexe de l'element si il est trouver
    """
    if not liste:
        return -1

    assert isinstance(element, type(liste[0])), "Wrong type between liste and element"

    if not bypass_sorting:
        liste = sort_list(liste)

    if end is None:
        end = len(liste) - 1
    if start > end:
        return -1

    middle = (start + end) // 2

    if liste[middle] == element:
        return middle
    elif element < liste[middle]:
        return dichotomie(liste, element, start, middle - 1, bypass_sorting=True) # bypass_sorting because it's already done
    else:
        return dichotomie(liste, element, middle + 1, end, bypass_sorting=True) # bypass_sorting because it's already done
