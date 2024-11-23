import LSC as lsc
from typing import Any

def creer_pile_vide() -> lsc.Liste_Simplement_Chainee:
    return lsc.creer_liste_vide()

def est_pile_vide(liste: lsc.Liste_Simplement_Chainee) -> bool:
    return lsc.est_vide(liste)

def sommet(liste: lsc.Liste_Simplement_Chainee) -> Any:
    return lsc.tete(liste)

def empiler(liste: lsc.Liste_Simplement_Chainee, element: Any) -> lsc.Liste_Simplement_Chainee:
    return lsc.ajouter_en_tete(liste,element)

def depiler(liste: lsc.Liste_Simplement_Chainee) -> lsc.Liste_Simplement_Chainee:
    return lsc.queue(liste)
