import time
import math

def main():
    instructions = [[line[0],line[1:]] for line in open("input.txt").read().split("\n")]

    x1_curr = 0     # East: >0, West <0
    y1_curr = 0     # North: >0, South <0
    dir1_curr = 0   # East: 0 rad, North: pi/2 rad, West: pi rad, South 3*pi/2 rad
    x2_curr = 0
    y2_curr = 0
    x_waypoint = 10    # Waypoint starts 10 units east
    y_waypoint = 1     # Waypoint starts 1 unit north
    for instruction in instructions:
        x1_new, y1_new, dir1_new = get_new_coord1(x1_curr, y1_curr, dir1_curr, instruction)
        x1_curr = x1_new
        y1_curr = y1_new
        dir1_curr = dir1_new
        x2_new, y2_new, x_waypoint_new, y_waypoint_new = get_new_coord2(x2_curr, y2_curr, x_waypoint, y_waypoint, instruction)
        x2_curr = x2_new
        y2_curr = y2_new
        x_waypoint = x_waypoint_new
        y_waypoint = y_waypoint_new
    print(f"Part 1: The ship's Manhattan position = {int(abs(x1_curr) + abs(y1_curr))}")
    print(f"Part 2: The ship's Manhattan position = {int(abs(x2_curr) + abs(y2_curr))}")


def get_new_coord1(x_curr, y_curr, dir_curr, action):
    act = action[0]
    value = int(action[1])
    x = x_curr
    y = y_curr
    angle = dir_curr
    if act == "N":
        y = y_curr + value
    elif act == "S":
        y = y_curr - value
    elif act == "E":
        x = x_curr + value
    elif act == "W":
        x = x_curr - value
    elif act == "L":
        angle = dir_curr + value * math.pi / 180
    elif act == "R":
        angle = dir_curr - value * math.pi / 180
    elif act == "F":
        x = x_curr + value * math.cos(dir_curr)
        y = y_curr + value * math.sin(dir_curr)
    return x, y, angle


def get_new_coord2(x_curr, y_curr, x_way, y_way, action):
    act = action[0]
    value = int(action[1])
    x = x_curr
    y = y_curr
    x_way_new = x_way
    y_way_new = y_way
    if act == "N":
        y_way_new = y_way + value
    elif act == "S":
        y_way_new  = y_way - value
    elif act == "E":
        x_way_new = x_way + value
    elif act == "W":
        x_way_new = x_way - value
    elif act == "L":
        angle = value * math.pi / 180
        x_way_new = x_way * math.cos(angle) - y_way * math.sin(angle)
        y_way_new = x_way * math.sin(angle) + y_way * math.cos(angle)
    elif act == "R":
        angle = value * math.pi / 180
        x_way_new = x_way * math.cos(angle) + y_way * math.sin(angle)
        y_way_new = - x_way * math.sin(angle) + y_way * math.cos(angle)
    elif act == "F":
        x = x_curr + x_way * value
        y = y_curr + y_way * value
    return x, y, x_way_new, y_way_new


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))