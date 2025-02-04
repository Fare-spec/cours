import random as rnd

class Labyrinth:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        # Grille initiale : 1 = mur, 0 = chemin
        self.grid = [[1 for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.end = None

    def voisins(self, x, y):
        """
        Retourne les voisins valides (encore des murs) de la cellule (x, y).
        """
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        voisins = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 1:
                voisins.append((nx, ny))
        
        return voisins

    def casser_mur(self, x1, y1, x2, y2):
        """
        Casse le mur entre les cellules (x1, y1) et (x2, y2).
        """
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2  # Coordonnées du mur à casser
        self.grid[mx][my] = 0  # Transformer le mur en chemin
        self.grid[x2][y2] = 0  # Transformer la cellule voisine en chemin

    def generate_maze(self):
        """
        Génère un labyrinthe parfait à l'aide de l'algorithme de Prim.
        """
        # Choisir une cellule de départ aléatoire
        x, y = rnd.randrange(0, self.rows, 2), rnd.randrange(0, self.cols, 2)
        self.grid[x][y] = 0  # Transformer la cellule en chemin

        # Liste des murs candidats (voisins de la cellule initiale)
        murs = self.voisins(x, y)

        while murs:
            # Choisir un mur aléatoire
            nx, ny = rnd.choice(murs)
            murs.remove((nx, ny))

            # Trouver une cellule voisine qui est déjà un chemin
            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                cx, cy = nx + dx, ny + dy
                if 0 <= cx < self.rows and 0 <= cy < self.cols and self.grid[cx][cy] == 0:
                    # Casser le mur entre les deux cellules
                    self.casser_mur(cx, cy, nx, ny)
                    # Ajouter les nouveaux murs adjacents
                    murs.extend(self.voisins(nx, ny))
                    break

    def set_start_end(self, start, end):
        """
        Définit les points de départ et d'arrivée du labyrinthe.
        """
        self.start = start
        self.end = end

    def __str__(self) -> str:
        """
        Représente le labyrinthe sous forme de chaîne de caractères.
        """
        return "\n".join("".join(" " if cell == 0 else "#" for cell in row) for row in self.grid)

