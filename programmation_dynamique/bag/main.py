Videos = {
    "Video 1": {"Durée": 114, "Taille": 4.57},
    "Video 2": {"Durée": 32, "Taille": 0.63},
    "Video 3": {"Durée": 20, "Taille": 1.65},
    "Video 4": {"Durée": 4, "Taille": 0.085},
    "Video 5": {"Durée": 18, "Taille": 2.15},
    "Video 6": {"Durée": 80, "Taille": 2.71},
    "Video 7": {"Durée": 5, "Taille": 0.32},
}


def dico_vers_liste(dico: dict) -> list:
    """
    Conversion d'un dictionnaire en liste.
    PARAM. :
    - dico : DICT, dictionnaire à applatir
    RESULT. :
    - LIST, chaque élément de la liste est un tuple (cle, valeur) du dictionnaire.
    PRECOND. :
    - aucune
    EFFET DE BORD :
    - aucun

    """
    return list(
        dico.items()  # j'ai remplacer le code de base qui contenait Videos a la place de dico dans le return
    )


def entier_vers_binaire(n: int, taille: int) -> list:
    """
    Conversion d'un entier en binaire sur une taille donnée.
    PARAM. :
    - n : INT, le nombre à convertir
    - taille : INT, la taille (nb de bits) fixe de la représentation
    RESULT. :
    - LIST, la liste des bits de la représentation en binaire,
    indexée par le poids
    PRECONDITION :
    - n < 2**taille : un entier >= 2**taille n'est pas représentable
    dans la taille donnée
    EFFET DE BORD :
    - aucun
    """
    assert 2**taille > n, "Taille de représentation trop petite"
    bits = [0] * taille
    for i in range(taille):
        bits[i] = (n >> i) & 1

    return bits


def ensemble_des_parties(ensemble: list) -> iterator:
    """
    Construit l'itérable enumérant toutes les parties d'un ensemble.
    PARAM. :
    - ensemble : LIST, la liste des éléments de l'ensemble
    RESULT. :
    - ITERATOR, le générateur de toutes les parties de l'ensemble
    PRECONDITION :
    - aucune
    EFFET DE BORD :
    - aucun
    """
    n = len(ensemble)
    for mask in range(2**n):
        partie = [ensemble[i] for i in range(n) if (mask >> i) & 1]
        yield partie

def total_duree(partie):
    return sum(elt[1]['Durée'] for elt in partie)
def total_taille(partie):
    return sum(elt[1]['Taille'] for elt in partie)
    
def sac_a_dos_force_brute(videos, capacite):
    meilleur = ([], 0, 0.0)
    for partie in ensemble_des_parties(videos):
        taille = total_taille(partie)
        duree = total_duree(partie)
        if taille <= capacite and duree > meilleur[1]:
            meilleur = ([v[0] for v in partie], duree, taille)
    return meilleur

if __name__ == "__main__":
    # Conversion du dictionnaire des vidéos en liste
    liste_videos = dico_vers_liste(Videos)
    # Affichage de contrôle
    for video in liste_videos:
        print(video)
