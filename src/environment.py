from constants import CellType, CELL_SIZE
from cell import Cell
import pygame


class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.init_matrix()

    def init_matrix(self):
        self.matrix = [
            [Cell(i, j, CellType.EMPTY) for j in range(self.cols)] for i in range(self.rows)
        ]

        self.matrix[0][0].type = CellType.START
        self.matrix[self.rows - 1][self.cols - 1].type =  CellType.END
        # Initialize random Walls

    def draw(self):
        width = self.cols * CELL_SIZE
        height = self.rows * CELL_SIZE

        surface = pygame.Surface((width, height))

        for row in self.matrix:
            for cell in row:
                cell.draw(surface)
        
        return surface