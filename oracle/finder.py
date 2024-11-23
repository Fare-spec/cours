from tri import triii


def dichotomie_maximum(arr: list):
    """cherche le maximum d'une liste triée de façon dichotomique

    Args:
        arr (list): la liste contenant le maximum

    Returns:
        int: le maximum
    """
    arr = triii(arr)
    if not arr:
        return None
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return arr[left]

def dichotomie_minimum(arr: list)->int:
    """cherche le minimum d'une liste de façon dichotometrique trier !

    Args:
        arr (list): la liste

    Returns:
        int: le minimum
    """
    arr = triii(arr)
    if not arr:
        return None
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return arr[left]

def trouver_indice_dichotomie(arr, x):
    """cherche l'élement x dans une liste arr

    Args:
        arr (list): la liste
        x (int): l'élement

    Returns:
        int: l'indice de l'element dans la liste ou -1 s'il est absent
    """
    arr = sorted(arr)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return None



liste = [i for i in range(20000)]
print(trouver_indice_dichotomie(liste,5624))

