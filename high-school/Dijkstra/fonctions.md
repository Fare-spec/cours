# Dijkstra
## Fonctions
### `dijkstra(graph: dict, start: any) -> tuple`
- **Paramètres :**
  - `graph` : Dictionnaire représentant le graphe. Chaque clé est un noeud et sa valeur est une liste de tuples `(voisin, poids)`.
  - `start` : Le noeud de départ.
- **Retourne :**
  - Un tuple contenant :
    - `distances` : Un dictionnaire associant à chaque noeud la distance minimale depuis `start`.
    - `predecesseur` : Un dictionnaire associant à chaque noeud son prédécesseur dans le chemin le plus court.

---
### `reconstruct_chemin(predecesseur: dict, start: any, end: any) -> list`

- **Paramètres :**
  - `predecesseur` : Dictionnaire des prédécesseurs.
  - `start` : Le noeud de départ.
  - `end` : Le noeud d'arrivée.
- **Retourne :**
  - Une liste représentant le chemin le plus court de `start` à `end`.  
    Si aucun chemin n'est trouvé, la fonction renvoie une liste vide.

---
### `solutions_dijkstra(graph: dict, start: any) -> dict`

- **Paramètres :**
  - `graph` : Dictionnaire représentant le graphe.
  - `start` : Le noeud de départ.
- **Retourne :**
  - Un dictionnaire où chaque clé est un noeud du graphe et la valeur associée est un sous-dictionnaire contenant :
    - `"distance"` : La distance minimale depuis `start`.
    - `"chemin"` : Le chemin le plus court sous forme de liste de noeuds None si pas trouver.

---
## Utilisation 
Le graphe doit être défini sous forme de dictionnaire. Exemple :
   ```python
graph = {
   'A': [('B', 4), ('C', 2)],
   'B': [('C', 5), ('D', 10)],
   'C': [('D', 3), ('E', 8)],
   'D': [('E', 4), ('F', 11)],
   'E': [('G', 6)],
   'F': [('G', 2)],
   'G': []
}
