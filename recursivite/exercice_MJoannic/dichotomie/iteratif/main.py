from sort_list import sort_list

def dichotomie(liste: list, element: any,bypass_sorting = False)->bool:
    """This function return return True if element is in liste False else

    Args:
        liste (list): the array to examinate
        element (any): the element to find into liste
        bypass_sorting (bool, optional):If True, skips sorting the list. Defaults to False.
    Returns:
        bool: True if present False else
    """
    if liste == []:
        return False
    assert type(element) == type(liste[0]), "Wrong type between liste and element" # On estime que la liste contient un seul et unique type...
    if bypass_sorting == False:
        liste = sort_list(liste)
    N, start, find,i = len(liste)-1, 0, False, 0
    end = N
    while (find != True) and (start <= end):
        middle = (start + end)//2
        if liste[middle] == element:
            find = True

        elif element > liste[middle]:
            start = middle+1
        else:
            end = middle - 1
    return find
