def sort_list(liste: list) -> list:
    """this function sort a liste

    Args:
        liste (list): the list to sort

    Returns:
        list: the list sorted
    """
    for i in range(len(liste)):
        min_index = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]

    return liste


def dichotomie(liste: list, element: any,bypass_sorting = False)->bool:
    """This function return return True if element is in liste False else

    Args:
        liste (list): the array to examinate
        element (any): the element to find into liste

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