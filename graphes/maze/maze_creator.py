import fifo
import random as rnd
import lifo

class Labyrinth:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[1 for _ in range(cols)]for _ in range(rows)]
        self.visited = [[False for _ in range(cols)]for _ in range(rows)]
        self.stack = fifo.Pile()
        self.queue = lifo.Queue()
        self.start = None
        self.end = None

    def voisins(self, x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # Les déplacements par-dessus un mur
        voisins = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 1:
                voisins.append((nx, ny))
    
        return voisins

    def casser_mur(self, x1, y1, x2, y2):
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2  # Position du mur entre deux cellules
        self.grid[mx][my] = 0  # Le mur devient un chemin
        self.grid[x2][y2] = 0  # La cellule voisine devient aussi un chemin



    def est_mur(self, x, y):
        return self.grid[y][x] == 1

    def cell_type(self, x, y):
        return self.grid[y][x]


    def __str__(self) -> str:
        return "\n".join("".join(" " if cell == 0 else "#" for cell in row) for row in self.grid)

    def set_start_end(self, start, end):
        self.start = start
        self.end = end
        

    def generate_maze(self):
            x, y = rnd.randrange(0, self.rows, 2), rnd.randrange(0, self.cols, 2)
            self.grid[x][y] = 0

            murs = self.voisins(x, y)

            while murs:
                nx, ny = rnd.choice(murs)
                murs.remove((nx, ny))

                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                    cx, cy = nx + dx, ny + dy
                    if 0 <= cx < self.rows and 0 <= cy < self.cols and self.grid[cx][cy] == 0:
                        self.casser_mur(cx, cy, nx, ny)
                        murs.extend(self.voisins(nx, ny))
                        break


    def solve(self):
        pass

