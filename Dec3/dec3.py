import math
import time

def main():
    x_key = [1, 3, 5, 7, 1]
    y_key = [1, 1, 1, 1, 2]

    max_x = max(x_key)
    tree_grid = create_grid("input.txt", max_x)
    # for n in range(len(tree_grid)):
    #    print(f"{tree_grid[n]}")

    nbr_of_trees = len(x_key)*[0]
    product = 1
    for n in range(len(x_key)):
        nbr_of_trees[n] = tree_encounter(tree_grid, x_key[n], y_key[n])
        # print(f"Trees encountered: {nbr_of_trees[n]}")
        product *= nbr_of_trees[n]
    print(f"Part 1: Trees encountered = {nbr_of_trees[1]}")
    print(f"Part 2: Product = {product}")


def create_grid(inputfile, key_x):
    grid = [list(line) for line in open(inputfile).read().split('\n')]
    grid_length = len(grid)
    # print(f"grid_length = {grid_length}")
    grid_width = len(grid[0])
    # print(f"grid_width = {grid_width}")
    factor_width = math.ceil(key_x * (grid_length-1) / grid_width)
    grid0 = grid.copy()
    for row in range(grid_length):
        temp = grid0[row]
        #print(f"temp = {temp}")
        grid[row].extend((factor_width-1)*temp)
        # print(f"grid[{row}] = {grid[row]}\n")
    return grid


def tree_encounter(grid, key_x, key_y):
    counter = 0
    x = 0
    y = 0
    for row in grid:
        # print(f"row = {y}, y = {x}")
        if y < len(grid):
            if grid[y][x] == '#':
                counter += 1
            x += key_x
            y += key_y
            # print(f"x = {x}, y = {y}")
    return counter


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s milliseconds ---" % (1000*(time.time() - start_time)))