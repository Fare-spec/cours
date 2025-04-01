def creer_file_vide():
    """
    Crée une nouvelle file vide.

    Returns:
        list: Une liste vide représentant la file.
    """
    return []


def est_vide(file):
    """
    Vérifie si une file est vide.

    Args:
        file (list): La file à vérifier.

    Returns:
        bool: `True` si la file est vide, `False` sinon.
    """
    return len(file) == 0


def enfiler(file, elt):
    """
    Ajoute un élément à la fin de la file.

    Args:
        file (list): La file à laquelle ajouter l'élément.
        elt: L'élément à ajouter.

    Returns:
        None
    """
    return file.append(elt)


def defiler(file: list):
    """
    Retire et renvoie le premier élément de la file.

    Args:
        file (list): La file dont l'élément de tête doit être retiré.

    Returns:
        list: La file sans le premier élément.
    """
    return file[1:]


def peak(file: list):
    """
    Renvoie l'élément en tête de la file sans le retirer.

    Args:
        file (list): La file dont on veut consulter le premier élément.

    Returns:
        L'élément en tête de la file.
    """
    return file[0]
