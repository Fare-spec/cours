import pygame
import random
import sys

# Paramètres de la grille
CELL_SIZE = 20          # Taille d'une cellule en pixels
COLS = 30               # Nombre de colonnes
ROWS = 30               # Nombre de lignes
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)

class Cell:
    def __init__(self, i, j):
        self.i = i  # Numéro de la colonne
        self.j = j  # Numéro de la ligne
        # Chaque cellule possède 4 murs, tous présents initialement
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw(self, surface):
        """Dessine la cellule et ses murs sur la surface donnée."""
        x = self.i * CELL_SIZE
        y = self.j * CELL_SIZE

        # Remplir la cellule (si visitée) AVANT de dessiner les murs
        if self.visited:
            pygame.draw.rect(surface, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
        
        # Dessiner les murs par-dessus la couleur de fond
        if self.walls['top']:
            pygame.draw.line(surface, WHITE, (x, y), (x + CELL_SIZE, y))
        if self.walls['right']:
            pygame.draw.line(surface, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
        if self.walls['bottom']:
            pygame.draw.line(surface, WHITE, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE))
        if self.walls['left']:
            pygame.draw.line(surface, WHITE, (x, y + CELL_SIZE), (x, y))

def get_cell(i, j):
    """Retourne la cellule aux coordonnées (i, j) si elle existe."""
    if 0 <= i < COLS and 0 <= j < ROWS:
        return grid[i][j]
    return None

def get_unvisited_neighbors(cell):
    """Retourne la liste des voisins non visités de la cellule donnée."""
    neighbors = []
    i, j = cell.i, cell.j
    # Voisin du haut
    top = get_cell(i, j - 1)
    if top and not top.visited:
        neighbors.append(top)
    # Voisin de droite
    right = get_cell(i + 1, j)
    if right and not right.visited:
        neighbors.append(right)
    # Voisin du bas
    bottom = get_cell(i, j + 1)
    if bottom and not bottom.visited:
        neighbors.append(bottom)
    # Voisin de gauche
    left = get_cell(i - 1, j)
    if left and not left.visited:
        neighbors.append(left)
    
    return neighbors

def remove_walls(current, next_cell):
    """
    Enlève les murs entre la cellule courante et le voisin sélectionné.
    """
    dx = next_cell.i - current.i
    dy = next_cell.j - current.j
    if dx == 1:  # Voisin à droite
        current.walls['right'] = False
        next_cell.walls['left'] = False
    elif dx == -1:  # Voisin à gauche
        current.walls['left'] = False
        next_cell.walls['right'] = False
    elif dy == 1:  # Voisin en bas
        current.walls['bottom'] = False
        next_cell.walls['top'] = False
    elif dy == -1:  # Voisin en haut
        current.walls['top'] = False
        next_cell.walls['bottom'] = False

def main():
    global grid
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labyrinthe généré par DFS")
    clock = pygame.time.Clock()

    # Création de la grille : une matrice de cellules
    grid = [[Cell(i, j) for j in range(ROWS)] for i in range(COLS)]
    
    # Initialisation de l'algorithme DFS
    current = grid[0][0]  # Départ en haut à gauche
    current.visited = True
    stack = []

    running = True
    finished = False  # Indique si la génération est terminée

    while running:
        clock.tick(60)  # Limite à 60 images par seconde
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Exécution de l'algorithme DFS tant que la génération n'est pas terminée
        if not finished:
            neighbors = get_unvisited_neighbors(current)
            if neighbors:
                # Choix aléatoire d'un voisin non visité
                next_cell = random.choice(neighbors)
                stack.append(current)
                remove_walls(current, next_cell)
                current = next_cell
                current.visited = True
            elif stack:
                # Revenir en arrière si aucun voisin n'est disponible
                current = stack.pop()
            else:
                # Génération terminée
                finished = True

        # Affichage
        screen.fill(BLACK)
        # Dessiner toutes les cellules de la grille
        for i in range(COLS):
            for j in range(ROWS):
                grid[i][j].draw(screen)

        # Mettre en évidence la cellule courante (seulement si la génération est en cours)
        if not finished:
            x = current.i * CELL_SIZE
            y = current.j * CELL_SIZE
            pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

