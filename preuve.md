```plaintext
maxi(liste)
precondition: |liste| > 0
    Resultat <- liste[0]
    index <- 1
    while index < |liste|
        if liste[index] > Resultat
            Resultat <- liste[index]
        index <- index + 1
    Resultat
```
# Preuve de terminaison
La terminaison est assuré par la présence d'un variant de boucle (séquence d'entier naturel). *ici* 
```plaintext
|liste| - index ```
est un variant de boucles


# Preuve de correction partielle
La correction partielle est assuré par *l'invariant de boucle* ici Resultat contient la valeur du plus grand élément de la liste entre les indices 0 et index - 1 inclus.
- Avant que le premier passage dans la boucle
Resultat contient liste[0]
index contient 1
q est le plus grand élément de la liste sur [0; index-1 = 0]

- Si à l'entrée dans la boucle invariant OK
resultat contient le maximum de la tranche de liste sur [0; index - 1]

## 1) Cas si liste[index] > Resultat
alors Resultat <- liste[index]
donc Resultat = max(liste[i])
i € [0; index]


## 2) Cas sinon liste[index]<= Resultat = max liste[i], i € [0;index - 1]
resultat = max(liste[i]) = Resultat
i € [0; index]
-----
index = index + 1

donc 
index = index - 1
-----
et 
--------                                   -----
Resultat contient le maxi de liste sur [0; index -1]
d'ou l'invariance 
# Conclusion 
l'algo se termine et, à la sortie, index = |liste|
et resultat contient le maxi de liste entre les index et |liste| - 1
