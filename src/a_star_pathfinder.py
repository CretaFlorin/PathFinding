from constants import CellType
import math

class AStarPathFinder:
    def __init__(self, env):
        self.env = env
        self.start, self.end = self.env.get_start_end()
        self.queue = [self.start]
        self.over = False
        self.current = None

    def step(self):
        if self.over:
            self.show_path_step()
        else:
            self.astar_step()

    def astar_step(self):
        if self.over:
            return

        if len(self.queue):
            self.queue.sort(key=lambda cell: cell.score)
            current = self.queue.pop(0)

            if current == self.end:
                self.over = True
                self.current = self.end
                return

            for n in self.env.get_neighbors(current):
                if n.type == CellType.EMPTY or n.type == CellType.END:
                    self.queue.append(n)
                    if n.type == CellType.EMPTY:
                        n.type = CellType.VISITED
                    n.parent = current
                    distance_from_start = math.sqrt((n.row - self.start.row)**2 + (n.col - self.start.col)**2)
                    distance_to_end = math.sqrt((n.row - self.end.row)**2 + (n.col - self.end.col)**2)
                    n.score = distance_from_start + distance_to_end


    def show_path_step(self):
        if self.current.parent:
            self.current = self.current.parent
            if self.current.type == CellType.VISITED:
                self.current.type = CellType.PATH
