from random import sample
from typing import List, Tuple

Coord = Tuple[int, int]
Grid = List[List[int]]
GridBool = List[List[bool]]


def gen_grid(n: int, m: int, v: int = 0) -> Grid:
    """
    Create a list of list to represent the board
    """
    return [[v for _ in range(m)] for _ in range(n)]


def place_mine(grid, n):
    h = len(grid)
    w = len(grid[0])
    total = h * w

    indices = sample(range(total), n)

    for k in indices:
        i = k // w
        j = k % w
        grid[i][j] = 1


def get_neighbours(coord: Coord, grid: Grid) -> List[Coord]:
    """
    Returns all the neighbors of a cell (y, x),
    with y being the vertical axis and x the horizontal one.
    Includes diagonals, excludes the cell itself.
    Returns (y, x) pairs (row index, then column index).
    """
    y, x = coord
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1

    neighbours: List[Coord] = []

    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            if ny == y and nx == x:
                continue  # skip the cell itself
            if 0 <= ny <= max_y and 0 <= nx <= max_x:
                neighbours.append((ny, nx))

    return neighbours


def test_mine(grid: Grid, coord: Coord) -> bool:
    """Return True if there is a mine at coord in the grid."""
    y, x = coord
    return grid[y][x] == 1


def count_near_mines(grid: Grid, coord: Coord) -> int:
    """Return the number of mines surrounding the cell at coord."""
    count = 0
    nearest_cells = get_neighbours(coord, grid)
    for y, x in nearest_cells:
        if grid[y][x] == 1:
            count += 1
    return count


def display_mines(grid: Grid) -> None:
    """Print the complete mine grid: '*' for mines, '-' for empty."""
    for row in grid:
        for cell in row:
            print("*" if cell == 1 else "-", end=" ")
        print()


def display_known(grid: Grid, known: GridBool) -> None:
    """
    Print what the player currently knows:
    - '?' for unknown cells
    - number of adjacent mines for known empty cells
    - '*' for known mines (optional but usually useful)
    """
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if not known[y][x]:
                print("?", end=" ")
            else:
                if cell == 1:
                    print("*", end=" ")
                else:
                    mines = count_near_mines(grid, (y, x))
                    print(mines, end=" ")
        print()


def get_coords(known_grid: GridBool) -> Coord:
    """
    Get coordinates from the user
    """
    max_y = len(known_grid) - 1
    max_x = len(known_grid[0]) - 1

    guess_x = -1
    guess_y = -1

    while True:
        while not (0 <= guess_x <= max_x):
            guess_x = int(input(f"Enter x between 0 and {max_x}: "))

        while not (0 <= guess_y <= max_y):
            guess_y = int(input(f"Enter y between 0 and {max_y}: "))

        if not known_grid[guess_y][guess_x]:
            return (guess_y, guess_x)

        guess_x = -1
        guess_y = -1


def is_end(known_grid: GridBool, grid: Grid) -> bool:
    """
    return True if all cells has been discovered
    """
    for y, row in enumerate(known_grid):
        for x, known in enumerate(row):
            if not test_mine(grid, (y, x)) and not known:
                return False
    return True


def linked_cells(grid: Grid, known_grid: GridBool, coord: Coord) -> list[Coord]:
    """
    Return all cells that must be revealed when the player opens `coord`,
    assuming:
    - `coord` is not a mine,
    - `coord` is currently unknown,
    - we must emulate Minesweeper expansion.

    Rules:
    - If `coord` has at least one adjacent mine: return only [coord].
    - If `coord` has zero adjacent mines:
        * reveal the entire connected region of zero-mine cells,
        * plus all numbered border cells around that region.
    The function returns coordinates only; it does not modify `known_grid`.
    """
    y0, x0 = coord
    frontier: list[Coord] = [coord]
    visited: set[Coord] = set()
    result: list[Coord] = []

    while frontier:
        cy, cx = frontier.pop()
        if (cy, cx) in visited:
            continue
        visited.add((cy, cx))

        mines_around = count_near_mines(grid, (cy, cx))
        result.append((cy, cx))

        if mines_around == 0:
            for ny, nx in get_neighbours((cy, cx), grid):
                if (ny, nx) not in visited and not known_grid[ny][nx]:
                    frontier.append((ny, nx))

    return result


if __name__ == "__main__":
    grid = gen_grid(7, 5, 0)
    place_mine(grid, 10)

    known = [[False for _ in range(5)] for _ in range(7)]
    known[1][1] = True

    display_mines(grid)
    print()
    display_known(grid, known)
