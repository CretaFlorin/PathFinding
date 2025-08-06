from constants import CellType

class BFSPathFinder:
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
            self.bfs_step()

    def bfs_step(self):
        if self.over:
            return

        if len(self.queue):
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

    def show_path_step(self):
        if self.current.parent:
            self.current = self.current.parent
            if self.current.type == CellType.VISITED:
                self.current.type = CellType.PATH
