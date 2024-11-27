```plaintext
maxi(liste)
precondition: |liste| > 0
    Resultat <- liste[0]
    index <- 1
    while index < |liste|
        if liste[index] > Resultat
            resultat <- liste[index]
        index <- index + 1
    Resultat
```
# Preuve de terminaison
    La terminaison est assuré par la présence d'un variant de boucle (séquence d'entier naturel). *ici* ```plaintext
|liste| - index 
```est un variant de boucles
