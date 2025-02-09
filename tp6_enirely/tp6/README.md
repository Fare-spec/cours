# Devoir Maison : Gestion de Piles et Notation Polonaise Inverse

Ce devoir présente des fonctions pour manipuler des piles et évaluer des expressions en notation polonaise inverse (NPI).

## Prérequis

Pour exécuter ce devoir, vous aurez besoin de :

- [Python 3.x](https://www.python.org/downloads/) installé sur votre machine.

### Installation de Python

1. **Téléchargez Python** : Allez sur le [site officiel de Python](https://www.python.org/downloads/) et téléchargez la dernière version stable pour votre système d'exploitation.

2. **Installez Python** : Suivez les instructions d'installation. Assurez-vous de cocher l'option "Add Python to PATH" lors de l'installation sur Windows.

3. **Vérifiez l'installation** : Ouvrez votre terminal ou votre invite de commande et exécutez la commande suivante :
    ```bash
    python --version
    ```
   Cela devrait afficher la version de Python installée.

## Utilisation des Modules

### Modules Fournis

Le devoir contient les modules suivants :

- `LSC` : Implémentation d'une liste simplement chaînée.
- `Pile_LSC` : Implémentation d'une pile utilisant une liste simplement chaînée.
- `Tuple` : Implémentation d'une pile utilisant un tuple.
- `Liste` : Implémentation d'une pile utilisant une liste.

#### Primitives du Module `LSC`

- `creer_liste_vide()`: Crée une liste vide.
- `est_vide(liste)`: Vérifie si la liste est vide.
- `ajouter_en_tete(liste, element)`: Ajoute un élément au début de la liste.
- `queue(liste)`: Retire le premier élément de la liste.
- `tete(liste)`: Renvoie le premier élément de la liste.

#### Primitives du Module `Pile_LSC`

- `creer_pile_vide()`: Crée une pile vide sous forme de liste simplement chaînée.
- `est_pile_vide(pile)`: Vérifie si la pile est vide.
- `sommet(pile)`: Renvoie l'élément au sommet de la pile.
- `empiler(pile, element)`: Ajoute un élément au sommet de la pile.
- `depiler(pile)`: Retire l'élément au sommet de la pile.

## Fichier `test.py`

Le fichier `test.py` contient des exemples d'utilisation des fonctionnalités de gestion de piles et d'évaluation en notation polonaise inverse. 

### Fonctions dans `test.py`

- **Afficher une pile** : Affiche les éléments d'une pile du sommet à la base.
- **Copier une pile** : Crée une copie d'une pile donnée.
- **Hauteur de la pile** : Renvoie la hauteur de la pile.
- **Inverser des éléments** : Inverse les `j` derniers éléments de la pile.
- **Trouver le maximum** : Renvoie la position du maximum parmi les `i` derniers éléments de la pile.
- **Tri des crêpes** : Trie les éléments de la pile en utilisant la méthode des crêpes.
- **Évaluation NPI** : Évalue une expression arithmétique en notation polonaise inverse.

### Exécution de `test.py`

Pour exécuter le script, ouvrez votre terminal, naviguez vers le dossier contenant le fichier `test.py`, puis exécutez la commande suivante :

```bash
python test.py
