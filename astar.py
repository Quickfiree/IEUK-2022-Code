from math import inf, sqrt

def hypot(x, y):
    return sqrt(x ** 2 + y ** 2)

def hCost(start, dest):
    return hypot(dest[0] - start[0], dest[1] - start[1])

def a_star(grid, start, dest_node):
    nodes = grid.get_nodes()
    closed = []
    open = [start]

    previous_node = {node : None for node in nodes}

    g = {node : inf for node in nodes}
    g[start] = 0

    f = {node : inf for node in nodes}
    f[start] = hCost(start, dest_node)

    while open:
        u = min(open, key = f.__getitem__)
        if u == dest_node:
            break

        open.remove(u)
        closed.append(u)

        for v in grid.get_adjacent(u):
            if v in closed:
                continue

            if v not in open:
                open.append(v)

            alt_g = g[u] + 1
            if alt_g < g[v]:
                g[v] = alt_g
                f[v] = g[v] + hCost(v, dest_node)
                previous_node[v] = u

    path = [dest_node]
    current_node = dest_node

    while previous_node[current_node]:
        path.append(previous_node[current_node])
        current_node = previous_node[current_node]

    return list(reversed(path))
