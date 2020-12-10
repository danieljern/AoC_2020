import time

def main():
    joltages = sorted([int(line) for line in open("input.txt").read().split("\n")])
    joltages.append(max(joltages) + 3)
    diff_joltage = get_jolt_differences(joltages)
    print(f"Part 1: 1-jolt differences * 3-jolt differences = {diff_joltage['diff1'] * diff_joltage['diff3']}")
    nbr_arrangements = get_arrangements(joltages)
    print(f"Part 2: Number of unique adapter arrangements = {nbr_arrangements}")


def get_jolt_differences(list_jolt):
    diff = {"diff1": 0,
            "diff3": 0
            }
    prev_jolt = 0 # Start with outlet joltage
    for joltage in list_jolt:
        if joltage - prev_jolt <= 3:
            diff["diff" + str(joltage - prev_jolt)] += 1
            prev_jolt = joltage
    return diff


def get_arrangements(list_jolt):
    # 0, 1, 4, 5 --> 1 unique arrangement
    # 0, 1, 4, 5, 6 --> 1 + 1 = 2 unique arrangements in total
    # 1, 4, 5, 6, 7 --> 1 + 1 + 2 = 4 unique arrangements in total
    # 1, 4, 5, 6, 7, 10 --> 4 unique arrangements in total
    # etc.
    # Iterate through list and accumulate all arrangements
    arrangements = {0: 1}   # Include outlet joltage
    for joltage in list_jolt:
        arrangements[joltage] = 0
        if joltage - 3 in arrangements:
            arrangements[joltage] += arrangements[joltage - 3]
        if joltage - 2 in arrangements:
            arrangements[joltage] += arrangements[joltage - 2]
        if joltage - 1 in arrangements:
            arrangements[joltage] += arrangements[joltage - 1]
        # print(f"{joltage}: {arrangements[joltage]}")
    return arrangements[list_jolt[-1]]


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s milliseconds ---" % (1000*(time.time() - start_time)))