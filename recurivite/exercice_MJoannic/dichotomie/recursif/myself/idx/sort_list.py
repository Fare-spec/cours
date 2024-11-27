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
