import time
import numpy as np


def main():
    temp = [list(line) for line in open("input.txt").read().split("\n")]
    seats = np.array(temp)
    grid = np.copy(seats)
    new_grid1 = np.copy(seats)
    no_changes = False
    while no_changes == False:
        for i in range(seats.shape[0]):
            for j in range(seats.shape[1]):
                if grid[i, j] != ".":
                    new_grid1[i, j] = get_next(grid, i, j, "part1")
        if (new_grid1==grid).all():
            no_changes = True
        else:
            grid[:] = new_grid1[:]
    print(f"Part 1: Number of occupied seats = {np.count_nonzero(new_grid1 == '#')}")

    grid = np.copy(seats)
    new_grid2 = np.copy(seats)
    no_changes = False
    while no_changes == False:
        for i in range(seats.shape[0]):
            for j in range(seats.shape[1]):
                if grid[i, j] != ".":
                    new_grid2[i, j] = get_next(grid, i, j, "part2")
        if (new_grid2==grid).all():
            no_changes = True
        else:
            grid[:] = new_grid2[:]
    print(f"Part 2: Number of occupied seats = {np.count_nonzero(new_grid2 == '#')}")


def get_next(grid, ix, iy, part):
    count_hash = 0
    element = grid[ix, iy]
    if ix == 0:
        adj_x = [0, 1]
    elif ix == grid.shape[0] - 1:
        adj_x = [-1, 0]
    else:
        adj_x = [-1, 0, 1]
    if iy == 0:
        adj_y = [0, 1]
    elif iy == grid.shape[1] - 1:
        adj_y = [-1, 0]
    else:
        adj_y = [-1, 0, 1]
    for x in adj_x:
        for y in adj_y:
            if [ix+x, iy+y] != [ix, iy]:
                if part == "part1":
                    comp = grid[ix+x, iy+y]
                else:
                    comp = get_closest_seat(grid, ix, iy, x, y)
                if element == "L" and comp == "#":
                    return "L"
                if element == "#" and comp == "#":
                    count_hash += 1
    if part == "part1":
        if element == "#" and count_hash >= 4 :
            return "L"
    else:
        if element == "#" and count_hash >= 5:
            return "L"
    if element == "L" and count_hash > 0:
        return "L"
    else:
        return "#"


def get_closest_seat(grid, x_coor, y_coor, x_dir, y_dir):
    while x_coor + x_dir >= 0 and x_coor + x_dir < grid.shape[0] and y_coor + y_dir >= 0 and y_coor + y_dir < grid.shape[1]:
        if grid[x_coor + x_dir, y_coor + y_dir] != ".":
            return grid[x_coor + x_dir, y_coor + y_dir]
        x_coor += x_dir
        y_coor += y_dir
    return "."


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))