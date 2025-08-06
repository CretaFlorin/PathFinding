import pygame
import pygame.time
from environment import Environment
from bfs_pathfinder import BFSPathFinder
from a_star_pathfinder import AStarPathFinder

from constants import CELL_SIZE, ROWS, COLS

pygame.init()

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
env = Environment(ROWS, COLS)
a_star_pf = AStarPathFinder(env)
bfs_pf = BFSPathFinder(env)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    a_star_pf.step()
    # bfs_pf.step()
    grid_surface = env.draw()

    screen.blit(grid_surface, (0, 0))

    pygame.display.update()

pygame.quit()
