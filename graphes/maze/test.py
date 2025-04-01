from fifo import (
    Pile,
)  # Remplacez "fifo" par le nom exact de votre fichier contenant la classe Pile

# Initialisation
pile = Pile()

# Test de empiler
pile.empiler(5)
pile.empiler(10)
assert pile.size() == 2, "Erreur : La taille de la pile devrait être 2"
assert pile.element == [5, 10], "Erreur : Les éléments de la pile ne correspondent pas"

# Test de est_vide
assert not pile.est_vide(), "Erreur : La pile ne devrait pas être vide"
pile.defiler()
pile.defiler()
assert (
    pile.est_vide()
), "Erreur : La pile devrait être vide après avoir défiler tous les éléments"

# Test de defiler
pile.empiler(7)
pile.empiler(3)
assert pile.defiler() == 3, "Erreur : Le dernier élément défilé devrait être 3"
assert pile.defiler() == 7, "Erreur : Le dernier élément défilé devrait être 7"
try:
    pile.defiler()
    assert False, "Erreur : defiler devrait lever une exception pour une pile vide"
except AssertionError as e:
    pass  # Test réussi

# Test de size
pile.empiler(4)
assert pile.size() == 1, "Erreur : La taille de la pile devrait être 1"
pile.defiler()
assert pile.size() == 0, "Erreur : La taille de la pile devrait être 0 après defiler"

# Test de index
pile.empiler(1)
pile.empiler(2)
pile.empiler(3)
assert pile.index(0) == 1, "Erreur : L'élément à l'index 0 devrait être 1"
assert pile.index(2) == 3, "Erreur : L'élément à l'index 2 devrait être 3"
try:
    pile.defiler()
    pile.defiler()
    pile.defiler()
    pile.index(0)
    assert False, "Erreur : index devrait lever une exception pour une pile vide"
except AssertionError as e:
    pass  # Test réussi

print("Tous les tests sont passés avec succès !")
