from enum import Enum

CELL_SIZE = 20
ROWS = 50
COLS = 70

WALL_CHANCE = 0.35
DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


class CellType(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3
    VISITED = 4
    PATH = 5


COLOR_MAP = {
    CellType.EMPTY: (255, 255, 255),
    CellType.WALL: (0, 0, 0),
    CellType.START: (0, 255, 0),
    CellType.END: (200, 200, 0),
    CellType.VISITED: (255, 150, 150),
    CellType.PATH: (100, 100, 255)
}
