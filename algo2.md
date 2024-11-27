```Plaintext
somme(liste)
somme = 0
idx = 0
while idx < |liste|
    somme = somme + liste[idx]
    idx = idx + 1
```

# Myself
## Preuve de terminaison
La *Terminaison* est assurée par un variant de boucle (ici idx < |liste| est un variant de boucle)
```plaintext
|liste| - idx
```
est ici l'ivariant de boucle

## Preuve de correction partielle
La correction partielle est assurée par *l'invariant de boucle* ici Somme contient toutes les valeurs de la liste ajouter les unes aux autres ? par
```Plaintext
somme = somme + liste[idx]
```
## Conclusion L'algo se termine et, à la sortie, idx = |liste| et somme contient tous les elements de la liste additionés entre eux
