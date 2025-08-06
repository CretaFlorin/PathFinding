from constants import CellType, CELL_SIZE, COLOR_MAP
import pygame


class Cell:
    def __init__(self, row, col, type=CellType.EMPTY):
        self.row = row
        self.col = col
        self.type = type
        self.parent = None
        self.score = 0

    def draw(self, surface):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE
        color = COLOR_MAP[self.type]

        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        if(self.type == CellType.WALL):
            pygame.draw.rect(surface, (200, 200, 200), rect, 1)
            pygame.draw.rect(surface, color, rect)
        else:
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, (200, 200, 200), rect, 1)
