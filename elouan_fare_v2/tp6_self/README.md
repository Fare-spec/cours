
# **README - DM Piles et NPI**

## **Comment exécuter le programme :**  
1. Verfier que tous les fichiers sont dans le même répertoire :  
   - `test.py`  
   - `Pile_Tuple.py`  
   - `Pile_LSC.py`  
   - `Pile_Liste.py`
   - `npi.py`
2. Ouvrez un terminal dans ce répertoire.
3. Exécutez le programme avec la commande suivante :  
   ```bash
   python3 test.py
   ```
    ou executer pour la notation polonaise inverse:
    ```bash
    python3 npi.py
    ```
---

## **Fonctions disponibles et leur utilisation :**  

### 1. **`creer_pile_vide()`**  
- **Description** : Crée et renvoie une pile vide.
- **Utilisation** :  
  ```python
  pile = creer_pile_vide()
  ```

---

### 2. **`est_pile_vide(pile)`**  
- **Description** : Vérifie si une pile est vide.  
- **Paramètre** :  
  - `pile` : La pile à vérifier.  
- **Retour** : Renvoie `True` si la pile est vide, sinon `False`.  
- **Utilisation** :  
  ```python
  if est_pile_vide(pile):
      print("La pile est vide.")
  ```

---

### 3. **`sommet(pile)`**  
- **Description** : Retourne l’élément au sommet de la pile sans le retirer.  
- **Paramètre** :  
  - `pile` : La pile à consulter.  
- **Retour** : L’élément au sommet de la pile.  
- **Utilisation** :  
  ```python
  print(sommet(pile))
  ```

---

### 4. **`empiler(pile, elt)`**  
- **Description** : Ajoute un élément au sommet de la pile.  
- **Paramètres** :  
  - `pile` : La pile à modifier.  
  - `elt` : L’élément à empiler.  
- **Retour** : La nouvelle pile avec l’élément ajouté.  
- **Utilisation** :  
  ```python
  pile = empiler(pile, 5)
  ```

---

### 5. **`depiler(pile)`**  
- **Description** : Retire l’élément au sommet de la pile.  
- **Paramètre** :  
  - `pile` : La pile à modifier.  
- **Retour** : La pile sans l’élément au sommet.  
- **Utilisation** :  
  ```python
  pile = depiler(pile)
  ```

---

### 6. **`hauteur_pile(pile)`**  
- **Description** : Renvoie le nombre d'éléments présents dans la pile sans la modifier.  
- **Paramètre** :  
  - `pile` : La pile à analyser.  
- **Retour** : La hauteur de la pile (nombre d'éléments).  
- **Utilisation** :  
  ```python
  print(hauteur_pile(pile))
  ```

---

### 7. **`max_pile(pile, i)`**  
- **Description** : Trouve le maximum parmi les `i` premiers éléments de la pile.  
- **Paramètres** :  
  - `pile` : La pile à analyser.  
  - `i` : Le nombre d'éléments à prendre en compte depuis le sommet.  
- **Retour** : Le maximum trouvé parmi les `i` éléments.  
- **Utilisation** :  
  ```python
  print(max_pile(pile, 3))
  ```

---

### 8. **`retourner(pile, j)`**  
- **Description** : Inverse l’ordre des `j` premiers éléments de la pile.  
- **Paramètres** :  
  - `pile` : La pile à modifier.  
  - `j` : Le nombre d'éléments à inverser.  
- **Retour** : La pile modifiée.  
- **Utilisation** :  
  ```python
  pile = retourner(pile, 2)
  ```

---

### 9. **`tri_crepes_recursif(pile)`**  
- **Description** : Trie une pile en suivant le tri des crêpes.  
- **Paramètre** :  
  - `pile` : La pile à trier.  
- **Retour** : La pile triée.  
- **Utilisation** :  
  ```python
  pile = tri_crepes_recursif(pile)
  ```
<hr>

Cela conclut la documentation des fonctions. Pour toute question, consultez le fichier **test.py** pour des exemples plus détaillés.
pour toutes questions: elouan.fare@protonmail.ch