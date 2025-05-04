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
    return sum(elt[1]["Durée"] for elt in partie)


def total_taille(partie):
    return sum(elt[1]["Taille"] for elt in partie)


def sac_a_dos_force_brute(videos, capacite):
    meilleur = ([], 0, 0.0)
    for partie in ensemble_des_parties(videos):
        taille = total_taille(partie)
        duree = total_duree(partie)
        if taille <= capacite and duree > meilleur[1]:
            meilleur = ([v[0] for v in partie], duree, taille)
    return meilleur


# Glouton
def sac_a_dos_glouton(videos, capacite, cle):
    tri = sorted(videos, key=cle, reverse=True)
    sélection = []
    totale_taille = 0.0
    totale_duree = 0
    for nom, info in tri:
        if totale_taille + info["Taille"] <= capacite:
            sélection.append(nom)
            totale_taille += info["Taille"]
            totale_duree += info["Durée"]
    return sélection, totale_duree, totale_taille


def sac_a_dos_dynamique(videos, capacite):
    precision = 100
    capacite = int(capacite * precision)
    liste = list(videos.items())
    n = len(liste)
    dp = [[0] * (capacite + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        nom, info = liste[i - 1]
        duree = info["Durée"]
        taille = int(info["taille"] * precision)
        for cap in range(capacite + 1):
            if taille <= cap:
                dp[i][cap] = max(dp[i - 1][cap], duree + dp[i - 1][cap - taille])
            else:
                dp[i][cap] = dp[i - 1][cap]
    cap = capacite
    selection = []
    for i in range(n, 0, -1):
        if dp[i][cap] != dp[i - 1][cap]:
            nom, info = liste[i - 1]
            selection.append(nom)
            cap -= int(info["taille"] * precision)
    return selection[::-1]


if __name__ == "__main__":
    # Conversion du dictionnaire des vidéos en liste
    liste_videos = dico_vers_liste(Videos)
    # Affichage de contrôle
    for video in liste_videos:
        print(video)
    opt_brut, dur_brut, taille_brut = sac_a_dos_force_brute(liste_videos, 5.0)
    print("--- Force brute ---")
    print(
        f"Vidéos : {opt_brut}\nDurée : {dur_brut} min\nTaille : {taille_brut:.3f} Go\n"
    )
    h_duree = lambda x: x[1]["Durée"]
    h_taille = lambda x: -x[1]["Taille"]
    h_ratio = lambda x: x[1]["Durée"] / x[1]["Taille"]
    selection_duree, dur_duree, taille_duree = sac_a_dos_glouton(
        liste_videos, 5.0, h_duree
    )
    selection_taille, dur_taille, taille_taille = sac_a_dos_glouton(
        liste_videos, 5.0, h_taille
    )
    selection_ratio, dur_ratio, taille_ratio = sac_a_dos_glouton(
        liste_videos, 5.0, h_ratio
    )
    print("--- Glouton par durée décroissante ---")
    print(
        f"Vidéos : {sel_duree}\nDurée : {dur_duree} min\nTaille : {taille_duree:.3f} Go\n"
    )
    print("--- Glouton par taille croissante ---")
    print(
        f"Vidéos : {sel_taille}\nDurée : {dur_taille} min\nTaille : {taille_taille:.3f} Go\n"
    )
    print("--- Glouton par ratio durée/taille ---")
    print(
        f"Vidéos : {sel_ratio}\nDurée : {dur_ratio} min\nTaille : {taille_ratio:.3f} Go\n"
    )
    videos_mb = [
        (nom, (info["Durée"], int(round(info["Taille"] * 1000))))
        for nom, info in liste_videos
    ]
    capacite_mb = 5000
    n = len(videos_mb)
    dp = [[0] * (capacite_mb + 1) for _ in range(n + 1)]
