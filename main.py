from grid import Grid
from astar import a_star

def main():
    # Initialise the grid 
    g = Grid(10, 10, obstacles = [(7,7), (6, 8), (8, 7), (9, 7)])
    start = (0, 0)
    dest = (9, 9)

    print("1 = Obstacle\n0 = Empty space\nP = Path")

    print("\nPath using A* search algorithm:")
    print(g.plot_path(a_star(g, start, dest)))

if __name__ == "__main__":
    main()
