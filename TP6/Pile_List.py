from typing import Any


def creer_pile_vide():
    return []


def est_pile_vide(pile: list):
    return len(pile) == 0


def sommet(pile: list):
    return pile[-1]


def empiler(pile: list, element: Any):
    return pile + [element]


def depiler(pile: list):
    return pile[:-1]
