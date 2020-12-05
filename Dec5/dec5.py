import time
import re


def main():
    seat_ids = get_seat_ids("input.txt")
    print(f"Part 1: Highest seat ID = {max(seat_ids)}")
    my_seat_id = find_my_seat(seat_ids)
    print(f"Part 2: My seat ID = {my_seat_id}")


def get_seat_ids(inputfile):
    id_list = []
    for line in open(inputfile).read().split("\n"):
        # Transform letters -> binary -> decimal
        row = int(re.split(r"[LR]{3}", line)[0].replace("F", "0").replace("B", "1"), 2)
        seat = int(re.split(r"[FB]{7}", line)[1].replace("L", "0").replace("R", "1"), 2)
        id_list.append(8 * row + seat)

    sorted_ids = sorted(id_list, reverse=False)
    return sorted_ids


def find_my_seat(seat_ids):
    min_id = min(seat_ids)
    max_id = max(seat_ids)
    # Create range of all seat ids
    id_comp = range(min_id, max_id + 1)
    # print(f"set(id_comp) - set(seat_ids) = {set(id_comp) - set(seat_ids)}")
    # Return the difference between all seat ids and occupied seat ids
    return list(set(id_comp) - set(seat_ids))[0]


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s milliseconds ---" % (1000*(time.time() - start_time)))