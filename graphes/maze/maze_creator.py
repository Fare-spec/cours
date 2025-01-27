import fifo
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

    def __str__(self) -> str:
        return "\n".join("".join(" " if cell == 0 else "#" for cell in row) for row in self.grid)
    def set_start_end(self, start, end):
        self.start = start
        self.end = end
    def generate_maze(self):
        pass

