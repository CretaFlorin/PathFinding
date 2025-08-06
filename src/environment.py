from constants import CellType, CELL_SIZE, WALL_CHANCE, DIRS
from cell import Cell
import pygame
from random import random


class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.init_matrix()

    def init_matrix(self):
        self.matrix = [
            [Cell(i, j, CellType.EMPTY) for j in range(self.cols)] for i in range(self.rows)
        ]

        self.matrix[self.rows//2][self.cols//4].type = CellType.START
        self.matrix[self.rows//2][self.cols//4 * 3].type =  CellType.END
        # Initialize random Walls
        for row in self.matrix:
            for cell in row:
                if random() < WALL_CHANCE and cell.type == CellType.EMPTY:
                    cell.type = CellType.WALL

    def draw(self):
        width = self.cols * CELL_SIZE
        height = self.rows * CELL_SIZE

        surface = pygame.Surface((width, height))

        for row in self.matrix:
            for cell in row:
                cell.draw(surface)
        
        return surface
    
    def get_start_end(self):
        start = end = None

        for row in self.matrix:
            for cell in row:
                if cell.type == CellType.START:
                    start = cell
                if cell.type == CellType.END:
                    end = cell
        
        return start, end
    
    def get_neighbors(self, cell):
        neighbors =[]

        for d_x, d_y in DIRS:
            r = cell.row + d_x
            c = cell.col + d_y
            if self.inside(r, c):
                neighbors.append(self.matrix[r][c])

        return neighbors
    
    def inside(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols