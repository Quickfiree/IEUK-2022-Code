from itertools import product

class Grid(object):
    #Initialise the grid
    def __init__(self, x, y, obstacles = []):
        self.x = x
        self.y = y
        self.grid = [[0] * x for _ in range(y)]

        self.obstacles = obstacles

        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = 1

    def __str__(self):
        return "\n".join("".join(x) for x in self.char_map())

    #Printing the grid
    def __repr__(self):
        return "{} by {} grid:\n".format(self.x, self.y) + self.__str__()

    #Mapping the grid according to arguments given in main
    def char_map(self):
        arr = [["0 "] * self.y for _ in range(self.x)]

        for obstacle in self.obstacles:
            arr[obstacle[0]][obstacle[1]] = "1 "

        return arr

    def get_adjacent(self, node):
        i = node[0]
        j = node[1]

        if i < 0 or i >= self.x or j < 0 or j >= self.y:
            raise Exception("Out of bounds")

        if self.grid[i][j] != 0:
            return []

        adjacent = []

        for del_pos in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= i + del_pos[0] < self.y and 0 <= j + del_pos[1] < self.y:
                if self.grid[i + del_pos[0]][j + del_pos[1]] == 0:
                    adjacent.append((i + del_pos[0], j + del_pos[1]))

        return adjacent

    def get_nodes(self):
        return [(i, j) for i, j in product(range(self.x), range(self.y)) if (i, j) not in self.obstacles]

    #Plot nodes on visualiser using given path
    def plot_path(self, path):
        arr = self.char_map()
        for node in path:
            arr[node[0]][node[1]] = "P "

        return "\n".join("".join(x) for x in arr)
