from constants import CellType

class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.init_matrix()

    def init_matrix(self):
        self.matrix = [[CellType.EMPTY for _ in self.cols] for _ in range(self.rows)]
        self.matrix[0][0] = CellType.START
        self.matrix[self.rows - 1][self.cols - 1] = CellType.END
        # Initialize random Walls